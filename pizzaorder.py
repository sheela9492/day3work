print("Welcome tp python pizza deliveries!")
size = input("What size pizza do you want? S, M or L:").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N:").upper()
extra_cheese = input("Do you want extra cheese on your pizza? Y or N: ").upper()
bill = 0
# work for size of pizza
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Sorry, i don't understand your size ")
# work for you want pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    if size == "M" or size == "L":
        bill += 3
#work for you want cheese
if extra_cheese == "Y":
    bill += 1
print(f"your final amount ${bill}.")