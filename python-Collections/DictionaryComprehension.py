
player_Name = ["Sachin","Dhoni","Ganguly","Samson"]
jersey_Number = [10,7,99,49]


team_Dic = {
    player_Name[i]:jersey_Number[i]
    for i in range(len(player_Name))
    if jersey_Number[i] < 8
}
print(f"Team Captains : ",team_Dic)



# using Zip fuction to convert the set/list to dict


result = dict(zip(player_Name,jersey_Number))
print(f'Result as Dictionary :: {result}')

resultAsList= list(zip(player_Name,jersey_Number))
print(f'Result as List using Zip function which returns as List of Tuples :: {result}')