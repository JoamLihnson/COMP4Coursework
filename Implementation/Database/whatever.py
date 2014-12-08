ListedFields = ["Donator", "DonatorID", "DonatorFirstName", "DonatorLastName", "DonatorAddress1", "DonatorAddress2", "DonatorCity", "DonatorCounty", "DonatorPostCode", "DonatorContact"]
completeList = (ListedFields[0] + " (" + ListedFields[1])
for count in range(len(ListedFields)-2):
    completeList = (completeList + ", " + ListedFields[count+2])
completeList = (completeList + ")")
print(completeList)
