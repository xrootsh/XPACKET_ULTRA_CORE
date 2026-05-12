from fastapi import FastAPI
import os, json

app = FastAPI(title="X🔴PACKET™ ULTRA DASHBOARD")

@app.get("/")
def read_root():
    return {"status": "ONLINE", "version": "v131.0 ULTRA", "engine": "X-Orchestrator"}

@app.get("/missions")
def get_missions():
    missions = os.listdir("missions")
    return {"active_missions": missions}

# Run using: uvicorn dashboard:app --reload
