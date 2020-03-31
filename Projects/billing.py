#This is the first iteration of this program, eventually, I want to use functions to simplify the program

print("Welcome to the billing system\nPlease enter the prices of the products and the associated discounts\nWhen you want to get your total, press ctrl-c")

items = []
discount_rates = []
total = []
province = 0.07
gst = 1.05 + province
final_price = []


try:  ##here, the try/except block basically says that try the code until there is an error (keyboardInterrupt) at which point break the loop
    while True:
        item_price = float(input("Enter the price of the item: "))
        discount = float(input("Enter the discount rate: "))
        items.append(item_price)
        discount_rates.append(discount)
except KeyboardInterrupt:
    print("\nYour list of items is printed below!")



for i in range(len(items)): #sets range to length of list (e.g. if 3 items, range is 3) --> range(len(list)) is good because for loops are not inclusive thus it helps includes all since the len method gives you the number of elements in the list which starts counting from 1
        final = items[i] * (1 - discount_rates[i]) #does the discounting process
        total.append(final) #appends the final variable result to the total list
        #loop restarts after this with next element

print(total)

for i in range(len(total)):  #here we are first setting up the range for which we want to run through total later (nth index + 1 (b/c exclusive))
    taxed = total[i] * gst  #setting up variable to store GST inclusive price
    final_price.append(taxed) #store GST inclusive price in an empty list named final_price



print('Your total bill is:', sum(final_price)) #sum function can sum all elements in a list
