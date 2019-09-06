cont=0
punctuation=".;!,:?"
while(cont==0):
    lower=0
    upper=0
    number=0
    error=0
    spaces=0

    punct=0
    password=input("Please input a password for your account ")
    length=len(password)
    if(length>=6):
        if(length<=20):
            i=0
            while(i<=length-1):
                letter=password[i]
                if letter.islower():
                    lower=lower+1
                elif letter.isupper():
                    upper=upper+1
                elif letter.isdigit():
                    number=number+1
                elif letter==" ":
                    spaces=spaces+1
                p=0
                while p<=5:
                    if letter==punctuation[p]:
                        punct=punct+1
                    p=p+1
                i=i+1
            if (punct>=1):
                print("Password cannot contain punctuation")
            if(spaces>=1):
                print("Password cannot contain spaces")
            if (lower==0):
                print("Password must have 1 lowercase letter ")
            if (upper==0):
                print("Password must have 1 uppercase letter ")
            if (number==0):
                print("Password must include number ")
            if(punct==0 and spaces==0 and lower!=0 and upper!=0 and number!=0):
                print("Password Accepted ")
        else:
            print("Password must be less than or equal to 20 characters ")
    else:
        print("Password must be greater than or equal to 6 characters ")
