
try:
    print(x)  
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")    
    
#Part Two

try:
    print(x)
except NameError:
    print("Variable x is undefined")
else:
    print("Everything went wrong")
    
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")                    