from pymongo import MongoClient
import pymongo
from django.shortcuts import render
from django.http import JsonResponse

client = MongoClient("mongodb+srv://joelferguson:crickeT1234@cluster0.cwjrv.mongodb.net/test?retryWrites=true&w=majority")
db = client["ardsDB"]
team = db.team


def show_one_member(name):
    results = []
    for member in team.find({"name": {'$regex': '.*'+name+'.*'}}):
        results.append(member)
    print(results)


def count_members():
    post_count = team.count_documents({})
    print(post_count)


def index():
    results = []
    for member in team.find({"name": {'$regex': '.*' + "Joel" + '.*'}}):
        results.append(member)
    return JsonResponse({"members": results})


show_one_member("Joel")

count_members()

'''
index()
'''