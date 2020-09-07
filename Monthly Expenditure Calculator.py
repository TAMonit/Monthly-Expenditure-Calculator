from tkinter import *
print('               Mothly Expenditure               ')


#taking individual prices
print("\n")

while True:
   try:
      print('Electricity bill')
      electricitybill = int(input())

      print('Groceries(daily consumables eg. milk, vegetables, fruits)')
      groceries = int(input())

      print('Clothes')
      clothes = int(input())

      print('Rent')
      rent = int(input())

      print('House Maintainance')
      housemaintainance = int(input())
      break
   except ValueError:
      print('Invalid Entry')

top = Tk()
top.geometry("200x100")
b = Button(top,text = "Simple")
b.pack()


