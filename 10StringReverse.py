s = input("Enter the string : ")
rev = ""
for i in range(len(s),0,-1):
    rev = rev + s[i-1]
print("Reverse of string is :",rev)
