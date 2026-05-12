import os
from contextlib import asynccontextmanager
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from neo4j import AsyncGraphDatabase, AsyncDriver

NEO4J_URI = "bolt://localhost:7687"
driver: Optional[AsyncDriver] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global driver
    # പാസ്‌വേഡ് ഇല്ലാതെ കണക്ട് ചെയ്യുന്നു (Bypass Mode)
    driver = AsyncGraphDatabase.driver(NEO4J_URI, auth=None)
    yield
    if driver:
        await driver.close()

app = FastAPI(title="X🔴PACKET™ ULTRA", version="v131.2", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/intel/network-graph")
async def network_graph():
    query = "MATCH (d:Domain)-[:HAS_SUBDOMAIN]->(s:Subdomain)-[:RESOLVES_TO]->(i:IP) RETURN d.name AS root, s.name AS sub, i.addr AS target LIMIT 100"
    try:
        async with driver.session(database="neo4j") as session:
            result = await session.run(query)
            graph = []
            unique_nodes = set()
            async for r in result:
                graph.append({"from": r["root"], "to": r["target"], "via": r["sub"]})
                unique_nodes.add(r["root"]); unique_nodes.add(r["sub"]); unique_nodes.add(r["target"])
            return {"graph": graph, "nodes_count": len(unique_nodes)}
    except Exception as e:
        return {"graph": [], "nodes_count": 0, "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9003)
