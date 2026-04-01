from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/ip")
async def read_root(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}

# En liten placeholder array av objekt som representerar rum. Byts ut mot databas
rooms = [
    {"room_id": 1, "room_number": "101", "type": "Enkelrum", "price": 850, "occupied": False},
    {"room_id": 2, "room_number": "102", "type": "Enkelrum", "price": 850, "occupied": True},
    {"room_id": 3, "room_number": "201", "type": "Dubbelrum", "price": 1250, "occupied": False},
    {"room_id": 4, "room_number": "202", "type": "Dubbelrum", "price": 1250, "occupied": False},
    {"room_id": 5, "room_number": "301", "type": "Svit", "price": 2900, "occupied": False},
    {"room_id": 6, "room_number": "302", "type": "Svit", "price": 2900, "occupied": True}
]

@app.get("/api/rooms")
def read_rooms():
    return {"rooms": rooms}

@app.get("/")
def read_root():
    return { "msg": "Hey! I changed the message you silly goober.", "v": "0.1" }


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}
