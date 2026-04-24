# # File Handling
# file = open("demo.txt","r")
# print("File name:",file.name)
# print("File Mode:",file.mode)
# print("Is closed?:",file.closed)
# file.close()
# print("Is closed?:",file.closed)

# # Reading the content
# file = open("demo.txt","r")
# content = file.read()
# print(content)
# file.close()

# # Writing the file
# with open("demo.txt","w") as file:
#     file.write("File Writing demo\n")
#     file.write("Example of file handling")

# print("File Edited Successfully")

# # Handling the Exception
# try:
#     file = open("demo.txt","r")
#     content = file.read()
#     print(content)

# except FileNotFoundError as e:
#     print("File Not Found",e)

# finally:
#     file.close()

# # Modes in File Handling
# # Read the file
# with open("demo.txt","r") as file:
#     content = file.read()
#     print(content)

# Write the file
# with open("demo.txt","w") as file:
#     file.write("Hello")

# # Append the file
# with open("demo.txt","a") as file:
#     file.write("\nThis is a new line")

# # binary of the file - binary should be combine with any of read, write,append
# with open("demo.txt","rb") as file:
#     data = file.read()
#     print(data)

# # Read and Write Mode - If the file exists already ,it will work. Otherwise, it will give an FileNotFoundError
# with open("demo.txt","r+") as file:
#     content = file.read()
#     # file.write("\nThis is a new line")
#     print(content)

# # Write and Read Mode - If the file exists already, it will write and read. Otherwise, it will create file with the given name and do the work
# with open("example.txt","w+") as file:
#     file.write("Demo of w+")
#     content = file.read()
#     print(content)