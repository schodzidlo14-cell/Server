import urllib.request
import json

print("Pobieranie listy projektów PaperMC...")
try:
    # Pobieramy główną listę wersji, aby ominąć przestarzałe ścieżki
    url = "https://api.papermc.io/v2/projects/paper"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        versions = data["versions"]
        if "1.21.4" not in versions:
            print("Wersja 1.21.4 nie została znaleziona w API.")
            exit(1)

    # Pobieramy buildy dla 1.21.4
    ver_url = "https://api.papermc.io/v2/projects/paper/versions/1.21.4"
    req_ver = urllib.request.Request(ver_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req_ver) as response:
        ver_data = json.loads(response.read().decode())
        latest_build = ver_data["builds"][-1]

    jar_url = f"https://api.papermc.io/v2/projects/paper/versions/1.21.4/builds/{latest_build}/downloads/paper-1.21.4-{latest_build}.jar"
    print(f"Pobieranie silnika: {jar_url}")
    
    jar_req = urllib.request.Request(jar_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(jar_req) as u, open("server.jar", "wb") as f:
        f.write(u.read())

    with open("eula.txt", "w") as f:
        f.write("eula=true\n")

    with open("server.properties", "w") as f:
        f.write("server-port=25565\nonline-mode=false\nenable-query=false\n")

    with open("start.bat", "w") as f:
        f.write("java -Xmx2G -Xms2G -jar server.jar nogui\npause\n")

    print("SUKCES! Pliki serwera zostały pobrane i skonfigurowane.")
except Exception as e:
    print(f"Błąd: {e}")
    print("\nAlternatywa: Otwórz przeglądarkę, wejdź na oficjalną stronę PaperMC, pobierz silnik Paper w wersji 1.21.4, zmień jego nazwę na 'server.jar' i wrzuć do tego folderu wraz z plikiem 'start.bat' zawierającym linijkę: java -jar server.jar")
