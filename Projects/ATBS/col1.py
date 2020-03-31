from sys import exit

def collatz(number):
        if number % 2 == 0:
            result = number // 2

        elif number % 2 == 1:
            result = number * 3 + 1

        while number != 1:
            number = result
            print(number) #the very first return statement executed will end the function thats why I was struggling for it to work when I was using a return statement for the print as well
            return collatz(number) #you are returning the function such that it runs again when this while condition is met

        if number == 1:
            print(number)
            exit()

num = int(input("Enter an integer: "))

run = collatz(num)

print(run)
