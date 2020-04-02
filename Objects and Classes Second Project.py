class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "The name of the menu is {} and the time it is available is between {} and {}.".format(self.name,
                                                                                                      self.start_time,
                                                                                                      self.end_time)

    def calculate_bill(self, purchased_items):
        my_sum = 0
        for item in purchased_items:
            my_sum += self.items[item]
        return my_sum


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "Store is based at {}.\n".format(self.address)

    def available_menus(self, time):
        avail_menu = []
        for menu in self.menus:
            if (time >= menu.start_time) and (time <= menu.end_time):
                avail_menu.append(menu.items)
        return avail_menu


class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


brunch_list = {'pancakes': 7.50,
               'waffles': 9.00,
               'burger': 11.00,
               'homefries': 4.50,
               'coffee': 1.50,
               'espreso': 3.00,
               'tea': 1.00,
               'mimosa': 10.50,
               'orange juice': 3.50}
brunch = Menu("Brunch", brunch_list, 11.00, 16.00)

early_bird_list = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                   'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
                   'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu('Early bird dinning', early_bird_list, 15.00, 18.00)

dinner_list = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("Dinner", dinner_list, 17.00, 23.00)

kids_list = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu("Kids' menu", kids_list, 11.00, 21.00)

print(kids, "\n\n")

print("The order for pancakes, homefries and coffee costs: ")
print("\t", brunch.calculate_bill(['pancakes', 'homefries', 'coffee']), "\n\n")

print("The order for salumeria plate and the vegan mushroom ravioli costs: ")

print("\t", early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

menu = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menu)

new_installment = Franchise("12 East Mulberry Street", menu)

print(flagship_store.available_menus(17), "\n")

my_business = Business("Basta Fazoolin", [flagship_store, new_installment])

arepas_list = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Arepas menu", arepas_list, 10, 20.00)

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

my_new_business = Business("Take a 'Arepa", arepas_place)








