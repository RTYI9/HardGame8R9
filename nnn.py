import os
import time
os.system("clear")

kill = "\033[0;32m"

b = "\033[0;34m"

r = "\033[0;31m"


from random import randint

print("Hello")
o ='y'
while o =="y":

    choice=int(input("\n\n\t\tEnter Number(0-10) 》: "))


    x=randint(0,10)
    if choice==x:
        time.sleep(2)
        print("" +kill)
        print(" _          __  _   __   _   __   _   _____   _____  ")
        print("| |        / / | | |  \ | | |  \ | | | ____| |  _  \ ")
        print("| |  __   / /  | | |   \| | |   \| | | |__   | |_| |  ")
        print("| | /  | / /   | | | |\   | | |\   | |  __|  |  _  /  ")
        print("| |/   |/ /    | | | | \  | | | \  | | |___  | | \ \  ")
        print("|___/|___/     |_| |_|  \_| |_|  \_| |_____| |_|  \_\ ")
        time.sleep(2)
        print ("" +b)
        print ("↓")
        print ("↓")
        print ("↓")
        print ("" +kill)
        print (x)
        print ("" +b)
        print ("↑")
        print ("↑")
        print ("↑")
    else:


        print("" +b)
        time.sleep(2)
        print("" +r)
        print(" _       _____   _____   _____   _____   _____  ")
        print("| |     /  _  \ /  ___/ /  ___/ | ____| |  _  \ ")
        print("| |     | | | | | |___  | |___  | |__   | |_| | ")
        print("| |     | | | | \___  \ \___  \ |  __|  |  _  /  ")
        print("| |___  | |_| |  ___| |  ___| | | |___  | | \ \  ")
        print("|_____| \_____/ /_____/ /_____/ |_____| |_|  \_\ ")
        time.sleep(2)
        print("" +b)
        print("↓")
        print("↓")
        print("↓")
        print( "" +kill)
        print(x)
        print("" +b)
        print("↑")
        print("↑")
        print("↑")
        time.sleep(2)
        o = input("\t\t \n\nReplay? y/n 》 : ")



                   
