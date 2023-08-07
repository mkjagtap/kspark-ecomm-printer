from fastapi import FastAPI
from printer import Printer

app = FastAPI()
printer_list = []

@app.get("/")
def home():
    print(f"inside home function")
    return {"message": "Welcome to the Mukesh's printer shop!"}

@app.post("/new-printer")
def add_new_printer(printer: Printer):
    print(f"inside add new printer method")
    printer_list.append(printer.dict())
    return printer_list

@app.get("/printers")
def get_printer():
    print(f"inside get printer")
    return {"availble_printers": printer_list}