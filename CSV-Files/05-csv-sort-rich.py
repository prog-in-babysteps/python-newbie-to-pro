import csv
from rich.console import Console
from rich.table import Table
import operator

console = Console()

def print_table(header, data):

    # Initialize a Rich table layout
    table = Table(show_header=True, header_style="bold magenta")
    for col in header:
        table.add_column(col.title())

    for row in data:
        # Convert to string before printing
        row = tuple(str(x) for x in row)
        table.add_row(*row)

    console.print(table)

with open('student-marks.csv', 'r') as sm_file:
    sm_csv_reader = csv.reader(sm_file)
    header = next(sm_csv_reader)

    data = []
    for row in sm_csv_reader:
        # Convert RollNo. and Marks to integer
        data.append([int(row[0]), row[1], int(row[2]),
                     int(row[3]), int(row[4]), int(row[5]),
                     int(row[6]), int(row[7])])

    print("Before Sorting:")
    print_table(header, data)

    while (True):
        colnum = int(input("Enter the Column to Sort: "))
        if colnum == -1:
            break

        sorted_data = sorted(data, key=operator.itemgetter(colnum), reverse=True)
        print_table(header, sorted_data)
