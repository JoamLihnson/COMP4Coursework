import sqlite3

#Displays the initial menu of options
def Menu():
    print("Would you like to...")
    print()
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. End")
    return

#You select which entities you wish to work with.
def Selection():
    print("Would you like to change...")
    print()
    print("1. Staff")
    print("2. Donator")
    print("3. Category")
    print("4. Item")
    print("5. Donation")
    print("6. Return to previous menu")
    selection = int(input(">>"))
    if selection == 1:
        Selected, Questioned, ListedFields = SelectStaff()
        return(Selected, Questioned, ListedFields)
    elif selection == 2:
        Selected, Questioned, ListedFields = SelectDonator()
        return(Selected, Questioned, ListedFields)
    elif selection == 3:
        Selected, Questioned, ListedFields = SelectCategory()
        return(Selected, Questioned, ListedFields)
    elif selection == 4:
        Selected, Questioned, ListedFields = SelectItem()
        return(Selected, Questioned, ListedFields)
    elif selection == 5:
        Selected, Questioned, ListedFields = SelectDonation()
        return(Selected, Questioned, ListedFields)
    else:
        return (0,0,0)
        
        
          


def Insert():
    with sqlite3.connect("charityShop.db") as db:
        Selected, Questioned, ListedFields = Selection()
        if Selected == 0:
            return(0)
        cursor = db.cursor()
        sql = "insert into {} values {}".format(Selected, Questioned)
        values = []
        for count in range(len(ListedFields)):
            values.append(0)
        for count in range(len(ListedFields)):
            values[count] = input("{} :".format(ListedFields[count]))
        values = tuple(values)
        cursor.execute(sql, values)
        db.commit()
        completion = 1
        return(1)

def Delete():
    return





          
def SelectStaff():
    Selected = "Staff (StaffID, StaffFirstName, StaffLastName)"
    Questioned = "(?,?,?)"
    ListedFields = ["StaffID", "StaffFirstName", "StaffLastName"]
    return(Selected, Questioned, ListedFields)

def SelectDonator():
    Selected = "Donator (DonatorID, DonatorFirstName, DonatorLastName, DonatorAddress1, DonatorAddress2, DonatorCity, DonatorCounty, DonatorPostCode, DonatorContact)"
    Questioned = "(?,?,?,?,?,?,?,?,?)"
    ListedFields = ["DonatorID", "DonatorFirstName", "DonatorLastName", "DonatorAddress1", "DonatorAddress2", "DonatorCity", "DonatorCounty", "DonatorPostCode", "DonatorContact"]
    return(Selected, Questioned, ListedFields)

def SelectCategory():
    Selected = "Category (ItemCategory, ItemCategoryDescription)"
    Questioned = "(?,?)"
    ListedFields = ["ItemCategory", "ItemCategoryDescription"]
    return(Selected, Questioned, ListedFields)

def SelectItem():
    Selected = "Item (ItemCode, ItemDescription, ItemPrice, ItemCategory, ItemQualityCheck, ItemStatus)"
    Questioned = "(?,?,?,?,?,?)"
    ListedFields = ["ItemCode", "ItemDescription", "ItemPrice", "ItemCategory", "ItemQualityCheck", "ItemStatus"]
    return(Selected, Questioned, ListedFields)

def SelectDonation():
    Selected = "Donation (DonationCode,ItemCode, DonatorID, StaffID, Date)"
    Questioned = "(?,?,?,?,?)"
    ListedFields = ["DonationCode", "ItemCode", "DonatorID", "StaffID", "Date"]
    return(Selected, Questioned, ListedFields)




if __name__ == "__main__":   
    Menu()
    menuSelect = int(input(">>"))
    if menuSelect == 1:
        completion = Insert()
        if completion == 1:
            print("Values added!")
        else:
            print("Addition aborted")
    elif menuSelect == 2:
        Delete()
