file=open("people.txt",'r')
while True:
    dict={}
    finalList=[]
    for line in file:
        line=line.rstrip("\n")
        list=line.split(",")
        name=list[0]
        del list[0]
        values=list
        values=set(values)
        dict.update({name:values})
    for key in dict:
        print(key)
    while True:
        try:
            name1=input("Choose name one: ")
            set1=dict[name1]
            break
        except KeyError:
            print("That name doesn't exist")
    while True:
        try:
            name2=input("Choose name two: ")
            set2=dict[name2]
            break
        except KeyError:
            print("That name doesn't exist")
    print("What they have in commmon: ")
    print(" ".join((set1).intersection(set2)))
    print("What is unique to ",name1,": ")
    print(" ".join(set1.difference(set2)))
    print("What is unique to ",name2,": ")
    print(" ".join(set2.difference(set1)))
    print("All the interests they do not have in common: ")
    print(" ".join(set2.symmetric_difference(set1)))
    answer=input("Would you like to continue? (yes or no)")
    if answer=="yes":
        print(" ")
    elif answer=="no":
        break
