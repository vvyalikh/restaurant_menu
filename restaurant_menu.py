#make a menu

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  #function to print out menu availability
  def __repr__(self):
    return self.name + " menu is available from "+ self.start_time + " to " + self.end_time

  #function to calculate bill
  def calculate_bill(self, purchased_items):
    bill = 0
    for items in purchased_items:
      if items in self.items:
        bill = bill + self.items[items]
    return bill


#menu
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
menu1 = Menu("brunch", brunch_items, "11am", "4pm",)

#print out bill from brunch menu
print(menu1.calculate_bill(['pancakes','home fries','coffee']))

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

menu2 = Menu("early bird", early_bird_items , "3pm", "6pm")

#print out bill from early-bird menu
print(menu2.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

menu3 = Menu("dinner", dinner_items, "5pm", "11pm")

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

menu4 = Menu("kids", kids_items, "11am", "9pm" )

#print out menu availability
print(menu1)
print(menu2)
print(menu3)
print(menu4)


