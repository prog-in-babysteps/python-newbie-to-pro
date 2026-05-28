import csv

with open("student-marks.csv") as sm_file:
    sm_csv_reader = csv.reader(sm_file)
    for row in sm_csv_reader:
        print(row)
