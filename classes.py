# Necessary classes
class marketplace:

    def __init__(self, name = "MY_MARKETPLACE"):
        self.name = name
        self.shops = []
        self.traders = []
    
    def number_of_shops(self):
        return len(self.shops)    

    def number_of_traders(self):
        return len(self.traders)

    def list_of_shops(self):
        shops_string = ''
        for shop in self.shops:
            shops_string += f'{shop.name} {shop.owner}\n'
        return shops_string

    def list_of_traders(self):
        traders_string = ''
        for trader in self.traders:
            traders_string += f'{trader.name}\n'

        return traders_string

    def add_shop(self, name, owner):
        self.shops.append(shop(owner, name))
        for trader in self.traders:
            if trader.name == owner:
                trader.add_shop(name)
                print('added to trader')
                print(trader.shops)
        print('added shop')

    def add_trader(self, name):
        self.traders.append(trader(name))
        print('added trader')

    def list_of_shops_of_a_trader(self, name):
        for trader in self.traders:
            if trader.name == name:
                return trader.list_of_shops()

    def list_of_items_of_a_shop(self, name):
        for shop in self.shops:
            if shop.name == name:
                return shop.list_of_items()

    def add_item(self, shop_name, name, price):
        for shop in self.shops:
            if shop.name == shop_name:
                shop.add_item(name, price)

    def change_owner(self, shop_name, owner):
        for shop in self.shops:
            if shop.name == shop_name:
                for trader in self.traders:
                    if trader.name == shop.owner:
                        trader.remove_shop(shop.name)
                    if trader.name == owner:
                        trader.add_shop(shop.name)
                shop.owner = owner

    def assign_money(self, name, money):
        for trader in self.traders:
            if trader.name == name:
                trader.account = money

class shop:
    
    def __init__(self, owner, name = "MY_SHOP"):
        self.name = name
        self.owner = owner
        self.items = []

    def list_of_items(self):
        return self.items
    
    def number_of_items(self):
        return len(self.number_of_items)

    def add_item(self, name, price):
        self.items.append(item(name, price))

    def list_of_items(self):
        items = ''
        for item in self.items:
            items += item.name + ' ' + item.price + '\n'
        return items




class item:

    def __init__(self, name, price):
        self.name = name
        self.price = price




class trader:

    def __init__(self, name):
        self.name = name
        self.shops = []
        self.account = 0

    def add_shop(self, name):
        self.shops.append(name)

    def list_of_shops(self):
        shops_string = ''
        for shop in self.shops:
            shops_string += f'{shop}\n'
        return shops_string

    def remove_shop(self, name):
        self.shops.remove(name)
