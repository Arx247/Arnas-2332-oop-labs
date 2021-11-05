#Arnas Oonsadao
#633040233-2
# Lab 11.  Useful modules : Problem 4 Writing data into CSV files
import csv

# gpa_max = 4.0
with open("numbers.csv", "w", newline="") as numbers:
    csv_writer = csv.writer(numbers)
    csv_writer.writerows([[2, 4, 6], [3, 7, 5], [8, 9, 7]])

with open("numbers.csv", "r") as rows:
    with open("numbers2.csv", "w", newline="") as numbers2:
        rows = csv.reader(rows)
        csv_writer2 = csv.writer(numbers2)
        for row in rows:
            row.sort()
            gpa_1 = row[0]
            gpa_2 = row[1]
            gpa_3 = row[2]
            highest_gpa = row[len(row) - 1]
            avg = row[len(row) // 3]
            avg_gpa = float(avg)
            show_row = [highest_gpa, gpa_2, gpa_1, avg_gpa]
            print(show_row)
            csv_writer2.writerow(show_row)



# import csv
# with open('number.csv',"w") as f:
# r = csv.reader(f)
#     for row in r:
#         print("{},{},{},{ :0.2f}".format(row[2].strip(),row[1].strip(),row[0].strip(),row[1].strip()))