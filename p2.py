import csv
with open('example.csv',mode='w',newline='')as file:
    writer = csv.writer(file)
    writer.writerow(['same','age','occupation'])
    data=[
        ['NAME','AGE','COUNTRY'],
        ["JOHN",23,"USA"],
        ["nirav",20,"INDIA"]
        ]
    writer.writerows(data)
