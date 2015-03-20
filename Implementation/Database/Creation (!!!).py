import sqlite3

def CreateTable(databaseName, table_name,sql):
     with sqlite3.connect(databaseName) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("This table already exists! Recreate table?: ")
            if response == "y":
                keep_table = False
                cursor.execute("drop table if exists {}".format(table_name))
                db.commit()
            else:
                print("No changes made.")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def CreateStaffTable():
    sql = """create table Staff
             (StaffID text,
             StaffFirstName text,
             StaffLastName text,
             primary key(StaffID))"""
    CreateTable(databaseName, "Staff", sql)

def CreateItemTable():
    sql = """create table Item
             (ItemCode text,
             ItemDescription text,
             ItemPrice real,
             ItemCategory text,
             ItemQualityCheck integer,
             ItemStatus text,
             primary key(ItemCode)
             foreign key(ItemCategory) references Category(ItemCategory))"""
    CreateTable(databaseName, "Item", sql)
    
def CreateCategoryTable():
    sql = """create table Category
             (ItemCategory text,
             ItemCategoryDescription text,
             primary key(ItemCategory))"""
    CreateTable(databaseName, "Category", sql)
    
def CreateDonationTable():
    sql = """create table Donation
             (DonationCode text,
             ItemCode text,
             DonatorID text,
             StaffID text,
             Date text,
             primary key(DonationCode)
             foreign key(ItemCode) references Item(ItemCode)
             foreign key(DonatorID) references Donator(DonatorID)
             foreign key (StaffID) references Staff(StaffID))"""
    CreateTable(databaseName, "Donation", sql)

def CreateDonatorTable():
    sql = """create table Donator
             (DonatorID text,
             DonatorFirstName text,
             DonatorLastName text,
             DonatorAddress1 text,
             DonatorAddress2 text,
             DonatorCity text,
             DonatorCounty text,
             DonatorPostCode text,
             DonatorContact text,
             primary key(DonatorID))"""
    CreateTable(databaseName, "Donator", sql)


    

if __name__ == "__main__":
    databaseName = "charityShop.db"
    CreateStaffTable()
    CreateCategoryTable()
    CreateItemTable()
    CreateDonatorTable()
    CreateDonationTable()
