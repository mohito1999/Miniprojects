import time, sys
indent = 0 #how many spaces to indent
indentIncreasing = True #whether indentation is increasing or # # not

try:
    while True:
        print(' '*indent, end="") #''*indent keeps track of how many spaces before the asteriks
        print('********')
        time.sleep(0.1) #sleep for 1/10 of a second

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False #Changes direction

        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except(KeyboardInterrupt):
    sys.exit()
