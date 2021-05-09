import random

item_list = ["Blender","Oven","Kettle","Television","Refrigerator"]
bought_list = []
budget = [50,100,150,200,250]
user_budget = 0

def show_available():
    print("--- Available Items ---\n")
    for i in item_list:
        print("- {}".format(i))
        
def add_remove_cart():
    rndm_budget = random.choice(budget)
    global user_budget
    user_budget = rndm_budget
    
    determiner = "y"
    while(determiner =="y"):
        print("Chose Items to buy:\n")
        print("1- Blender (5$)\n2- Oven (10$)\n3- Kettle (15$)\n4- Television (20$)\n5- Refrigerator (25$)\n6- Return items\n7- Main menu")
        choice = input("\nEnter your selection: ")

        if (int(choice) == 1):
            if (user_budget>=5):
                user_budget = user_budget-5
                bought_list.append("Blender")
                print("\nAdded Blender to the List\n")
                print("--- Your Cart List ---")
                for i in bought_list:
                    print("- {}".format(i))
                print("\nRemaining balance: {}".format(user_budget))
            else:
                print("\nNOTE: Cant buy this item!")
                print("REASON: Low balance = {}\n".format(user_budget))
                
        elif (int(choice) == 2):
            if (user_budget>=10):
                user_budget = user_budget-10
                bought_list.append("Oven")
                print("\nAdded Oven to the List\n")
                print("--- Your Cart List ---")
                for i in bought_list:
                    print("- {}".format(i))
                print("\nReamining balance: {}".format(user_budget))
            else:
                print("\nNOTE: Cant buy this item!")
                print("REASON: Low balance = {}\n".format(user_budget))
        
        elif (int(choice) == 3):
            if (user_budget>=15):
                user_budget = user_budget-15
                bought_list.append("Kettle")
                print("\nAdded Kettle to the List\n")
                print("--- Your Cart List ---")
                for i in bought_list:
                    print("- {}".format(i))
                print("\nReamining balance: {}".format(user_budget))
            else:
                print("\nNOTE: Cant buy this item!")
                print("REASON: Low balance = {}\n".format(user_budget))
        
        elif (int(choice) == 4):
            if (user_budget>=20):
                user_budget = user_budget-20
                bought_list.append("Television")
                print("\nAdded Television to the List\n")
                print("--- Your Cart List ---")
                for i in bought_list:
                    print("- {}".format(i))
                print("\nReamining balance: {}".format(user_budget))
            else:
                print("\nNOTE: Cant buy this item!")
                print("REASON: Low balance = {}\n".format(user_budget))
        
        elif (int(choice) == 5):
            if (user_budget>=25):
                user_budget = user_budget-25
                bought_list.append("Refrigerator")
                print("\nAdded Refrigerator to the List\n")
                print("--- Your Cart List ---")
                for i in bought_list:
                    print("- {}".format(i))
                print("\nReamining balance: {}".format(user_budget))
            else:
                print("\nNOTE: Cant buy this item!")
                print("REASON: Low balance = {}\n".format(user_budget))
        
        elif (int(choice) == 6):
            while(True):
                print("Which Item you want to return:\n")
                print("1- Blender (5$)\n2- Oven (10$)\n3- Kettle (15$)\n4- Television (20$)\n5- Refrigerator (25$)\n6- Main Menu")
                choice3 = input("\nEnter your selection: ")
                
                if (int(choice3) == 1):
                    if "Blender" in bought_list:
                        user_budget = user_budget+5
                        bought_list.remove("Blender")
                        print("Removed a Blender")
                    else:
                        print("Item is not in the cart!")

                elif (int(choice3) == 2):
                    if "Oven" in bought_list:
                        user_budget = user_budget+10
                        bought_list.remove("Oven")
                        print("Removed an Oven")
                    else:
                        print("Item is not in the cart!")

                elif (int(choice3) == 3):
                    if "Kettle" in bought_list:
                        user_budget = user_budget+15
                        bought_list.remove("Kettle")
                        print("Removed a Kettle")
                    else:
                        print("Item is not in the cart!")

                elif (int(choice3) == 4):
                    if "Television" in bought_list:
                        user_budget = user_budget+20
                        bought_list.remove("Television")
                        print("Removed a Television")
                    else:
                        print("Item is not in the cart!")

                elif (int(choice3) == 5):
                    if "Refrigerator" in bought_list:
                        user_budget = user_budget+25
                        bought_list.remove("Refrigerator")
                        print("Removed a Refrigerator")
                    else:
                        print("Item is not in the cart!")
                elif (int(choice3) == 6):
                    main_menu()
                    determiner = "n"
                    break
                else:
                    print("Invalid selection")
        
        elif (int(choice) == 7):
            main_menu()
            break
            
        else:
            print("Kindly, make a valid selection!")

def cart_list():
    print("--- Your Cart List ---")
    for i in bought_list:
        print("- {}".format(i))
            
def main_menu():
    while(True):
        print("\n--- MAIN MENU: Select your action ---")
        print("1- Show available items\n2- Buy/Remove items\n3- Show current cart list\n4- Exit shop")
        choice2 = input("\nEnter your selection: ")
        
        if (int(choice2)==1):
            show_available()
        elif (int(choice2)==2):
            add_remove_cart()
            break
        elif (int(choice2)==3):
            cart_list()
        elif (int(choice2)==4):
            print("Exited")
            break
        else:
            print("Kindly, make a valid selection!")
    
main_menu()