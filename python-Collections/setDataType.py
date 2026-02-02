art_students={"Praneeth","Ramesh","Suresh"}
science_students={"Suresh","Hareesh","Ramesh"}
# differnce() method
art_but_not_science_Diff = art_students.difference(science_students)
print(art_but_not_science_Diff)

science_but_not_art = science_students.difference(art_students)
print(science_but_not_art)


diguvapalem_family={"Chandra","Praneeth","Sushma","Nagamani"}
p_Family={"Sushma","Prasad","Vijayalakshmi"}

diguvapalem_family_only = diguvapalem_family.difference(p_Family)
print(diguvapalem_family_only)

p_Family_only = p_Family.difference(diguvapalem_family)
print(p_Family_only)



# difference() --> The elements which are not in one another.. eg: line 4
# & symmetric_difference --> The elements which are not the common from both sets -- eg line 28,30
#intersection : --> Common elements from both sets --> Line eg 34

group_A = {'Sachin','Sehwag','Dravid'}
group_B = {'Dhoni','Ganguly','Sachin'}

symetricData0 = group_A.symmetric_difference(group_B)
print(symetricData0)
symetricData1 = group_B.symmetric_difference(group_A)
print(symetricData1)
intersectionData = group_A.intersection(group_B)
print(intersectionData)


