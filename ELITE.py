import string
from datetime import datetime
import random

note = open('shop_list.txt','r')
fd = note.read()
note.close() 
products = fd.split('\n')

def Bill(a,b,c,d):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    print("\n************     SACHU's MINI D-Mart**********\n")
    print("time: ",datetime.now(),"      Transaction_id: ",ran)
    print('______________________________________________________________________')
    print('name\t\tprice\t\tqty\t\tsub-total')  
    print(a,'\t',b,'\t\t',c,'\t\t',d)
    print('_________                               _______________________')
    print('#Total                                          ',d)

def add_ex(add1): #this is the function to add existing items in mall
    add1
    new_record = []
    pro_id = input('enter the product id: ')
    qty = int(input("enter the quantity: "))
    
    for product in add1:
        prod = product.spli
        if pro_id == prod[0]:
            prod[4] = int(prod[4])+qty
        new_record.append(prod[0]+','+prod[1]+','+prod[2]+','+prod[3]+','+str(prod[4])+','+prod[5]+','+prod[6]+'\n')
    new_record[-1] = new_record[-1][:-1]
    f1 = open('shop_list.txt','w')
    for i in new_record:
        f1.write(i)
    f1.close()

def add_new(add1): #this is the function to add new items in mall
    new_record = add1
    
x = int(input("select your choice\n1 for customer\n2 for agent: "))

new_record = []
if x==1:
    pro_id = input("enter the product id: ")
    qty = int(input("enter the quantity: "))
    for product in products:
        prod = product.split(',')
        if pro_id == prod[0]:
            if qty <= int(prod[4]):
                d = float(prod[2])*qty
                Bill(prod[1],prod[2],qty,d)
                prod[4] = int(prod[4])-qty
            else:
                print("enter quantity exceeds the limit: ",prod[4])
        new_record.append(prod[0]+','+prod[1]+','+prod[2]+','+prod[3]+','+str(prod[4])+','+prod[5]+','+prod[6]+'\n')
if x==1:
    new_record[-1] = new_record[-1][:-1]

    f1 = open('shop_list.txt','w')
    for i in new_record:
          f1.write(i)
    f1.close()
if x==2:
    print("which product would you like to add: ")
    entry1 = int(input("enter 1 for existing: \nenter 2 for new item: "))
    if entry1 == 1:
        print("**********enter the product Details***************")
        pro_id = input("enter the product id: ")
        qty = int(input("enter the quantity: "))
        for product in products:
            prod = product.split(',')
            if pro_id == prod[0]:
                    prod[4] = int(prod[4]) + qty
            new_record.append(prod[0]+','+prod[1]+','+prod[2]+','+prod[3]+','+str(prod[4])+','+prod[5]+','+prod[6]+'\n')
        new_record[-1] = new_record[-1][:-1]
        f1 = open('shop_list.txt','w')
        for i in new_record:
            f1.write(i)
        f1.close()
    elif entry1==2:
        print("**********enter the product Details***************")
        pro_id = input('enter the product id: ')
        pro_name = input('enter the product Name: ')
        mall_price = input('enter the mall price: ')
        actual_price = input('enter the Actual price: ')
        qty = input("enter the quantity: ")
        prod_info = input("enter the product details: ")
        prod_exp = input("enter the product expiry: ")
        
        init1 = (pro_id+','+pro_name+','+mall_price+','+actual_price+','+qty+','+prod_info+','+prod_exp+'\n')
        f1 = open('shop_list.txt','a')
        f1.write("\n")
        f1.write(init1)
        f1.close()