from flat import Bill, Flatmate
from reports import PdfReport

amount=float(input("Hey user, enter the bill amount: "))
period=input("What is bill period? E.g.March 2021: ")

name1=input("What is your name: ")
days_in_house1=int(input(f"How many days did {name1} stay in the house: "))

name2=input("What is the name of your flatmate?")
days_in_house2=int(input(f"How many days did {name2} stay in the house: "))

the_bill = Bill(amount, period)
person1 = Flatmate(name1, days_in_house1)
person2 = Flatmate(name2, days_in_house2)

print(f"{person1.name} pays", person1.pays(bill=the_bill, flatmate2=person2))
print(f"{person2.name} pays", person2.pays(bill=the_bill, flatmate2=person1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")

pdf_report.generate(person1, person2, the_bill)