from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def send_data(reuqest: Request):
    date,time = generate_time_stamp()
    payload = {
        "card_holder_name": generate_name(),
        "unique_id": generate_unique_id(),
        "validity": "Valid Card",
        "card_number": generate_card_number(),
        "cvv_number": generate_cvv(),
        "date": date,
        "time": time

    }
    context = {"request": reuqest, "payload": payload}
    generate_time_stamp()
    return templates.TemplateResponse("index.html", context)

def generate_unique_id():
    return f"{random.randint(000000,999999):06}"

def generate_name():
    fname = ["Aman", "Christian", "Elon", "Jonathan", "21", "John"]
    lname = ["Dubey", "Bale", "Mc Adams", "Savage", "Singh"]
    name = random.choice(fname)+ " "+ random.choice(lname)
    return name

def generate_card_number():
    hash_map = {
        10:1,
        12:3,
        14:5,
        16:7,
        18:9
    }
    flag=False
    while not flag:
        card_number = f"{random.randint(0000,9999):04} {random.randint(0000,9999):04} {random.randint(0000,9999):04} {random.randint(0000,9999):04}"
        cc_number = card_number.replace(" ","")
        list1 = [int(i) for i in list(cc_number)[-1::-2]]
        list2 = [hash_map.get(2*int(i), 2*int(i)) for i in list(cc_number)[-2::-2]]
        if (sum(list1)+sum(list2))%10==0:
            flag=True
    
    return card_number

def generate_cvv():
    return f"{random.randint(000,999):03}"

def generate_time_stamp():
    date_str = datetime.today()
    date = date_str.strftime("%b %d, %Y")
    time = date_str.strftime("%H:%M:%S")
    return date, time
