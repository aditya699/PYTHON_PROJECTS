import json
from difflib import get_close_matches
data = json.load(open("C:/Users/aditya/Desktop/LifePY/Applications/APP_DICT/data.json"))
# print(type(data))
def funct(n):
    n=n.lower()
    if n in data:
        return data[n]
    elif len(get_close_matches(n,data.keys())) > 0:
        yn= input("Did you mean %s instead?  Enter Y if yes , N if no : " % get_close_matches(n,data.keys())[0])
        if yn=="Y":
           return data[get_close_matches(n,data.keys())[0]]
        elif yn=="N":
            return "The word doesn't exist.Please double check it'"
        else:
            return "We didn't understand ur query"

    else:
        return "The word doesn't exist.Please double check'"

n=input("enter the word whose meaning u want: ")
output=funct(n)
if type(output)==list:
    for i in output:
        print (i)
else:
    print (output)
