import csv

def f1():
    with open("studdb.csv", "w") as db:
        file = csv.writer(db, delimiter=",")
        file.writerow(["admission", "name", "ROLL NO"])


        while 1:
            d1 = int(input("enter teh admision no.: "))
            d2 = input("enetr your name: ")
            d3 = int(input("enter your roll nFo.: "))

            rec = [d1,d2,d3]
            file.writerow(rec)

            if input("press 'x'to exit or other key to continue:").lower() == "x":
                break

    print("File creation successful")

f1()    