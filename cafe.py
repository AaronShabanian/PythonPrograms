#gets order from user and creates bill
price=0
print("""
small tea - $2.00
medium tea - $3.25
large tea - $4.50
small coffee- $3.50
medium coffee- $3.50
large coffee- $4.75"""
)
x=0
while(x==0):
    type=input("Would you like coffee or tea? ")
    if(type=="coffee"):
        coffeeSize=input("Would you like a small, medium or large coffee ").lower()
        if(coffeeSize=="small"):
            print("A small coffee with a price of $2.25 has been added to your order ")
            price=price + 2.25
        elif(coffeeSize=="medium"):
            vanilla= input("Would you like a shot of vanilla flavored syrup for an additional 25 cents? ").lower()
            if(vanilla=="yes"):
                print("A medium coffee with a shot of vanilla flavores syrup with a price of 3.75 has been added to your order")
                price=price+3.75
            elif(vanilla=="no"):
                print("A medium coffee with a price of $3.50 has been added to your order ")
                price=price + 3.50
            else:
                print("invalid input, try again")

        elif(coffeeSize=="large"):
            vanilla= input("Would you like a shot of vanilla flavored syrup for an additional 25 cents? ").lower()
            if(vanilla=="yes"):
                print("A medium coffee with a shot of vanilla flavores syrup with a price of 5.00 has been added to your order")
                price=price+5.00
            elif(vanilla=="no"):
                print("A medium coffee with a price of $4.75 has been added to your order ")
                price=price + 4.75
            else:
                print("invalid input, try again")
        else:
            print("invalid input, try again")
    elif(type=="tea"):
        teaSize=input("Would you like a small, medium or large tea ").lower()
        if(teaSize=="small"):
            print("A small tea with a price of $2.00 has been added to your order ")
            price=price + 2.00
        elif(teaSize=="medium"):
            print("A medium tea with a price of $3.25 has been added to your order ")
            price=price + 3.25
        elif(teaSize=="large"):
            vanilla= input("Would you like a  fancy, organic, or Oprah- sponsored option for an additional 50 cents? ").lower()
            if(vanilla=="yes"):
                print("A large tea with a shot of vanilla flavores syrup with a price of 5.00 has been added to your order")
                price=price+5.00
            elif(vanilla=="no"):
                print("A large tea with a price of $4.75 has been added to your order ")
                price=price + 4.75
            else:
                print("invalid input")
        else:
            print("invalid input")
    else:
        print("invalid input")
    complete=input("Is your order complete?(yes or no)").lower()
    if complete=="yes":
        x=1
    elif complete=="no":
        x=0
    else:
        print("invalid input")
print("Your total bill is $",price, " have a good day")
