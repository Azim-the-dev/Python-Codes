num = int(input("Enter a num: "))
count = 0
i = 1

while(i <= num):
    if(num % i == 0):
        count += 1
    i += 1
    
if(count == 2):
    print("The num " + str(num) + " is prime.")
else:
    print("The num " + str(num) + " is not prime.")