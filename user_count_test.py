from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

class User(BaseModel):
    id: str

users = set()

@app.post("/user")
async def add_user(user: User):
    users.add(user.id)
    return {"count": len(users)}

@app.get("/count")
async def get_count():
    return {"count": len(users)}

@app.get("/generate_id")
async def generate_id():
    return {"id": str(uuid.uuid4())}

    import streamlit as st
import requests
