
# small pizza - $10
# medium pizza - $15
# large pízza - $20
# Pepperoni - $5 - não pode ser um valor fixo, pois irá variar de acordo com o tamanho da pizza
# pepS - $3 , pepM - $5 , pepL - $7 
# Extra Cheese - $3 - mesma ideia do pep
# ext_cheeseS - $3 , ext_cheeseM - $5 , ext_cheeseL - $7


# MY FIRST TRY
# bill = 0
# if size == "S":
#     bill += 10
#     if pepperoni == "Y":
#         bill += 5
#     elif pepperoni == "N":
#         bill == bill
#     else:
#         print("Please tell me if you want or not pepperoni.")
#     if extra_cheese == "Y":
#             bill += 3
#     elif extra_cheese == "N":
#             bill == bill
#     else:
#             print("Please tell me if you want or not extra cheese.")
# elif size == "M":
#     bill += 15
#     if pepperoni == "Y":
#         bill += 5
#     elif pepperoni == "N":
#         bill == bill
#     else:
#         print("Please tell me if you want or not pepperoni.")
#     if extra_cheese == "Y":
#         bill += 3
#     elif extra_cheese == "N":
#         bill == bill
#     else:
#         print("Please tell me if you want or not extra cheese.")
# elif size == "L":
#     bill += 20
#     if pepperoni == "Y":
#         bill += 5
#     elif pepperoni == "N":
#         bill == bill
#     else:
#         print("Please tell me if you want or not pepperoni.")
#     if extra_cheese == "Y":
#         bill += 3
#     elif extra_cheese == "N":
#         bill == bill
#     else:
#         print("Please tell me if you want or not extra cheese.")
# else:
#     print("Choose a correct size.")


# print(f"According to your order the total is going to be: {bill}")

print("Welcome to Python Pizzaz Deliveries!")

while True:
    size = input("What size pizza do you want? S, M or L:\n").upper()

    if size in ("S", "M", "L"):
        break


    print("Incorrect size. Try again!")

print(f"Chosen size: {size}")#



while True:
    pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n").upper()

    if pepperoni in ("Y", "N"):
        break


    print("Incorrect answer. Try again!")

print(f"Chosen option: {pepperoni}")
    

while True:
    extra_cheese = input("Do you want pepperoni on your pizza? Y or N:\n").upper()

    if extra_cheese in ("Y", "N"):
        break

    print("Incorrect answer. Try again!")

print(f"Chosen option: {extra_cheese}")




bill = 0

if size == "S":
    bill += 10
    if pepperoni == "Y":
        bill += 3
    elif pepperoni == "N":
        bill == bill
    else: 
        print("Please tell me if you want or not pepperoni.")

    if extra_cheese == "Y":
        bill += 3
    elif extra_cheese == "N":
        bill == bill
    else:
        print("Please tell me if you want or not extra cheese.")

elif size == "M":
    bill += 15
    if pepperoni == "Y":
        bill += 5
    elif pepperoni == "N":
        bill == bill
    else: 
        print("Please tell me if you want or not pepperoni.")
        
    if extra_cheese == "Y":
        bill += 5
    elif extra_cheese == "N":
        bill == bill
    else:
        print("Please tell me if you want or not extra cheese.")

elif size == "L":
    bill += 20
    if pepperoni == "Y":
        bill += 7
    elif pepperoni == "N":
        bill == bill
    else: 
        print("Please tell me if you want or not pepperoni.")

    if extra_cheese == "Y":
        bill += 7
    elif extra_cheese == "N":
        bill == bill
    else:
        print("Please tell me if you want or not extra cheese.")    
else:
    print()


print(f"Your order resulted in a total of: {bill}")

