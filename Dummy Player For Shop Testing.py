#Dummy Player for shop testing


class Player():
    def __init(self,items,name):
        self.name=name
        self.items=items
        self.money=100
class items():
    def __init__(self,items,name):
        self.name=name
        self.Price=Price
    def ShopHomeBase():
        print("Info")
        choice=input("Would you like to buy or sell items? ")
        if choice in("buy","b","Buy"):
            BuyItems()
        elif choice in("sell","s","Sell"):
            SellItems()
        else:
            secChoice=input("Would you like to exit(Y/N)")
            if secChoice=="y":
                exitloop
