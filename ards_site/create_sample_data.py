from pymongo import MongoClient
import pymongo

client = MongoClient("mongodb+srv://joelferguson:crickeT1234@cluster0.cwjrv.mongodb.net/test?retryWrites=true&w=majority")
db = client["ardsDB"]
team = db.team


data = [
    {
        "name": "Joel Ferguson",
        "role": "player",
        "type": "batter",
        "team": "secondXi",
        "dateJoined": "2007-05-20",
        "mobile": "07759008631",
        "awards": [{
            "year": 2015,
            "type": "batting",
        }],
    },
]

for new_member in data:
    team.insert_one(new_member)
