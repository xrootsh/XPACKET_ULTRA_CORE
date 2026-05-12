import asyncio
import aiohttp
import os
import time
import sqlite3
import json
import threading
import signal
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn
from colorama import Fore, Style, init
from urllib.parse import urlparse

init(autoreset=True)
app = FastAPI()

# --- CONFIG ---
WORDLIST_PATH = "SecLists/Discovery/Web-Content/common.txt"
DB_PATH = "database/scan_history.db"
os.makedirs("database", exist_ok=True)

# ---------------- X🔴PACKET™ HEADER ----------------
def header():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # ASCII Header - TM exactly 1 space from ASCII
    print(Fore.RED + Style.BRIGHT + "    __  __ ___  _   ___ _  __ ___ _____ " + Fore.WHITE + "™")
    print(Fore.RED + Style.BRIGHT + "    \\ \\/ /| _ \\/_\\ / __| |/ /| __|_   _|")
    print(Fore.RED + Style.BRIGHT + "     >  < |  _/ _ \\ (__| ' < | _|  | |")
    print(Fore.RED + Style.BRIGHT + "    /_/\\_\\|_|/_/ \\_\\___|_|\\_\\|___| |_|   " + Fore.WHITE + "v10.5\n")
    
    # Developer name set to Cybervedan
    print(" " * 12 + Fore.WHITE + "Developed by: " + Fore.GREEN + Style.BRIGHT + "Cybervedan")
    print(Fore.CYAN + "—" * 55)
    
    # Shortened Tagline to ensure single line in Termux
    print("   " + Fore.WHITE + Style.BRIGHT + "PRO FUZZER & DB INTEL | DIR SCAN v28")
    print(Fore.CYAN + "—" * 55)

# ---------------- DB LAYER ----------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS scans
                (target TEXT, path TEXT, status INTEGER, url TEXT, timestamp TEXT)""")
    conn.commit()
    conn.close()

def save_log(target, path, status, url):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO scans VALUES (?,?,?,?,?)", (target, path, status, url, time.ctime()))
    conn.commit()
    conn.close()

# ---------------- GLOBAL CONTROL ----------------
paused = False
stop = False
done = 0
total = 0

# ---------------- WORKER ENGINE ----------------
async def worker(session, target, queue, ws):
    global done, paused, stop
    while not queue.empty() and not stop:
        while paused:
            await asyncio.sleep(0.5)

        path = await queue.get()
        url = f"{target.rstrip('/')}/{path}"
        try:
            async with session.get(url, timeout=5, allow_redirects=False) as r:
                if r.status in [200, 301, 302, 401, 403]:
                    progress = round((done / total) * 100, 2)
                    save_log(target, path, r.status, url)
                    await ws.send_json({
                        "path": path,
                        "status": r.status,
                        "url": url,
                        "progress": progress
                    })
        except:
            pass
        done += 1
        queue.task_done()

# ---------------- EXIT ENDPOINT ----------------
@app.get("/exit")
def exit_server():
    print(Fore.GREEN + "\n [✓] Web UI Exit Triggered. Returning to Menu...")
    os.kill(os.getpid(), signal.SIGINT)
    return {"status": "shutdown"}

# ---------------- WEBSOCKET ----------------
@app.websocket("/ws")
async def ws(websocket: WebSocket):
    global paused, stop, done, total
    await websocket.accept()
    try:
        while True:
            msg = await websocket.receive_text()
            if msg == "PAUSE": paused = True; continue
            if msg == "RESUME": paused = False; continue
            if msg == "STOP": stop = True; continue

            # New Scan Init
            target = msg if msg.startswith("http") else "http://" + msg
            stop = False; paused = False; done = 0

            # Wordlist Loading logic
            if os.path.exists(WORDLIST_PATH):
                with open(WORDLIST_PATH) as f:
                    paths = [x.strip() for x in f if x.strip() and not x.startswith("#")]
            else:
                paths = ["admin","login","api","db",".env","uploads","backup","wp-admin"]

            total = len(paths)
            queue = asyncio.Queue()
            for p in paths: queue.put_nowait(p)

            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=25)) as session:
                print(Fore.YELLOW + f" [*] PRO Scan Started: {target}")
                workers = [asyncio.create_task(worker(session, target, queue, websocket)) for _ in range(15)]
                await queue.join()
                for w in workers: w.cancel()
                print(Fore.GREEN + " [✓] PRO Scan Completed.")
    except WebSocketDisconnect:
        pass

# ---------------- UI DASHBOARD ----------------
HTML = """
<!DOCTYPE html><html>
<head><title>X-PACKET v28 PRO</title>
<style>
    body{background:#0a0a0a; color:#00ff99; font-family:monospace; padding:20px;}
    .controls{background:#111; padding:20px; border:1px solid #333; border-radius:8px; text-align:center; margin-bottom:20px;}
    input{background:#000; color:#00ff99; border:1px solid #00ff99; padding:12px; width:45%; border-radius:4px; outline:none;}
    button{padding:12px 15px; cursor:pointer; font-weight:bold; border:none; border-radius:4px; margin:2px; transition: 0.3s;}
    .btn-main{background:#ff3333; color:white;}
    .btn-ctrl{background:#444; color:white;}
    .btn-ctrl:hover{background:#666;}
    .btn-back{background:#ff9900; color:#000;}
    .btn-back:hover{background:#e68a00;}
    .card{background:#151515; padding:10px; margin-bottom:5px; border-left:4px solid #ffcc00; display:flex; justify-content:space-between;}
</style>
</head>
<body>
    <h2 style="text-align:center; color:#ff3333;">📁 X🔴PACKET™ <span style="color:white; font-size:18px;">DIR SCANNER v28.0</span></h2>
    <div class="controls">
        <input id="t" placeholder="Target Domain (e.g. example.com)">
        <button class="btn-main" onclick="startScan()">SCAN</button>
        <button class="btn-ctrl" onclick="sendCtrl('PAUSE')">PAUSE</button>
        <button class="btn-ctrl" onclick="sendCtrl('RESUME')">RESUME</button>
        <button class="btn-ctrl" onclick="sendCtrl('STOP')">STOP</button>
        <button class="btn-back" onclick="goBack()">[ BACK ]</button>
    </div>
    <div id="out"></div>
    <script>
        let ws = new WebSocket("ws://"+location.host+"/ws");
        ws.onmessage = (e) => {
            let d = JSON.parse(e.data);
            let out = document.getElementById("out");
            let div = document.createElement("div");
            div.className = "card";
            div.style.borderColor = d.status == 200 ? "#00ff99" : "#ffcc00";
            div.innerHTML = `<span><b>${d.path}</b></span> <span>HTTP ${d.status} (${d.progress}%)</span>`;
            out.prepend(div);
        }
        function startScan(){ document.getElementById("out").innerHTML=""; ws.send(document.getElementById('t').value); }
        function sendCtrl(cmd){ ws.send(cmd); }
        function goBack(){ fetch('/exit').then(() => window.close()); }
    </script>
</body></html>
"""

@app.get("/")
def home(): return HTMLResponse(HTML)

@app.get("/export")
def export():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM scans")
    data = cur.fetchall()
    conn.close()
    return JSONResponse({"logs": data})

# ---------------- TERMINAL INPUT LISTENER ----------------
def terminal_listener():
    try:
        while True:
            cmd = input().strip()
            if cmd in ["00", "0", "exit", "back"]:
                print(Fore.GREEN + "\n [✓] Closing Module. Returning to Command Center...")
                os.kill(os.getpid(), signal.SIGINT)
                break
    except:
        pass

if __name__ == "__main__":
    init_db()
    header()
    print(Fore.YELLOW + " [*] Dir Scanner Engine: " + Fore.GREEN + "ONLINE")
    print(Fore.YELLOW + " [*] Dashboard URL: " + Fore.CYAN + "http://localhost:8005\n")
    
    # Compact line for returning
    print(Fore.WHITE + " (Type " + Fore.RED + "'00'" + Fore.WHITE + " to return to Menu)\n")

    # Start the background listener for '00'
    threading.Thread(target=terminal_listener, daemon=True).start()

    # Start the web server
    uvicorn.run(app, host="0.0.0.0", port=8005, log_level="error")
