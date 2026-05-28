import csv
from tabulate import tabulate

with open("student-marks.csv") as sm_file:
    sm_csv_reader = csv.reader(sm_file)
    header = next(sm_csv_reader)
    data = list(sm_csv_reader)

print(tabulate(data, headers=header, tablefmt='grid'))

