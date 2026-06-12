f1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
f1.writelines(L)
f1.close()

# Append-adds at last
f1 = open("myfile.txt", "a")  
f1.write("Today \n")
f1.close()

f1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(f1.readlines())
print()
f1.close()

# Write-Overwrites
f1 = open("myfile.txt", "w")  
f1.write("Tomorrow \n")
f1.close()

f1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(f1.readlines())
print()
f1.close()