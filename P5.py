#Arnas Oonsadao, 633040233-2
"""
Lab 2 Variables and Collections: Problem 5
"""
taekwondo_olympics2020_w49k = {
    "Gold": {"Thailand"},
    "Silver": {"Spain"},
    "Bronze": {"Israel","Serbia"}
}
print("The list of medals in Taekwondo Olympics 2020 women 49 kilograms:")
for key, value in taekwondo_olympics2020_w49k.items():
    for items in value:
        print("%s received %s medal"%(items, key))
print("The dictionary of medals is", taekwondo_olympics2020_w49k)




