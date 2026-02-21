
player_Name = ["Sachin","Dhoni","Ganguly","Samson"]
jersey_Number = [10,7,99,49]


team_Dic = {
    player_Name[i]:jersey_Number[i]
    for i in range(len(player_Name))
    if jersey_Number[i] < 8

}
print(f"Team Captains : ",team_Dic)
