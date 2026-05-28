import csv

# Register a custom dialect
csv.register_dialect("cutom_dialect", delimiter=';', skipinitialspace=True)

with open("student-marks-new.csv") as sm_file:
    sm_csv_reader = csv.reader(sm_file, dialect='cutom_dialect')
    for row in sm_csv_reader:
        print(row)
