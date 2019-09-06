new=[]
filename=input("what is the name of the file?: ")
distance=int(input("How many letters would you like to shift: "))
def encrypt(filename, distance):
    text=open(filename,"r")
    for line in text:
        for char in line:
            if char.isalpha():
                if char.islower():
                    newchar=chr(ord(char)+distance)
                    if newchar.isalpha():
                        newchar=newchar
                    else:
                        neword=ord(char)-(26-distance)
                        newchar=chr(neword)
                    new.append(newchar)
                if char.isupper():
                    newchar=chr(ord(char)+distance)
                    if newchar.isalpha():
                        newchar=newchar
                    else:
                        neword=ord(char)-(26-distance)
                        newchar=chr(neword)
                    new.append(newchar)
            else:
                new.append(char)
encrypt(filename,distance)
print("".join(new))
