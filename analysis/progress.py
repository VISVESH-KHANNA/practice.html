import csv

def f1():
    with open("xcel.csv","a+",newline="") as db:

        def f2():
            file = csv.DictWriter(db,fieldnames= ["no","marks secured","total marks"])

            file.writeheader()
            no1 = 0
            while True:
                no1 +=1
                no = no1
                marks_secured = int(input("enter teh marks secured: "))
                total_marks = int(input("enter teh total marks: "))

                rec = {
                    "no" : no,
                    "marks secured" : marks_secured,
                    "total marks" : total_marks
                }

                file.writerow(rec)
                db.flush()


                if input("press 'x' to exit : ").lower() == "x":
                    break

        
        
        def f3():
            db.seek(0)
            file = csv.DictReader(db)

            for i in file:
                print(i)


        print("select teh option to continue teh execution: \n [1]=write \n [2]=read")

        a = int(input("enter teh choice: "))
        if  a == 1:
            f2()

        elif a == 2:
            f3()

        else:
            print("not valid.")

f1()