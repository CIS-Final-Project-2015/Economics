# Dummy Player for shop testing
# Code made by Thomas Morrissey, Jacob Snipes, Luke Gosnell, and Bryson Mueller.
# Pseudocode:
# Shop program. You can buy/sell items here.
# The program is incomplete because the inventory team is not finished with the items/item values.

class item(object):
    def __init__(self,price,name):
        self.name=name
        self.price=price

class Player(object):
    def __init__(self,name):
        self.name=name
        Item=item(50,"Sword")
        self.items=[]
        self.items.append(Item)
        self.money=100
        
    def SellItems(self):
        Continue=""
        while Continue != "n":
            print("Money:",self.money)
            for item in self.items:
                print(item.name,":",item.price)
            Selcetion=input("Which item would you like to sell? ")
            self.money += item.price
            self.items.remove(item)
            print("Current Cash:",self.money)
            Continue=input("Would you like to sell more?(y/n)")

    def BuyItems(self,BuyItemsList ):
        Continue=""
        
   
        while Continue != "n":
            print("Money:",self.money)
            print(BuyItemsList.keys())
            Selection=input("Which item would youlike to buy?")
            item=BuyItemsList[Selection]
            self.items.append(item)
            self.money -= item.price
            print("Money left:",self.money)
            Continue=input("Would you like to buy more? (y/n)")

        
def ShopHomeBase():
    requiredItems = {}
    item1=item(45,"Dagger")
    requiredItems["Dagger"]=item1
    item2=item(75,"Armor")
    requiredItems["Armor"]=item2
    item3=item(35,"Potion")
    requiredItems["Potion"]=item3
    choice=""

    player = Player("Bob Sacks")
    print("Info")
    while choice != "N":
        choice=input("Would you like to buy or sell items? (B/S) or would you like to exit? (N)")
        if choice in("buy","b","Buy", "B"):
            player.BuyItems(requiredItems)
        elif choice in("sell","s","Sell", "S"):
            player.SellItems()
        
        
ShopHomeBase()
