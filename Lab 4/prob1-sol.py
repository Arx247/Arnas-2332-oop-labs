# Arnas Oonsadao, 633040233-2
"""
Lab 4 Errors and Exceptions: Problem 1 'prob1-sol.py'
"""
patients = [[70, 1.80], [58, 1.55], [100, 1.90]]
n = 0
def calculate_bmi(_weight, _height):
    return _weight / (_height * 2)

for patient in range(1,4):
    weight, height = patients[n]
    bmi = calculate_bmi(weight, height)
    n += 1
    print(f"Patient's BMI is: {bmi:0.02f}")

