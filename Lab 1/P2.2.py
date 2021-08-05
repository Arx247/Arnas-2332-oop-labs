#Lab 1 : Problem 2
#Problem 2.2

theSum = 0
count = 0
average = 0


while True:
    num = input("Enter a positive number ")
    if num < '0':
        
        break
    
    theSum += float(num)
    count += 1
    
average = theSum/count
print("The average number of the list is ", average)
