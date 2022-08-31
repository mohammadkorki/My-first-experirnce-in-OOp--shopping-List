import csv
from typing import List


class Warehouse:
    """
    This class contained Warehouse product
    """
    def ware_house() -> List:
        """this function is ware house and it makes your ware house"""

        vegtable = [['cucumber', '10', '9'], ['onion', '5', '8']]
        fruits = [['apple', '20', '20'], ['orange', '20', '20']]
        dairy = [['milk', '10', '20'], ['yogurt', '5', '10']]
        product = vegtable + fruits + dairy

        return product

    def ware_house_goods_name(product: List) -> List:
        """THis function is contained our ware house name
        that help to reduce the population of itration

        Parameters
        ----------
        product: List :


        Returns
        -------


        """
        goods_name = list()
        for i in range(len(product)):
            goods_name.append(product[i][0])
        return goods_name

    def ware_house_goods_number(product: List) -> List:
        """THis function is contained our ware house number
        that help to reduce the population of itration

        Parameters
        ----------
        product: List :


        Returns
        -------


        """
        goods_number = list()
        for i in range(len(product)):
            goods_number.append(product[i][1])
        return goods_number

    def ware_house_cost(product: List) -> List:
        """THis function is contained our ware house cost
        that help to reduce the population of itration

        Parameters
        ----------
        product: List :


        Returns
        -------


        """
        goods_cost = list()
        for i in range(len(product)):
            goods_cost.append(product[i][2])
        return goods_cost


class Writer:
    """
    This class contain functions
    that get goods
    """
    def __init__(self, goods_name, goods_cost, product):
        self.goods_name = goods_name
        self.goods_cost = goods_cost
        self.product = product

    def get_goods(self) -> List:
        """This function gets your
        goods from your ware house

        Parameters
        ----------

        Returns
        -------


        """
        print("If you want to close your list Enter 'close' ")
        goods_list = list()
        while True:
            each_goods_info = list()

            name_goods = input("Enter name of goods: ")
            name_goods = name_goods.strip(" ")
            if name_goods != 'close':
                if name_goods in self.goods_name:
                    try:
                        number_goods = int(input("Enter number of goods: "))

                    except ValueError:
                        print()
                        print("you should enter number !!!!!")
                        continue
                    each_goods_info.append(name_goods)
                    each_goods_info.append(number_goods)

                    for i in range(len(self.product)):
                        if name_goods == self.product[i][0]:
                            each_goods_info.append(self.goods_cost[i])
                            if number_goods > int(self.product[i][1]):
                                print("we dont have enough storage ")
                            else:
                                if each_goods_info not in goods_list:
                                    goods_list.append(each_goods_info)
                                    print("data set in your list")

                                continue
                else:
                    print("this is not in ware house choose again!")
            else:
                return goods_list


class Editor:
    """
    This class include edit and delete functions
    """
    def __init__(self, goods_list, pro) -> None:
        self.goods_list = goods_list
        self.pro = pro

    def edit_list(self) -> List:
        """This function is edditing ypur goods list"""

        while True:
            try:
                Item = int(input("enter wich one you want to edit: "))
                break
            except ValueError:
                print("you must enter number not character")
                continue
        goods_Item = self.goods_list[Item-1]
        for i in range(len(self.pro)):
            if self.goods_list[Item-1][0] == self.pro[i][0]:
                self.pro[i][1] = str(int(self.pro[i][1]) + int(goods_Item[1]))
        edit_goods = list()
        edit_goods_name = input("Enter your name of altenative goods: ")
        name_ware_house = list()
        for i in range(len(self.pro)):
            name = self.pro[i][0]
            name_ware_house.append(name)
        if edit_goods_name in name_ware_house:
            while True:
                try:
                    # edit_goods.append(edit_goods_name)
                    edit_goods_number = input("Enter your number \
    of altenative goods: ")
                    for i in range(len(name_ware_house)):
                        if edit_goods_name in self.pro[i][0]:
                            self.pro[i][1] = str(int(self.pro[i][1])-int(edit_goods_number))#E501
                            if int(self.pro[i][1]) >= 0:
                                edit_goods.append(edit_goods_name)
                                edit_goods.append(edit_goods_number)
                                if edit_goods_name in self.pro[i][0]:
                                    edit_goods.append(self.pro[i][2])

                            else:
                                print("its not enough in your warehouse")
                                break
                    break

                except ValueError:
                    print("please Enter number not character ")
                    continue

            self.goods_list[Item - 1] = edit_goods
            return self.goods_list

    def delete_item(self) -> List:
        """This function is deleting your goods list item
        Parameters

        ----------
        show :Output of get goods

        Returns list
        -------

        Parameters
        ----------

        Returns
        -------


        """
        while True:
            try:
                choose_item = int(input("Enter wich item you want to edit: "))
                break
            except ValueError:
                print('you should enter number not character')
                continue
        self.goods_list.pop(choose_item-1)
        return self.goods_list


class Opration:
    """
    This class is use for opration works
    like show in list form , decrease/increase of
    warehouse
    """
    def __init__(self, goods_list, product):
        self.goods_list = goods_list
        self.product = product

    def final_show_list(self) -> str:
        """It will design and show your list of shopping items"""
        show_list_ = list()
        while True:
            try:
                for i in range(len(self.goods_list)):
                    Item_show = print(f'name : {self.goods_list[i][0]} | numb:\
            {self.goods_list[i][1]} | cost : {self.goods_list[i][2]}')
                    show_list_.append(Item_show)
                waiter = input("Enter any key to continue: ")
                print(waiter)
                break
            except TypeError:
                print("choose some thing in ware house")
                break

        return show_list_

    def decreaser(self) -> List:
        """This function is decrease quantity of
        your ware house goods

        Parameters
        ----------

        Returns
        -------


        """
        for i in range(len(self.product)):
            for j in range(len(self.goods_list)):
                if self.product[i][0] == self.goods_list[j][0]:
                    self.product[i][1] = str(int(self.product[i][1]) - int(self.goods_list[j][1]))#E501
        return self.product

    def increaser(self) -> List:
        """This function is increase quantity of
        your ware house goods

        Parameters
        ----------
        product : its the output of your warehouse

        goods_list : list


        Returns
        -------


        """
        for i in range(len(self.product)):
            for j in range(len(self.goods_list)):
                if self.product[i][0] == self.goods_list[j][0]:
                    self.product[i][1] = str(int(self.product[i][1]) + int(self.goods_list[j][1]))#E501
        return self.product

    def number_goods_getter(self):
        """this function is use to get the number of function"""
        number_goods_list = list()
        for i in range(len(self.goods_list)):
            number_goods_list.append(self.goods_list[i][1])
        return number_goods_list

    def name_goods_getter(self) -> List:
        """this function is use to get the name of function"""
        name_goods_list = list()
        for i in range(0, len(self.goods_list)):
            name_goods_list.append(self.goods_list[i][0])
        return name_goods_list

    def cost_goods_getter(self) -> List:
        """this function is use to get the cost of function
        it will use for caluculating your list and how much you should pay

        Parameters
        ----------

        Returns
        -------


        """
        cost_goods_list = list()
        for i in range(len(self.goods_list)):
            cost_goods_list.append(self.goods_list[i][2])
        return cost_goods_list

    def change_place(self) -> None:
        """its use full to chenge the item in your shopping list"""
        while True:
            try:
                first_Item = int(input("Enter the number of item tat you want\
    to change its place: "))
                print("\n data set \n")
                break
            except ValueError:
                print("you should enter number not character")
                continue
        second_Item = int(input("Enter the number of item tat you want to \
    replace with first Item: "))
        alt_list = list()
        alt_list = [self.goods_list[second_Item - 1], self.goods_list[first_Item - 1]]#E501
        self.goods_list[first_Item - 1] = alt_list[0]
        self.goods_list[second_Item - 1] = alt_list[1]
        return self.goods_list

    def waiter() -> None:
        """This function is used for see the rsault"""
        x = input("\n if check press any key to continue \n")
        return x

    def final_print(self) -> None:
        """This function is making csv file
        and print your final list

        Parameters
        ----------

        Returns
        -------

        """
        with open('shopping_list.csv', 'w', encoding='UTF8') as file:

            writer = csv.writer(file)

            writer.writerow(self.goods_list)


class Research:
    """
    This class is used for researching the data in
    your goods list
    """
    def __init__(self, name_goods_list) -> None:
        self.name_goods_list = name_goods_list

    def research(self) -> str:
        """This function is search to find wich things in my list"""
        research_vlaue = input("search something you want : ")
        while True:
            if research_vlaue in self.name_goods_list:
                return f"{research_vlaue} is availaable!!"

            else:
                return f"{research_vlaue} is not availaable!!"

    def __repr__(self) -> str:
        return str(self.research())


class Accountants:
    """
    this class include a function is used for
    calucating the data to pay
    """
    def __init__(self, goods_list, number_goods_list, cost_goods_list):
        self.goods_list = goods_list
        self.number_goods_list = number_goods_list
        self.cost_goods_list = cost_goods_list

    def total_cost(self) -> str:
        """

        Parameters
        ----------
        this function is calculating the cost to pay :

        goods_list : its got from goods getter function

        number_goods_list : its got from number_goods_list function

        cost_goods_list : its got from cost_goods_list function


        Returns
        -------


        """
        total_cost_list = list()
        for i in range(len(self.goods_list)):
            total_costt = int(self.number_goods_list[i]) * int(self.cost_goods_list[i])#E501
            total_cost_list.append(total_costt)
        total_cost = sum(total_cost_list)
        return total_cost

    def __repr__(self) -> str:
        return str(self.total_cost())
