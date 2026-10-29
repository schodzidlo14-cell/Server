FROM eclipse-temurin:21-jdk-jammy

WORKDIR /data

# Kopiujemy wszystkie pliki serwerowe do kontenera
COPY . /data

# Otwieramy port Minecrafta
EXPOSE 25565

# Uruchamiamy serwer z limitami RAM dostosowanymi do Railway (np. 1GB)
CMD ["java", "-Xmx1024M", "-Xms512M", "-jar", "server.jar", "nogui"]
