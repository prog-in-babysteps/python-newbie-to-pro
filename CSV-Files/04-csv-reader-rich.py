import csv
from rich.console import Console
from rich.table import Table

console = Console()

with open('student-marks.csv', 'r') as sm_file:
    sm_csv_reader = csv.reader(sm_file)
    header = next(sm_csv_reader)

    # Initialize a Rich table layout
    table = Table(show_header=True, header_style="bold magenta")
    for col in header:
        table.add_column(col.title())

    for row in sm_csv_reader:
        table.add_row(*row)

console.print(table)
