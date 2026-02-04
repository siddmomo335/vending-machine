
                                                                        #vending Machine
items = {
    "A1": ("Chips", 15),
    "A2": ("Cookie", 20),                                                #here the codes that i will run it for machine
    "A3": ("Sweet", 25),
    "A4": ("Chocolate", 30) 
}                                                                                                                               

print("Welcome to the vending Machine!")
print("Items available:")                                                   #that the machine print when running the code
                                                                           
for key in items:
    name, price = items[key]
    print(key, "-", name, "($", price, ")", sep="")                       #that is the key for code that i will do it

choice = input("Choose an item (A1/A2/A3/A4): ")                          #chosing the code in the input way 

if choice in items:
    item_name, item_price = items[choice]
    money = int(input("Insert money: "))

    if money >= item_price:
        change = money - item_price
        print("You got:", item_name)
        print("Your change is:", change)
    else:
        print("Not enough money. Money returned.")                       #here the mony if it is not enough the code will get that
else:
    print("Invalid choice.")                                             #if i will enter the code in worng way

for key in items:
    name, price = items[key]
    print(key, "-", name, "($", price, ")", sep="")                      #that is the key for code that i will do it 

choice = input("Choose an item (A1/A2/A3/A4): ")                         #chosing the code in the input way

if choice in items:
    item_name, item_price = items[choice]
    money = int(input("Insert money: "))  

    if money >= item_price:
        chanye = money - item_price
        print("You got:", item_name)
        print("Your change is:", change)
    else:
        print("Not enough money. Money returned.")                      #here the money if it is not enough the code will get 
else:
    print("Invalid choice.")                                            # if i will enter the code in wrong way
v
