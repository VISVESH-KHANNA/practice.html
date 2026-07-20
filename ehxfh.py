import csv

def f1():
    with open("test.csv","w") as db:
        file = csv.writer(db)
        file.writerow(['s_no','produxt',"price"])

        c = 1
        try:
            while True:
                print("enter teh upcoming fields")
                print("\n \n \n \n \n \n \n  \n \n")
                d1 = c
                c+=1
                name = input("enter your name: ")
                price = float(input("enter teh price: "))
                rec = [d1,name,price]
                file.writerow(rec)

        except :
            print("OOPS made mistake while entering input")
            d1 = c
            c+=1
            name = input("enter your name: ")
            price = float(input("enter teh price: "))
            rec = [d1,name,price]
            file.writerow(rec)

        finally:
            print("thanks for using")
            def f2():
                with open("test.csv","r") as db:
                    file = csv.writer(db)
                    

                    for i in file:
                        print(i)