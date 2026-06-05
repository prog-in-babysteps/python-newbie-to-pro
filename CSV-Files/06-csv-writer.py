import csv

contact_details = [
    ["First Name", "Last Name", "Company", "City", "Email"],
    ["Akash", "Ganesh", "Tata Motors", "Delhi", "akash.ganesh@example.in"],
    ["Vikram", "Mehta", "Bajaj Auto", "Bengaluru", "vikram.mehta2@example.in"],
    ["Chitra", "Kumar", "HDFC Bank", "Bhopal", "chitra.kumar@example.in"],
    ["Priya", "Senthil", "Axis Bank", "Ahmedabad", "priya.senthil@example.in"],
    ["Radha", "Ilango", "Zomato", "Chennai", "radha.ilango@example.in"],
    ["Ayush", "Hariharan", "TCS", "Hyderabad", "ayush.hariharan@example.in"],
]

csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL)

with open("data\\contact-details.csv", 'w', newline='') as contact_file:
    contact_writer = csv.writer(contact_file, dialect='myDialect')
    for row in contact_details:
        contact_writer.writerow(row)
    print("Records are written successfully")
