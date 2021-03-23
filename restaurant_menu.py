#make a menu

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  #function to print out menu availability
  def __repr__(self):
    return self.name + " menu is available from "+ str(self.start_time) + " to " + str(self.end_time)

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
menu1 = Menu("brunch", brunch_items, 1100, 1600,)

#print out bill from brunch menu
print(menu1.calculate_bill(['pancakes','home fries','coffee']))

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

menu2 = Menu("early bird", early_bird_items , 1500, 1800)

#print out bill from early-bird menu
print(menu2.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

menu3 = Menu("dinner", dinner_items, 1700, 2300)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

menu4 = Menu("kids", kids_items, 1100, 2100 )

#print out menu availability
print(menu1)
print(menu2)
print(menu3)
print(menu4)

#create the franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "The address of our new restaurant is " + self.address

#function define available menus depending on day time
  def available_menus(self,time):
    available_menu_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu_list.append(menu)
    return available_menu_list

menus = [menu1, menu2, menu3, menu4]

flagship_store = Franchise("1232 West End Road", menus)

print(flagship_store)

new_installment = Franchise("12 East Mulberry Street", menus)

print(flagship_store.available_menus(1700)) 

#create business chain

class Business:
   def __init__(self, name, franchises):
     self.name = name
     self.franchises = franchises

arepas_menu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
menu5 = Menu("Take a’ Arepa", arepas_menu, 1000, 2000 )

arepas_place = Franchise("189 Fitzgerald Avenue", [menu5])

arepa = Business("Basta Fazoolin' with my Heart", [arepas_place])

print(arepas_place)
print(arepa.franchises[0])
print(menu5)
print(arepas_place.available_menus(1200))

print(menu5.calculate_bill(['arepa pabellon', 'guayanes arepa']))
