from typing import Union

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/student/")
def read_sagar():
    return {"name": "sagar",
            "class":"learning fastapi"}

@app.get("/numbers/{number}")
def read_item(number: int):

    sum_of_n_numbers = 0

    for el in range(1, number+1):
        sum_of_n_numbers = sum_of_n_numbers + el


    return {"sum": sum_of_n_numbers}
