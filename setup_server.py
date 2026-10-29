import urllib.request
import json
import os
import subprocess

def setup():
    print("Pobieranie listy wersji PaperMC...")
    url = "https://api.papermc.io/v2/projects/paper/versions/1.21.4"
    req = urllib.request.urlopen(url)
    data = json.loads(req.read().decode())
    builds = data["builds"]
    latest_build = builds[-1]
    
    jar_url = f"https://api.papermc.io/v2/projects/paper/versions/1.21.4/builds/{latest_build}/downloads/paper-1.21.4-{latest_build}.jar"
    jar_name = f"paper-1.21.4-{latest_build}.jar"
    
    print(f"Pobieranie PaperMC build {latest_build}...")
    urllib.request.urlretrieve(jar_url, jar_name)
    
    with open("eula.txt", "w") as f:
        f.write("eula=true\n")
        
    with open("server.properties", "w") as f:
        f.write("server-port=25565\nonline-mode=false\n")
        
    print("Serwer skonfigurowany pomyślnie!")
    
if __name__ == "__main__":
    setup()
