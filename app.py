import requests
import json
from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"Item": "lata", "Preço": 4, "quantidade":5},
    2: {},
    3: {},
    4: {}
}

@app.get("/")
def home():
    return {"Vendas":len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
     return vendas[id_venda]
    else: 
       return {"erro":"ID da venda inexistente"}
