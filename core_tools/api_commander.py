from fastapi import FastAPI, WebSocket
from neo4j import GraphDatabase
import uvicorn
import asyncio

app = FastAPI()

# --- DB CONFIG ---
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASS = "shivasakthi"

class GraphManager:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))

    def get_live_stats(self):
        with self.driver.session() as session:
            # ഡാറ്റാബേസിലെ നോഡുകളുടെ എണ്ണം എടുക്കുന്നു
            result = session.run("MATCH (n) RETURN count(n) as count")
            return result.single()["count"]

manager = GraphManager()

@app.get("/")
def root():
    return {"status": "X🔴PACKET™ INFRA ONLINE", "version": "v131.0 ULTRA"}

@app.get("/api/stats")
def stats():
    count = manager.get_live_stats()
    return {"total_nodes": count}

@app.websocket("/ws/graph")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # ഓരോ 5 സെക്കൻഡിലും പുതിയ ഡാറ്റാ അപ്‌ഡേറ്റ് അയക്കുന്നു
        count = manager.get_live_stats()
        await websocket.send_json({"live_nodes": count})
        await asyncio.sleep(5)

if __name__ == "__main__":
    print("\n[!] X🔴PACKET™ SOC DASHBOARD STARTING ON PORT 9003...")
    uvicorn.run(app, host="0.0.0.0", port=9003)
