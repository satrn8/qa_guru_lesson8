import csv

# with open(".\\resources\\username.csv") as f:
#     reader = csv.reader(f)
#     for i in reader:
#         print(i)

f = csv.DictReader(".\\resources\\username.csv", "r")
print(f.reader)