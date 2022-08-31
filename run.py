import os

from main import (
    Opration,
    Warehouse,
    Writer,
    Editor,
    Accountants,
    Research
)

if __name__ == '__main__':
    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("""Enter one of these:
            if you want to write a list Enter=> w

            if you want to edit list of goods Enter=> e

            if you want to delete the goods in list Enter=> d

            if you want to show the list Enter=> s

            if you want to get the total cost of list press => b

            if you want to change the place of two item press => ch

            if you want to search the item in list  press => se

            if you want to save your data press => f

            if you want to close the program Enter => c
                                                            """)
        handel = input("Enter one of these itemes: ")
        handel = handel.lower()

        if handel == "w":
            print("""
        They are in your warehouse:
name : cucumber | numb :         10 | cost : 9
name : onion | numb :         5 | cost : 8
name : apple | numb :         20 | cost : 20
name : orange | numb :         20 | cost : 20
name : milk | numb :         10 | cost : 20
name : yogurt | numb :         5 | cost : 10""")
            pro = Warehouse.ware_house()
            goods_cost = Warehouse.ware_house_cost(pro)
            goods_name = Warehouse.ware_house_goods_name(pro)
            print("\n now please enter your list\n")
            show = Writer(goods_name, goods_cost, pro).get_goods()
            print("\n This is your shopping list \n")
            Opration(show, pro).final_show_list()
            show_ware = Opration(show, pro).decreaser()
            print("\n this the updated data of ware house \n ")
            Opration(show_ware, pro).final_show_list()

        elif handel == "e":
            Opration(show, pro).final_show_list()
            show = Editor(show, pro).edit_list()
            Opration(show, pro).final_show_list()

        elif handel == "d":
            print("befor edit")
            Opration(show, pro).final_show_list()
            Editor(show, pro).delete_item()
            show_ware = Opration(show, pro).increaser()
            print("after edit")
            Opration(show, pro).final_show_list()

        elif handel == "s":
            Opration(show, pro).final_show_list()

        elif handel == "b":
            number_goods_list_ = Opration(show, pro).number_goods_getter()
            cost_goods_list_ = Opration(show, pro).cost_goods_getter()
            ttl = Accountants(show, number_goods_list_, cost_goods_list_)
            print(f"the total cost you should pay is :${ttl}")
            Opration(show, pro).final_show_list()

        elif handel == 'ch':
            Opration(show, pro).final_show_list()
            Opration(show, pro).change_place()
            Opration(show, pro).final_show_list()

        elif handel == 'se':
            name_goods_list_ = Opration(show, pro).name_goods_getter()
            print(Research(name_goods_list_))
            Opration.waiter()
        elif handel == 'f':
            Opration(show, pro).final_print()
            print("data print in a csv file")
            Opration.waiter()

        elif handel == "c":
            break
        else:
            os.system('cls')
            print("error")
