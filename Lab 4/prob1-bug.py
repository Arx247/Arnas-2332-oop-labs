# Arnas Oonsadao, 633040233-2
"""
prob1-bug.py
"""
patients = [[70, 1.80], [58, 1.55], [100, 1.90]]


def calculate_bmi(_weight, _height):
    return _weight / (_height * 2)


for patient in patients:
    weight, height = patients[0]
    bmi = calculate_bmi(height, weight)
    print(f"Patient's BMI is: {bmi:0.02f}")

