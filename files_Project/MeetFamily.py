familyMembers = input("Enter the family member name to meet in Person").split(",")

family_data_frm_file = open("family.txt","r")
familyMembers_data = [familyPerson.strip() for familyPerson in family_data_frm_file.readlines()]

family_data_frm_file.close()


familyMembers_set = set(familyMembers)
family_data_frm_file_set = set(familyMembers_data)

actual_family_set = familyMembers_set.intersection(family_data_frm_file_set)

actual_family_to_file = open("ActualFamily.txt","w")

for memberName in actual_family_set:
    print(f"{memberName} is my family member.. Happy to Meet...")
    actual_family_to_file.write(f"{memberName} /n")

actual_family_to_file.close()







