# Dummy Player for shop testing
# Code made by Thomas Morrissey, Jacob Snipes, Luke Gosnell, and Bryson Mueller.
# Pseudocode:
#   Shop program. You can buy/sell items here.
#   Thanks to the Inventory team to giving us the Inventory Items we can now complete the program.
# Modified by Jacob Snipes to import the Inventory program and take the items from there.
import Inventory

class item(object):
    def __init__(self,cost,name):
        self.name=name
        self.cost=cost
    def __str__(self):
        print("n\Cost:",self.cost)

class Player(object):
    def __init__(self,name):
        self.name=name
        self.items=[]
        self.money=200
        
    def SellItems(self):
        Continue=""
        while Continue != "n":
            print("Money:",self.money)
            for item in self.items:
                print(item.name,":",item.cost/2)
            Selection=input("Which item would you like to sell: ")
            sellItem=[]
            sellItem2=[]
            for i in self.items:
                sellItem.append(i.name)
                sellItem2.append(i.cost)
            count=0
            missell=True
            for i in sellItem:
                if Selection == i:
                    self.money += sellItem2[count]/2
                    
                    self.items.remove(self.items[count])
                    print("Inventory:")
                    missell=False
                    for item in self.items:
                        print(item.name,":",item.cost)
                
                else:
                    count+=1
                    
            if missell==True:
                print("Please enter a valid item")
            Continue=input("Would you like to sell more? (y/n): ")
            

    def BuyItems(self):
        Continue=""
        
   
        while Continue not in ("no","No","n","N"):
            print("Money:",self.money)
            Inventory.Print()
            Selection=input("Which item would you like to buy: ")
            if Selection in Inventory.myInventory.weapons:
                item=Inventory.myInventory.weapons[Selection]
                print("Success")
                if item.cost > self.money:
                    print("You don't have enough cash!")
                else:
                    self.money -= item.cost
                    self.items.append(item)
            elif Selection in Inventory.myInventory.items:
                item=Inventory.myInventory.items[Selection]
                if item.cost > self.money:
                    print("You don't have enough cash!")
                else:
                    self.money -= item.cost
                    self.items.append(item)
            elif Selection in Inventory.myInventory.consumables:
                item=Inventory.myInventory.consumables[Selection]
                if item.cost > self.money:
                    print("You don't have enough cash!")
                else:
                    self.money -= item.cost
                    self.items.append(item)
            elif Selection in Inventory.myInventory.armors:
                item=Inventory.myInventory.armors[Selection]
                if item.cost > self.money:
                    print("You don't have enough cash!")
                else:
                    self.money -= item.cost
                    self.items.append(item)
            else:
                print("That's not an item,",self.name)
            print("Money left:",self.money)
            Continue=input("Would you like to buy more? (y/n): ")
        return self.items

def NewShopHomeBase():
    choice=""
    name=input("Enter name: ")
    player = Player(name)
    print("Info")
    while choice not in ("N","No","no","n"):
        choice=input("Would you like to buy or sell items? (B/S) or would you like to exit?(N): ")
        if choice in("buy","b","Buy", "B"):
            player.BuyItems()
        elif choice in("sell","s","Sell", "S"):
            player.SellItems()
        
NewShopHomeBase()
