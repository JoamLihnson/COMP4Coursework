import sqlite3

#For whatever reason, Adam did it this way, so I am too :v
#The multiBinds variable is there to prevent binding errors, as if you refernce an unequal amount of fields
#there is an error, and different functions require different amounts. Insert needs many, delete needs 1
#So, this method allows both versions of code to run as long as I tell it if its working with more than 1 field
def Query (sql, data, multiBinds, method):
    with sqlite3.connect("charityShop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        if not multiBinds:
            cursor.execute(sql, (data,))
        else:
            cursor.execute(sql, data)
        if method == "Select":
            selected = cursor.fetchone()
            db.commit()
            return(selected)
        db.commit()

        
#Displays the initial menu of options
def Menu():
    print("Would you like to...")
    print()
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. End")
    print()
    return

#You select which entities you wish to work with.
def EntSelect():
    print("Would you like to change...")
    print()
    print("1. Staff")
    print("2. Donator")
    print("3. Category")
    print("4. Item")
    print("5. Donation")
    print("6. Return to previous menu")
    print()
    selection = int(input(">>"))
    print()
    if selection == 1:
        Questioned, ListedFields = SelectStaff()
        return(Questioned, ListedFields)
    elif selection == 2:
        Questioned, ListedFields = SelectDonator()
        return(Questioned, ListedFields)
    elif selection == 3:
        Questioned, ListedFields = SelectCategory()
        return(Questioned, ListedFields)
    elif selection == 4:
        Questioned, ListedFields = SelectItem()
        return(Questioned, ListedFields)
    elif selection == 5:
        Questioned, ListedFields = SelectDonation()
        return(Questioned, ListedFields)
    else:
        return (0,0)


def Insert():
    with sqlite3.connect("charityShop.db") as db:
        Questioned, ListedFields = EntSelect()
        if Questioned == 0:
            return(0)
        cursor = db.cursor()
# Since the format of the string is very specfic, it would require it to be hardcoded from every seperate entity and every action
# Instead, I have made it so that it manipulates the contents of the ListFields list (which contains the names for every part of every entity)
# The string is therefore constucted by using FOR loops and string editing, so this process can be applied to whatever I throw at it
        completeList = (ListedFields[0] + " (" + ListedFields[1])
        for count in range(len(ListedFields)-2):
            completeList = (completeList + ", " + ListedFields[count+2])    
        completeList = (completeList + ")")
        sql = "insert into {} values {}".format(completeList, Questioned)
        values = []
        for count in range(len(ListedFields) - 1):
            values.append(0)
        for count in range(len(ListedFields) - 1):
            values[count] = input("Enter the {} :".format(ListedFields[count +1]))
        values = tuple(values)
        Query(sql, values, True, "Insert")
        completion = 1
        return(1)

def Delete():
    with sqlite3.connect("charityShop.db") as db:
        cursor = db.cursor()
        print("Would you like to delete...")
        print("1. All Data")
        print("2. Entity Specfic Data")
        print("3. Return to previous menu")
        Choice = int(input(">>"))
        print()
        if Choice == 1:
                    print("The code to delete everything does exist, but I'm not letting it run out of danger of it DELETING ALL DATA AJHSJKHAKS")
                    deleteAll = False
                    print()
                    print("Would you really like to run it?")
                    Choice = input(">>")
                    if Choice in ("Y","y","Yes","yes"):
                        deleteAll = True
                    if deleteAll:
                        sql = ("delete from Staff")
                        cursor.execute(sql)
                        sql = ("delete from Donator")
                        cursor.execute(sql)
                        sql = ("delete from Category")
                        cursor.execute(sql)
                        sql = ("delete from Item")
                        cursor.execute(sql)
                        sql = ("delete from Donation")
                        cursor.execute(sql)
                        print("its all gone ;_;7")
                    return
        elif Choice == 2:
            Questioned, ListedFields = EntSelect()
            print("Would you like to delete data by referncing from the field...")
            for count in range (len(ListedFields) - 1):
                print("{}. {}".format(count + 1, ListedFields[count + 1]))
            Choice = int(input(">>"))
            print()
            print("What is the data you will use to reference...")
            refData = input(">>")
            print()
            sql = "delete from {} where {}=?".format(ListedFields[0], ListedFields[Choice])
            print(sql)
            Query(sql, refData, True, "Delete")
            print("Deleted!")
            print()
        return

def Update():
    with sqlite3.connect("charityShop.db") as db:
        cursor = db.cursor()
        Questioned, ListedFields = EntSelect()
        print("Enter the primary key for the entry you would like to update: ")
        primKey = int(input(">>"))
        print()
        completeList = (ListedFields[1] + "," + ListedFields[2])
        for count in range(len(ListedFields)-3):
            completeList = (completeList + "," + ListedFields[count+3])
        sql = "select {} from {} where {}=?".format(completeList,ListedFields[0],ListedFields[1])
        selected = Query(sql, primKey, False, "Select")
        for count in range(len(ListedFields)-1):
            print("{}: {}".format(ListedFields[count+1], selected[count]))
        print()
        stopRepeat = False
        while not stopRepeat:
            print("Which value would you like to change?")
            for count in range (len(ListedFields)-1):
                print("{}. {}".format(count+1,ListedFields[count+1]))
            print("{}. End updating".format(len(ListedFields)))
            print()
            Choice = int(input(">>"))
            if Choice > 0 and Choice < (len(ListedFields)-1):
                print("Enter a new value for the {} field".format(ListedFields[Choice]))
                newData = input(">>")
                print()
                sql = "update {} set {}=? where {}={}".format(ListedFields[0], ListedFields[Choice], ListedFields[1], primKey)
                Query(sql, newData, False, "Update")
                print("Update Successful!")
            else:
                stopRepeat = True                     
    return





# All these SelectEntity functions have the atributes of each entity hardcoded in so that they can be manipulated in a way that Python understands
# This allows for flexability when making changes to different entities, as it won't require indivdual method functions be written for each individual entity
def SelectStaff():
    Questioned = "(?,?,?)"
    ListedFields = ["Staff", "StaffID", "StaffFirstName", "StaffLastName"]
    return(Questioned, ListedFields)

def SelectDonator():
    Questioned = "(?,?,?,?,?,?,?,?,?)"
    ListedFields = ["Donator", "DonatorID", "DonatorFirstName", "DonatorLastName", "DonatorAddress1", "DonatorAddress2", "DonatorCity", "DonatorCounty", "DonatorPostCode", "DonatorContact"]
    return(Questioned, ListedFields)

def SelectCategory():
    Questioned = "(?,?)"
    ListedFields = ["Category", "ItemCategory", "ItemCategoryDescription"]
    return(Questioned, ListedFields)

def SelectItem():
    Questioned = "(?,?,?,?,?,?)"
    ListedFields = ["Item", "ItemCode", "ItemDescription", "ItemPrice", "ItemCategory", "ItemQualityCheck", "ItemStatus"]
    return(Questioned, ListedFields)

def SelectDonation():
    Questioned = "(?,?,?,?,?)"
    ListedFields = ["Donation", "DonationCode", "ItemCode", "DonatorID", "StaffID", "Date"]
    return(Questioned, ListedFields)




if __name__ == "__main__":
    repeatMenu = True
    while repeatMenu:
        Menu()
        menuSelect = int(input(">>"))
        print()
        if menuSelect == 1:
            completion = Insert()
            if completion == 1:
                print("Values added!")
            else:
                print("Addition aborted")
            print()
        elif menuSelect == 2:
            Update()
        elif menuSelect == 3:
            Delete()
        elif menuSelect == 4:
            repeatMenu = False
