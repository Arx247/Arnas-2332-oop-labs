#Arnas Oonsadao
#633040233-2
# Lab 11.  Useful modules : Problem 2. Splitting strings
import re

def split_str(lst): #function split the list
    list_split1 = lst[0].split()
    list_split2 = lst[1].split()
    # use re.split()
    print(*re.split(" ,*", f'{list_split1[0]} has email as {list_split1[1]} and phone as {list_split1[2]}'))
    print(*re.split(" ,*", f'{list_split2[0]} has email as {list_split2[1]} and phone as {list_split2[2]}'))

if __name__ == '__main__':
    lst = ["mana mana@kku.ac.th 043-222-3333",
           "manee manee@kku.ac.th. 043-888-9999"]
    split_str(lst)


# import re
# pat = ' '
# lst = "mana mana@kku.ac.th 043-22-3333 manee manee@kku.ac.th 043-888-9999"
# rr = re.split(pat,lst)
# print(rr)

# if __name__ == '__main___':
#     lst = ["mana mana@kku.ac.th 043-22-3333","manee manee@kku.ac.th 043-888-9999"]
#     split_str(lst)
#
# for i in range(len(lst)):
#     #     list_split = lst[i].split() #use re.split()
#     #     text_split = (list_split[0]) + f" has email as " + (list_split[1]) + f" and phone as " + (list_split[2]) #Showing
#     #     print(text_split)