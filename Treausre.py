#! /usr/bin/python3
# Program Name: Treasure.p
# Author: Thomas Morrissey, Jacob Snipes, Luke Gosnell, Bryson Mueller
# Date Written:3-9-2015
# Psuodecode:
#   3-10-2015
#   The Basic money name is money. We choose this name just because it is generic and easily changable. Four basic types of money is Copper, Silver, Gold, and Platinum.
#   We decide to follow the SRD:Treasure website and the website's web address is at http://www.dandwiki.com/wiki/SRD:Treasure.
#   3-12-2015
#   Thomas worte MainFunctions and Level REwards for levels #1-8, Luke wrote Level Rewards for 9-15, and Jacob wrote Level Rewards for 16-20.
#   Due to Bryson's absence for the 12th and the 11th he was unable to write any part of the code.
import random
def LevelOneReward(money):
        RanNum=random.randint(00,101)
        if RanNum > 0 and RanNum < 15:
            print("You get nothing!")
        elif RanNum > 14 and RanNum < 30:
            Amount = random.randint(00,7)
            print("You got ", Amount, "copper piece(s)!")
            money = money + (Amount * 1000)
        elif RanNum > 29 and RanNum < 53:
            Amount = random.randint(00,9)
            print("You got ", Amount, "silver piece(s)!")
            money = money + (Amount * 1000)
        elif RanNum > 52 and RanNum < 96:
            Amount = random.randint(00,16)
            print("You got ", Amount, "gold piece(s)!")
            money = money + (Amount * 1000)
        elif RanNum > 95 and RanNum < 101:
            Amount = random.randint(00,5)
            print("You got ", Amount, "platinum piece(s)!")
            money = money + (Amount * 10000)
        return money
def LevelTwoReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 00 and RanNum < 14:
            print("You got nothing.")
        elif RanNum > 13 and RanNum < 24:
            Amount = random.randint(1,11)
            print("you got",Amount,"copper pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 23 and RanNum < 44:
            Amount = random.randint(1,21)
            print("you got",Amount,"silver pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 43 and RanNum < 96:
            Amount = random.randint(1,5)
            print("you got",Amount,"gold pieces!")
            Money=Money+(Amount*10000)
        elif RanNum > 95 and RanNum < 101:
            Amount = random.randint(0,11)
            print("you got",Amount,"platinum pieces!")
            Money=Money+(Amount*10000)
        return Money
    
def LevelThreeReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 00 and RanNum < 12:
            print("You got nothing.")
        elif RanNum > 11 and RanNum < 22:
            Amount = random.randint(0,11)
            print("you got",(Amount * 1000),"copper pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 21 and RanNum < 42:
            Amount = random.randint(1,21)
            print("you got",Amount,"silver pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 41 and RanNum < 96:
            Amount = random.randint(0,5)
            print("you got",Amount,"gold pieces!")
            Money=Money+(Amount*10000)
        elif RanNum > 95 and RanNum < 101:
            Amount = random.randint(0,11)
            print("you got",Amount,"platinum pieces!")
            Money=Money+(Amount*10000)
        return Money
    
def LevelFourReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 00 and RanNum < 12:
            print("You got nothing.")
        elif RanNum > 11 and RanNum < 22:
            Amount = random.randint(2,31)
            print("you got",(Amount * 10000),"copper pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 21 and RanNum < 42:
            Amount = random.randint(1,21)
            print("you got",Amount,"silver pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 41 and RanNum < 96:
            Amount = random.randint(0,5)
            print("you got",Amount,"gold pieces!")
            Money=Money+(Amount*10000)
        elif RanNum > 95 and RanNum < 101:
            Amount = random.randint(0,11)
            print("you got",Amount,"platinum pieces!")
            Money=Money+(Amount*10000)
        return Money
def LevelFiveReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 1 and RanNum < 11:
            print("You got nothing.")
        elif RanNum > 10 and RanNum < 20:
            Amount = random.randint(0,5)
            print("you got",(10000*Amount),"copper pieces!")
            Money=Money+(Amount*10000)
        elif RanNum > 19 and RanNum < 39:
            Amount = random.randint(0,7)
            print("you got",(Amount*10000),"silver pieces!")
            Money=Money+(Amount*10000)
        elif RanNum > 38 and RanNum < 96:
            Amount = random.randint(0,9)
            print("you got",Amount,"gold pieces!")
            Money=Money+(Amount*10000)
        elif RanNum > 95 and RanNum < 101:
            Amount = random.randint(0,11)
            print("you got",Amount,"platinum pieces!")
            Money=Money+(Amount*10000)
        return Money
def LevelSixReward(money):
        RanNum=random.randint(00,101)
        if RanNum > 0 and RanNum < 11:
            print("You get nothing!")
        elif RanNum > 10 and RanNum < 19:
            Amount = random.randint(00,7)
            Amount = Amount * 10000
            print("You get",Amount,"copper coins.")
            money = money + Amount
        elif RanNum > 18 and RanNum < 38:
            Amount = random.randint(0,9)
            Amount = Amount * 1000
            print("You got",Amount,"silver pieces!")
            money=money+(Amount*10)
        elif RanNum > 37 and RanNum < 96:
            Amount = random.randint(0,11)
            Amount=Amount*100
            print("you got",Amount,"gold pieces.")
            money=money+(Amount*100)
        else:
            Amount=random.randint(1,13)
            Amount=Amount*10
            print("You got",Amount,"Platinum pieces.")
        return money
def LevelSevenReward(money):
        RanNum=random.randint(0,101)
        if RanNum > 0 and RanNum < 12:
            print("You get Nothing!")
        elif RanNum > 11 and RanNum < 19:
            amount=random.randint(0,11)
            amount = amount * 10000
            print ("You get",amount,"copper pieces!")
            money=money+amount
        elif RanNum > 18 and RanNum < 36:
            amount=random.randint(0,13)
            amount = amount * 1000
            print("You got",amount,"silver pieces.")
            money=money+(amount*10)
        elif RanNum > 35 and RanNum < 94:
            amount = random.randint(1,13)
            amount = amount * 100
            print("You got",amount,"Gold pieces!")
            money=money+(amount*100)
        else:
            amount=random.randint(2,13)
            amount = amount * 10
            print("You got",amount,"Platinum pieces!")
        return money
def LevelEightReward(money):
       RanNum=random.randint(0,101)
       if RanNum > 0 and RanNum < 11:
           print("You got nothing!")
       elif RanNum > 10 and RanNum < 16:
            amount = random.randint(1,13)
            amount=amount*10000
            print("You got",amount,"copper pieces!")
            money=money+amount
       elif RanNum > 15 and RanNum < 30:
           amount=random.randint(1,13)
           amount=amount*1000
           print("You got",amount,"Silver pieces!")
           money=money+(amount*10)
       elif RanNum > 29 and RanNum < 88:
            amount=random.randint(1,17)
            amount=amount*100
            print("You got",amount,"Gold pieces!")
            money=money+(amount*100)
       else:
            amount=random.randint(2,19)
            amount=amount*10
            print("You got",amount,"Platinum pieces!")
            money=money+(amount*1000)
       return money
    
def LevelNineReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 00 and RanNum < 11:
            print("You got nothing.")
        elif RanNum > 10 and RanNum < 16:
            Amount = random.randint(1,13)
            print("you got",(Amount*10000),"copper pieces!")
            Money=Money+(Amount*10000)
        elif RanNum > 15 and RanNum < 30:
            Amount = random.randint(2,17)
            print("you got",(Amount*1000),"silver pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 29 and RanNum < 88:
            Amount = random.randint(4,21)
            print("you got",(Amount*100),"gold pieces!")
            Money=Money+(Amount*100)
        elif RanNum > 85 and RanNum < 101:
            Amount = random.randint(1,25)
            print("you got",(Amount*10),"platinum pieces!")
            Money=Money+(Amount*10)
        return Money

def LevelTenReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 00 and RanNum < 11:
            print("You got nothing.")
        elif RanNum > 10 and RanNum < 25:
            Amount = random.randint(1,21)
            print("you got",(Amount*1000),"copper pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 24 and RanNum < 80:
            Amount = random.randint(5,25)
            print("you got",(Amount*1000),"silver pieces!")
            Money=Money+(Amount*100)
        elif RanNum > 79 and RanNum < 101:
            Amount = random.randint(4,31)
            print("you got",(Amount*10),"gold pieces!")
            Money=Money+(Amount*10)
        return Money
def LevelElevenReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 0 and RanNum < 9:
            print("You got nothing.")
        elif RanNum > 8 and RanNum < 15:
            Amount = random.randint(2,31)
            print("you got",(Amount*1000),"copper pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 14 and RanNum < 76:
            Amount = random.randint(3,33)
            print("you got",(Amount*100),"gold pieces!")
            Money=Money+(Amount*100)
        elif RanNum > 75 and RanNum < 101:
            Amount = random.randint(3,41)
            print("you got",(Amount*10),"platinum pieces!")
            Money=Money+(Amount*10)
        return Money
def LevelTwelveReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 00 and RanNum < 9:
            print("You got nothing.")
        elif RanNum > 8 and RanNum < 15:
            Amount = random.randint(2,37)
            print("you got",(Amount*1000),"copper pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 14 and RanNum < 76:
            Amount = random.randint(0,6)
            print("you got",(Amount*1000),"silver pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 75 and RanNum < 101:
            Amount = random.randint(0,5)
            print("you got",(Amount*100),"gold pieces!")
            Money=Money+(Amount*100)
        return Money
def LevelThirteenReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 0 and RanNum < 9:
            print("You got nothing.")
        elif RanNum > 8 and RanNum < 76:
            Amount = random.randint(0,5)
            print("you got",(Amount*1000),"copper pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 75 and RanNum < 101:
            Amount = random.randint(0,11)
            print("you got",(Amount*100),"silver pieces!")
            Money=Money+(Amount*100)
        return Money

        
def LevelFourteenReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 0 and RanNum < 9:
            print("You got nothing.")
        elif RanNum > 8 and RanNum < 76:
            Amount = random.randint(0,7)
            print("you got",(Amount*1000),"copper pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 75 and RanNum < 101:
            Amount = random.randint(0,13)
            print("you got",(Amount*100),"silver pieces!")
            Money=Money+(Amount*100)
        return Money
def LevelFifteenReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 0 and RanNum < 4:
            print("You got nothing.")
        elif RanNum > 3 and RanNum < 75:
            Amount = random.randint(0,9)
            print("you got",(Amount*1000),"copper pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 74 and RanNum < 101:
            Amount = random.randint(2,13)
            print("you got",(Amount*100),"silver pieces!")
            Money=Money+(Amount*100)
        return Money
def LevelSixteenReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 0 and RanNum < 4:
            print("You got nothing.")
        elif RanNum > 3 and RanNum < 75:
            Amount = random.randint(0,5)
            print("you got",(Amount*1000),"gold pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 74 and RanNum < 101:
            Amount = random.randint(0,11)
            print("you got",(Amount*100),"platinum pieces!")
            Money=Money+(Amount*100)
        return Money
#Level 17
def LevelSeventeenReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 0 and RanNum < 4:
            print("You got nothing.")
        elif RanNum > 3 and RanNum < 69:
            Amount = random.randint(0,5)
            print("you got",(Amount*1000),"gold pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 68 and RanNum < 101:
            Amount = random.randint(0,11)
            print("you got",(Amount*100),"platinum pieces!")
            Money=Money+(Amount*100)
        return Money
#Level 18
def LevelEighteenReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 0 and RanNum < 3:
            print("You got nothing.")
        elif RanNum > 2 and RanNum < 66:
            Amount = random.randint(0,5)
            print("you got",(Amount*1000),"gold pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 65 and RanNum < 101:
            Amount = random.randint(0,11)
            print("you got",(Amount*100),"platinum pieces!")
            Money=Money+(Amount*100)
        return Money
#Level 19
def LevelNineteenReward(Money):
            RanNum=random.randint(1,101)
            if RanNum > 0 and RanNum < 3:
                print("You got nothing.")
            elif RanNum > 2 and RanNum < 66:
                Amount = random.randint(0,5)
                print("you got",(Amount*1000),"gold pieces!")
                Money=Money+(Amount*1000)
            elif RanNum > 65 and RanNum < 101:
                Amount = random.randint(0,11)
                print("you got",(Amount*100),"platinum pieces!")
                Money=Money+(Amount*100)
            return Money
#Level 20
def LevelTwentyReward(Money):
        RanNum=random.randint(1,101)
        if RanNum > 0 and RanNum < 3:
            print("You got nothing.")
        elif RanNum > 2 and RanNum < 66:
            Amount = random.randint(0,5)
            print("you got",(Amount*1000),"gold pieces!")
            Money=Money+(Amount*1000)
        elif RanNum > 65 and RanNum < 101:
            Amount = random.randint(0,11)
            print("you got",(Amount*100),"platinum pieces!")
            Money=Money+(Amount*100)
        return Money
def MainFunction(MonLevel,Money):
    print(MonLevel)
    if MonLevel == 1:
            Money=LevelOneReward(Money)
    elif MonLevel == 2 :
            Money=LevelTwoReward(Money)
    elif MonLevel == 3:
            Money=LevelThreeReward(Money)
    elif MonLevel == 4:
            Money=LevelFourReward(Money)
    elif MonLevel == 5:
            Money=LevelFiveReward(Money)
    elif MonLevel == 6:
            Money=LevelSixReward(Money)
    elif MonLevel == 7:
            Money=LevelSevenReward(Money)
    elif MonLevel == 8:
            Money=LevelEightReward(Money)
    elif MonLevel == 9:
            Money=LevelNineReward(Money)
    elif MonLevel == 10:
            Money=LevelTenReward(Money)
    elif MonLevel == 11:
            Money=LevelElevenReward(Money)
    elif MonLevel == 12:
            Money=LevelTwelveReward(Money)
    elif MonLevel == 13:
            Money=LevelThirteenReward(Money)
    elif MonLevel == 14:
            Money=LevelFourteenReward(Money)
    elif MonLevel == 15:
            Money=LevelFifteenReward(Money)
    elif MonLevel == 16:
            Money=LevelSixteenReward(Money)
    elif MonLevel == 17:
            Money=LevelSeventeenReward(Money)
    elif MonLevel == 18:
            Money=LevelEighteenReward(Money)
    elif MonLevel == 19:
            Money=LevelNineteenReward(Money)
    else:
            Money=LevelTwentyReward(Money)
    print("You have",Money,"cp!")
        

def main():
    for number in range(0,21):
        MonLevel=number
        money=MainFunction(MonLevel,100)
main()
    
