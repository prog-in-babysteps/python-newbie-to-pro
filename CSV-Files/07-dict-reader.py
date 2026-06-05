import csv

with open("data\\customer-details.csv", 'r') as customer_file:
    customer_reader = csv.DictReader(customer_file)
    for row in customer_reader:
        print(row)
