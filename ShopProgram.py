# Dummy Player for shop testing
# Code made by Thomas Morrissey, Jacob Snipes, Luke Gosnell, and Bryson Mueller.
# Pseudocode:
#   Shop program. You can buy/sell items here.
#   Thanks to the Inventory team to giving us the Inventory Items we can now complete the program.

class item(object):
    def __init__(self,price,name):
        self.name=name
        self.price=price
    def __str__(self):
        print("n\Cost:",self.price)

class Player(object):
    def __init__(self,name):
        self.name=name
        Item=item(50,"Sword")
        Item2=item(45,"Sheild")
        self.items=[]
        self.items.append(Item)
        self.items.append(Item2)
        self.money=100
        
    def SellItems(self):
        Continue=""
        while Continue != "n":
            print("Money:",self.money)
            for item in self.items:
                print(item.name,":",item.price)
            Selection=input("Which item would you like to sell: ")
            sellItem=[]
            sellItem2=[]
            for i in self.items:
                sellItem.append(i.name)
                sellItem2.append(i.price)
            count=0
            missell=True
            for i in sellItem:
                if Selection == i:
                    self.money += sellItem2[count]
                    self.items.remove(self.items[count])
                    print("Inventory:")
                    missell=False
                    for item in self.items:
                        print(item.name,":",item.price)
                
                else:
                    count+=1
                    
            if missell==True:
                print("Please enter a valid item")
            Continue=input("Would you like to sell more? (y/n): ")
            

    def BuyItems(self,BuyItemsList1,BuyItemsList2,BuyItemsList3,BuyItemsList4):
        Continue=""
        
   
        while Continue not in ("no","No","n","N"):
            print("Money:",self.money)
            print("Weapons:")
            for Item in BuyItemsList1.keys():
                print("Name:",Item,"Cost:",BuyItemsList1[Item].price)
            print("Food:")
            for Item in BuyItemsList2.keys():
                print("Name:",Item,"Cost:",BuyItemsList2[Item].price)
            print("Goods:")
            for Item in BuyItemsList3.keys():
                print("Name:",Item,"Cost:",BuyItemsList3[Item].price)
            print("Armor:")
            for Item in BuyItemsList4.keys():
                print("Name:",Item,"Cost:",BuyItemsList4[Item].price)
            Selection=input("Which item would you like to buy: ")
            if Selection in BuyItemsList1:
                item=BuyItemsList1[Selection]
                if item.price > self.money:
                    print("You don't have enough cash!")
                else:
                    self.money -= item.price
                    item.price=item.price / 2
                    self.items.append(item)
            elif Selection in BuyItemsList2:
                item=BuyItemsList2[Selection]
                if item.price > self.money:
                    print("You don't have enough cash!")
                else:
                    self.money -= item.price
                    item.price=item.price / 2
                    self.items.append(item)
            elif Selection in BuyItemsList3:
                item=BuyItemsList3[Selection]
                if item.price > self.money:
                    print("You don't have enough cash!")
                else:
                    self.money -= item.price
                    item.price=item.price / 2
                    self.items.append(item)
            elif Selection in BuyItemsList4:
                item=BuyItemsList4[Selection]
                if item.price > self.money:
                    print("You don't have enough cash!")
                else:
                    self.money -= item.price
                    item.price=item.price / 2
                    self.items.append(item)
            else:
                print("That's not an item,",self.name)
            print("Money left:",self.money)
            Continue=input("Would you like to buy more? (y/n): ")
        return self.items

        
def ShopHomeBase():
    WeaponsDict = {}
    Weapons=["Dagger","Sickle","Club","Morning Star","Long Spear", "Spear","Cross Bow","Javelin","Kukri","War Razor","Klar","Terbutje","Scizore","Bec De Corbin","Earth Braker","Lucrene Hammer","Syringa Spear"]
    WeaponsCost=[2,6,1,8,5,2,35,1,8,8,12,20,20,15,40,15,100]
    for weapon in Weapons:
        WeaponIndex=Weapons.index(weapon)
        WeaponName=Weapons[WeaponIndex]
        WeaponCost=WeaponsCost[WeaponIndex]
        Item=item(WeaponCost,WeaponName)
        WeaponsDict[WeaponName]=Item
    FoodDict={}
    FoodNames=["Loaf of Bread","Hunk of Chesse","Common(Picher)","Fine(Bootle)","Chunk of Meat","Good Meal","Common Meal","Poor Meal"]
    FoodsCost=[0.01,0.1,0.2,10,0.3,0.5,0.3,0.1]
    for Food in FoodNames:
        FoodIndex=FoodNames.index(Food)
        FoodName=FoodNames[FoodIndex]
        FoodCost=FoodsCost[FoodIndex]
        Item=item(FoodCost,FoodName)
        FoodDict[FoodName]=Item
    ArmorsDict = {}
    Armors=["Padded Armor","Studded Armor","Scale Mail","Chainmail","Banded Mail","Full-Plate","Light Wool","Heavy Steel"]
    ArmorsCost=[5,25,50,150,250,1500,3,20]
    for armor in Armors:
        ArmorIndex=Armors.index(armor)
        ArmorName=Armors[ArmorIndex]
        ArmorCost=ArmorsCost[ArmorIndex]
        Item=item(ArmorCost,ArmorName)
        ArmorsDict[ArmorName]=Item
    GoodsDict = {}
    Goods=["Backpack","10ft Pole","Crowbar","Grappling Hook","Spade","50ft Rope","Cure Light","Cure Medium","Cure Serious"]
    GoodsCost=[2,.5,2,1,2,1,50,300,750]
    for good in Goods:
        GoodIndex=Goods.index(good)
        GoodName=Goods[GoodIndex]
        GoodCost=GoodsCost[GoodIndex]
        Item=item(GoodCost,GoodName)
        GoodsDict[GoodName]=Item
    choice=""
    name=input("Enter name: ")
    player = Player(name)
    print("Info")
    while choice not in ("N","No","no","n"):
        choice=input("Would you like to buy or sell items? (B/S) or would you like to exit?(N): ")
        if choice in("buy","b","Buy", "B"):
            player.BuyItems(WeaponsDict,FoodDict,GoodsDict,ArmorsDict)
        elif choice in("sell","s","Sell", "S"):
            player.SellItems()
        
        
ShopHomeBase()
