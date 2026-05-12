import os
import time
import asyncio
from typing import Optional, Dict, Any, List
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Depends, WebSocket, Security
from fastapi.middleware.cors import CORSMiddleware
from neo4j import AsyncGraphDatabase, AsyncDriver, AsyncSession
from pydantic import BaseModel

# ശരിക്കുള്ള പാസ്‌വേഡ് നേരിട്ട് ഇവിടെ നൽകുന്നു
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASS = "Shivasakthi" 

driver: Optional[AsyncDriver] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global driver
    driver = AsyncGraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    yield
    await driver.close()

app = FastAPI(title="XPACKET™ ULTRA", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_session() -> AsyncSession:
    if driver is None: raise HTTPException(status_code=500, detail="DB not ready")
    return driver.session(database="neo4j")

@app.get("/")
async def status():
    return {"status": "ONLINE", "engine": "XPACKET ULTRA v131"}

@app.get("/intel/network-graph")
async def network_graph():
    query = "MATCH (d:Domain)-[:HAS_SUBDOMAIN]->(s:Subdomain)-[:RESOLVES_TO]->(i:IP) RETURN d.name AS domain, s.name AS subdomain, i.addr AS ip LIMIT 100"
    try:
        async with await get_session() as session:
            result = await session.run(query)
            graph = []
            async for r in result:
                graph.append({"from": r["domain"], "via": r["subdomain"], "to": r["ip"]})
            return {"graph": graph, "nodes_count": len(graph)}
    except Exception as e:
        return {"graph": [], "nodes_count": 0, "error": str(e)}
