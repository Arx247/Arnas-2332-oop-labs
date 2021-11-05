#Arnas Oonsadao
#633040233-2
# Lab 11.  Useful modules : Problem 3.  Search pattern in text
import re

str1 = input("Enter text: ")
str2 = input("Enter pattern: ")
index = str1.find(f"{str2}")
match = re.findall(f"{str2}",str1)
if match:
    print(f"Found {str2} in {str1} at {index}")
else:
    print(f"Cannot find {str2} in {str1}")
