# Json -  json is used for storing and exchanging the data and is text , written with javascript object notion
# import json

# x = '{"name":"yousuf","age":21,"city":"Chennai"}'        # Json Data

# y = json.loads(x)                                        # Parse x

# print(y["age"])                                          # Result is python dictionary

# Convert python to JSON

# import json

# x = {                               # Python dictionary
#     "name":"yousuf",
#     "age":21,
#     "city":"Chennai"
# }

# y = json.dumps(x)                   # convert into json

# print(y)                            # result is json string

# Convert From Python into JSON
# import json

# print(json.dumps({"name":"Yousuf","age":21}))     # Dictionary to Object
# print(json.dumps(["Apple","Orange"]))             # List to Array
# print(json.dumps(("Apple","Orange")))             # Tuple to Array
# print(json.dumps("Yousuf"))                       # str to String
# print(json.dumps(145))                            # int to Number
# print(json.dumps(2.5))                            # float to Number
# print(json.dumps(True))                           # True to true
# print(json.dumps(False))                          # False to false
# print(json.dumps(None))                           # None to null

# import json

# x = "Yousuf"

# y = json.dumps(x)
# print(y)

# import json

# x = {
#     "name":"Yousuf",
#     "age":21,
#     "married":False,
#     "single":True,
#     "disease":None,
#     "fav.fruits":("Apple","Banana"),
#     "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # y = json.dumps(x,indent = 4)                           # indent will make the json string readable
# # y = json.dumps(x,indent = 4,separators=(".","="))
# y = json.dumps(x,indent = 4,sort_keys=True)
# print(y)

# Regular Expression - RegEx can be used to check if the string contains specific string pattern

# import re

# txt = "The rain in Spain"

# y = re.search("^The.*Spain$",txt)

# if y:
#     print("Match Found")

# else:
#     print("Match not found")

# RegEx Functions
# findall()

# import re

# txt = "The rain in Spain"
# x = re.findall("ai",txt)
# print(x)

# search()

# import re

# txt = "The rain in Spain"
# x = re.search("\\s",txt)
# print("The First whitespace occur in the position:",x.start())
# x = re.search("Portugal",txt)
# print(x)

# split()

# import re

# txt = "The rain in Spain"
# # x = re.split("\\s",txt)
# x = re.split("\\s",txt,1)             # maxsplit is given in end of split to specify no.of.splits
# print(x)

# sub()

# import re

# txt = "The rain in Spain"
# # y = re.sub("\s","9",txt)
# y = re.sub("\s","9",txt,2)         # Substitute for first 2 occurences
# print(y)

# Match Objects

# span()

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+",txt)
# print(x.span())

# string

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+",txt)
# print(x.string)

# group()

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+",txt)
print(x.group())