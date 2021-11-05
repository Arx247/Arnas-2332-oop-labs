#Arnas Oonsadao
#633040233-2
# Lab 11.  Useful modules : Problem 1. Generating a strong password
import random
import string

p1 = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
join1 = ''.join(p1)
p2 = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
ranp2 = ''.join(random.choice(p2) for i in range(5))
join2 = ''.join(join1 + ranp2)
print("Random password is:", join2)