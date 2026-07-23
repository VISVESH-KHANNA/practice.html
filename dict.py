print("updating a file in dict")

import csv 
 

def f1():
    with open("dict.csv","w+",newline = "") as db:
        file = csv.DictWriter(db,fieldnames=["key","values"])

        file.writeheader()

        while True:
        
            key = input("Enter key: ")
            value = input("Enter value: ")

            file.writerow({
                "key": key,
                "values": value
            })

            db.flush()

            if input("Press x to exit: ").lower() == "x":
                break

        if input("press y to read") == "y":
            db.seek(0)
            file_reader = csv.DictReader(db)

            for i in file_reader:
                print(i)

#fn call
f1()