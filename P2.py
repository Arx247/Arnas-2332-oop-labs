#Arnas Oonsadao, 633040233-2
"""
Lab 2 Variables and Collections: Problem 2
"""
from re import A

name = input("Please enter your Student ID: ")
if name > '0':
    print("Welcome!")
else:
    print("Please enter your student ID again")
mark = input("Please enter your midterm mark(0-100): ")
if int(mark) in range(0, 100):
    m1 = str
elif mark == chr():
    print("Please enter a mark as a decimal number")
else:
    print("Please enter a mark in range [0,100]")
mark2 = input("Please enter your final mark(0-100): ")
if int(mark) in range(0, 100):
    m2 = str
else:
    print("Please enter a mark in range [0,100]")
markm = float(mark)*0.4
markf = float(mark2)*0.6
total = float(markm)+float(markf)
if total in range(80, 100):
    totalA = 'A'
    print("Student ID %s has the total mark as %s and has grade as %s" % (name, total,totalA))
elif total in range(70, 79):
    totalB = 'B'
    print("Student ID %s has the total mark as %s and has grade as %s" % (name, total, totalB))
elif total in range(60, 69):
    totalC = 'C'
    print("Student ID %s has the total mark as %s and has grade as %s" % (name, total, totalC))
elif total in range(50, 59):
    totalD = 'D'
    print("Student ID %s has the total mark as %s and has grade as %s" % (name, total, totalD))
elif total < 50:
     totalF = 'F'
     print("Student ID %s has the total mark as %s and has grade as %s"%(name,total,totalF))