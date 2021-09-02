# Arnas Oonsadao, 633040233-2
"""
Lab 4 Errors and Exceptions: Problem 4
"""
import json
with open("hobbies.json","r") as read_f:
    data = json.load(read_f)
    #print(f"data is {data}")
    firstName = data["firstName"]
    hobbies = data["hobbies"]
    hobbies_join = ', '.join(hobbies)
    print(f"{firstName} has hobbies as {hobbies_join}")
