from fastapi import FastAPI
from APIModel.Response import response_util
from APIModel.Requests import requests_util
from lib import common,constants,error_codes


app = FastAPI()

# define database server here
store_items = dict()
store_items[0] = "apple"
store_items[1] = "pear"

@app.get("/")
async def root():
    return response_util.create_success_response()

@app.get("/root/{item_id}")
def print_item(item_id):
    # exception handling here
    if item_id not in store_items:
        return "item not found"
    return store_items[item_id]