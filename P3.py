#Arnas Oonsadao, 633040233-2
"""
Lab 2 Variables and Collections: Problem 3
"""
def add_number(list):
    print("Before adding an interger, the list is", list)
    add = int(input("Enter a number to add to a list: "))
    list.append(add)
    print("Before adding an interger, the list is", list)
def replace_number(list):
    print("Finding a number to replace in the list", list)
    find_num = int(input("Enter a number to find: "))
    replace_num = int(input("Enter a new number to replace: "))
    new_num = [i if i != find_num else replace_num for i in list]
    print("After replacing %s with %s, the new list is %s"%(find_num,replace_num,new_num))
def remove_number(list):
    print("Finding a number to remove in the list", list)
    remove_num = int(input("Enter a new number to remove: "))
    list.remove(remove_num)
    print("After replacing %s, the list is %s"%(remove_num,list))

if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 5]
    add_number(num_list)
    replace_number(num_list)
    remove_number(num_list)



