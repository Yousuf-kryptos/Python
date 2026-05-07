# # File Handling - use open() to open the file and it includes filename, mode of opening the file 
# # Modes: r - Read(default value) - open a file for reading, returns error if the file does not exists
# #       w - Write - open a file for writing , create file if the file does not exists
# #       a - Append - open a file for appending, creates file if the file does not exists
# #       x - create new specified file , returns an error if file is already exists
# # In Addition, we can specify if the file should be handled as binary or text mode
# #       t - Text - default value - Text Mode
# #       b - Binary - binary mode

# f = open("demotext.txt","r")      # Default Reading mode
# f = open("demotext.txt","rt")     # Reading mode with Default Text
# f = open("demotext.txt",'b')      # Default Reading mode with binary mode 

# f = open("demotext.txt",'r')
# print(f.read())
# f.close()

# # using with statement - it will open the file and manage the closing part also

# with open ("demotext.txt",'r') as f:
#     print(f.read())

# # we can also specify how may characters to be return

# with open ("demotext.txt",'r') as f:
#     print(f.read(5))

# # we can also return one line in the file and by calling it two times we can return two lines

# with open ("demotext.txt",'r') as f:
#     print(f.readline())
#     print(f.readline())

# # Read using for loop

# with open ("demotext.txt",'r') as f:
#     for x in f:
#         print(x)

# # Write in the existing file
# # 'w' - will overwrite teh content in the existing file
# # 'a' - will append to the end of the file

# with open("demotext.txt",'a') as f:
#     f.write("\nI am working with Python")

# with open ("demotext.txt",'r') as f:
#     print(f.read())

# with open ("demotext.txt",'w') as f:
#     f.write("I have deleted the content")

# with open ("demotext.txt",'r') as f:
#     print(f.read())

# # Create a new file

# f = open("newfile.txt","x")
# with open ("newfile.txt",'w') as f:
#     f.write("New Content Updated")

# with open ("newfile.txt",'a') as f:
#     f.write("\nContent Appended") 

# with open ("newfile.txt",'r') as f:
#     print(f.read())

# # Delete the file

import os
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("The file does not exists")