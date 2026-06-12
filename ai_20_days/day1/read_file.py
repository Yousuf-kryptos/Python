with open("student_marks.csv","r") as file:
    data = file.readlines()
    for index, line in enumerate(data):
        print(index,line)

print(data)

f1 = open("myfile.txt", "w")  
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

f1.write("Hello \n")          
f1.writelines(L)             
f1.close()                   

f1 = open("myfile.txt", "r+") 

print("Output of read():")
print(f1.read())              
print()

f1.seek(0)                    
print("Output of readline():")
print(f1.readline())          
print()

f1.seek(0)
print("Output of read(9):")
print(f1.read(9))             
print()

f1.seek(0)
print("Output of readline(9):")
print(f1.readline(9))         
print()

f1.seek(0)
print("Output of readlines():")
print(f1.readlines())         
print()

f1.close()