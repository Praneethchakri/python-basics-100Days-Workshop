file_read = open('data.txt','r')
file_red_Content = file_read.read()
file_read.close()
print(file_red_Content)

data = input("Enter Name: ")
file_Data = open('data.txt','w')# w mode will override the data which the file is already having..
file_Content = file_Data.write(data)
file_Data.close()

