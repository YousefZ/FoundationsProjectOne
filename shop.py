####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

''' signature cupcakes name: '''
signature_names = "desino"

############################# Start Here! ##############################
cupcake_shop_name = "SweetTooth"
signature_flavors = ["red-velvet","molten","organic","sugarfree"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print(30*"-")
    print("Welcome to ", cupcake_shop_name)
    print(30*"-")
    print('\n\n')
    print("We have ", len(menu),"items on our menu :")
    print(30*"-")
    #print("Menu Items Are:", menu)

    num=1
    for item in menu:
        print (num,". ",item,"(",menu[item], "KD)")
        num +=1
    print(30*"-")

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print()
    print(50*"-")
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    print(50*"-")
    # your code goes here!
    
    
    print ('-','\n- ' .join(original_flavors))
    print()




def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print(50*"-")
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    print(50*"-")
    # your code goes here!
    print('-','\n- ' .join(signature_flavors))
    print()
    print(50*"-")


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in menu or order in original_flavors or order in signature_flavors:
        #print("Correct")
        return True
    else : print("Sorry Item not in menu")



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    order_item = 1
    print("What's your order? Type Exit to end your order: ")
    while order_item  != "exit":
        order_item= input()
        if order_item.lower()=="exit":
            break
        if is_valid_order(order_item.lower()) == True:
            #print("CheckedShouldAdd")
            order_list.append(order_item.lower())
   
    # your code goes here!

    #print(*order_list)
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        print("Your order is eligible for credit card payment")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for n in order_list:
        if n in original_flavors:
            total=total+2
        if n in signature_flavors:
            total=total+2.75
        if n in menu:
            total = total+ menu[n]

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("You Ordered a total of", len(order_list), "Items")
    print("Your order is: ")
    # your code goes here!
    id=1
    for m in order_list:
        
        if m in original_flavors:
            print(id,". ",m, "2 KD")
            id=id+1
        if m in signature_flavors:
            print(id,". ",m, "2.75 KD")
            id=id+1
        if m in menu:
            print(id,". ",m, menu[m], "KD")
            id=id+1
    

    print("*"*50)
    print("Total price of Order", get_total_price(order_list),"KWD")
    accept_credit_card(get_total_price(order_list))
    print("*"*50)
    print("      Thank you for shopping at SweetTooth ! ")
    print("*"*50)

#Sources:
    #https://www.python-course.eu/python3_dictionaries.php
    #https://stackoverflow.com/questions/5681271/or-statement-handling-two-clauses-python
    #http://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
    #https://www.programiz.com/python-programming/list
    #https://www.programiz.com/python-programming/methods/list/append
    #https://www.decalage.info/en/python/print_list
    #https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html