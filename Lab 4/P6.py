# Arnas Oonsadao, 633040233-2
"""
Lab 4 Errors and Exceptions: Problem 6 [Extra Credit]
"""
try:
    def sum_of_list(numbers):
        return sum(numbers)

    def average(sum, n):
        return sum / n

    def final_data(data):
        for item in data:
            print("Average:", average(sum_of_list(item), len(item)))
    list1 = [10, 20, 30, 40, 50]
    list2 = [100, 200, 300, 400, 500]
    # empty list
    list3 = []
    lists = [list1, list2, list3]
    final_data(lists)
except ZeroDivisionError:
    print("The list is empty")

