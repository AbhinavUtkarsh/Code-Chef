file = open("MyFile.txt","a") 
print(400-2)
for i in range(3,58):
    string=str(str(i)+" "+str(i//2)+"\n")
    file.write(string)
    for j in range(i,0,-1):
        string2=str(str(j)+" ")
        file.write(string2)
    file.write("\n")