import csv

mountain_list = [
    {
        "MOUNTAIN": "Everest",
        "HEIGHT": "8848",
        "RANGE": "Mahalangur Himalaya",
        "LOCATION": "Nepal",
    },
    {
        "MOUNTAIN": "Kilimanjaro",
        "HEIGHT": "5895",
        "RANGE": "Eastern Rift Mountains",
        "LOCATION": "Tanzania",
    },
    {
        "MOUNTAIN": "K2",
        "HEIGHT": "8611",
        "RANGE": "Baltoro Karakoram",
        "LOCATION": "Pakistan",
    },
    {
        "MOUNTAIN": "Kangchenjunga",
        "HEIGHT": "8586",
        "RANGE": "Kangchenjunga Himalaya",
        "LOCATION": "Nepal",
    },
    {
        "MOUNTAIN": "Aconcagua",
        "HEIGHT": "6961",
        "RANGE": "Andes",
        "LOCATION": "Argentina",
    },
    {
        "MOUNTAIN": "Denali",
        "HEIGHT": "6190",
        "RANGE": "Alaska Range",
        "LOCATION": "United States",
    },
    {
        "MOUNTAIN": "Elbrus",
        "HEIGHT": "5642",
        "RANGE": "Caucasus Mountains",
        "LOCATION": "Russia",
    },
    {
        "MOUNTAIN": "Vinson Massif",
        "HEIGHT": "4892",
        "RANGE": "Sentinel Range",
        "LOCATION": "Antarctica",
    },
    {
        "MOUNTAIN": "Puncak Jaya",
        "HEIGHT": "4884",
        "RANGE": "Sudirman Range",
        "LOCATION": "Indonesia",
    },
    {
        "MOUNTAIN": "Mont Blanc",
        "HEIGHT": "4808",
        "RANGE": "Alps",
        "LOCATION": "France, Italy",
    }
]


with open("data\\mountains.csv",'w', newline="") as mountain_file:
    fields = ['MOUNTAIN', 'HEIGHT', 'RANGE', 'LOCATION']

    mountain_writer = csv.DictWriter(mountain_file, fieldnames = fields)
    mountain_writer.writeheader()
    mountain_writer.writerows(mountain_list)
    print("File writing completed")
