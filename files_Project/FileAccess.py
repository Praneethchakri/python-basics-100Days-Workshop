file_read = open('data.txt','r')
file_red_Content = file_read.read()
file_read.close()
print(file_red_Content)

data = input("Enter Name: ")
file_Data = open('data.txt','w')
file_Content = file_Data.write(data)
file_Data.close()

