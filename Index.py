input("Power of 4: n % 3 == 1 \n Power of 8: n % 7 == 1. Press Enter")
print(" 16 Binary - ", bin(16)[2:], " 16 % 3 =", 16 % 3, " power of 4 - Yes")
print(" 8 Binary - ", bin(8)[2:], " 8 % 7 =", 8 % 7, " power of 8 - Yes")

n = int(input("Enter a no. (try 64 or 32) : "))
Guess = input("Is " + str(n) + " a power of 4? (Yes / No) : ")
input("Check : n % 3 == 1. Press Enter ")
s_pow4 = n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
if s_pow4:
    print(" ", n, "binary - ", bin(n)[2:], "power of 4 - Yes \n Your Guess - ", Guess)
else:
    print(" ", n, "binary - ", bin(n)[2:], "power of 4 - No \n Your Guess - ", Guess)