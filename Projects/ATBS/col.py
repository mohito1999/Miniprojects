def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    if number % 2 == 1:
        result = number * 3 + 1
        print(result)
        return result

    
while num != 1:
    num = collatz(num) #reason for this is that the function keeps repeating separately until num = 1 so each number printed is as if the function is being reexecuted with the previous output
