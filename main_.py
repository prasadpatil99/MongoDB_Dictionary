import json
from pymongo import MongoClient
from difflib import get_close_matches

client = MongoClient('localhost', 27017)

db = client['dictionary']                 # connecting to database

db_collc = db['collc']                    # connecting to collection

with open('data.json') as f:              # loading json file
    data = json.load(f)
                                          # replace dot present in key
final_data = {x.replace('.', ''): v for x, v in data.items()} 

db_collc.insert_one(final_data)           # insert data into database

for record in db_collc.find({}):          # retrieving data from databse
   		continue

def translate(w):
    w = w.lower()
    if w in record:
        return record[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or "y":
            return record[get_close_matches(w, record.keys())[0]]
        elif yn == "N" or "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
    

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
