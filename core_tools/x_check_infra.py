import asyncio
from neo4j import AsyncGraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

async def check_x_infra():
    print("🔍 Testing X🔴INFRA Connection...")
    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    password = os.getenv("NEO4J_PASS", "password")
    
    try:
        driver = AsyncGraphDatabase.driver(uri, auth=(user, password))
        async with driver.session() as session:
            result = await session.run("RETURN 'X-INFRA ONLINE' as status")
            record = await result.single()
            print(f"✅ Status: {record['status']}")
        await driver.close()
    except Exception as e:
        print(f"❌ X-INFRA OFFLINE: {e}")

if __name__ == "__main__":
    asyncio.run(check_x_infra())
