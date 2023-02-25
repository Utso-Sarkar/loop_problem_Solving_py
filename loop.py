infinite loop



while True:
    print("Enter your name:")
    name=input()
    if name=="your name":
        break
    print("Thank you!")










odd_sum------------1+3+5+7+9+11+13+15............100


odd_sum=0
for i in range(1,101,2):
    odd_sum=odd_sum+i
print(odd_sum)








continue statement
while True:
    print("Who are you?")
    name=input()
    if name!="Utso":
        continue
    print("Hello Utso ! How can i help you ? For help give me your passcode:")
    passcode=input()
    if passcode=="lolypop":
        break
print("Thank you!")



series-------------1+2+3+4
sum=0
for i in range(1,5):
    sum=sum+i
print(sum)




# series-------------------------1^2+2^2+3^2+4^2+.......
sum=0
for i in range(1,5):
    sum=sum+i*i
print(sum)




Leap year.................

year=int(input("Enter the year:"))
if year%400==0:
    print("It's a leap year")
elif year%100==0:
    print("it's not a leap year")
elif year%4==0:
    print("it's a leap year")
else:
    print("It's not a leap year")


# pattarn painting:1
number=int(input())
sum=0
for i in range(0,number):
    for j in range(0,number-i-1):
        print(end=" ")
    sum=sum+1
    for k in range(0,i+sum):
        print("%",end="")
    print(" ")    






