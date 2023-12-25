import random
#message
print("Start GAME")
print("\n*Ranking*\n1-Exelent\n2-Best\n3-Good\n4-NeedTry\n5-Noob")
print("\n*** Guess My Number ***")
#VALUES
x = int(random.randint(1,100))
n = int()
p = int()
#RUN
while p != x:
    p = int(input("\n* Guess * : "))
    n += 1
    if p == x:
        print("Wow You Win")
    elif p >= x:
        print("Oh No , Come Down")
    elif p <= x:
        print("Oh No , Come Higher")
#Rank
if n <= 3:
    print("Your IQ Has Exelent 100%")
elif 4 >= n <= 5:
    print("Your IQ Has Best 80%")
elif 6 >= n <= 7:
    print("Your IQ Has Good 50%")
elif 8 >= n <= 10:
    print("Your IQ Has NeedTry 30%")
else:
    print("Your IQ Has Noob 0%")
#END
print("END GAME")