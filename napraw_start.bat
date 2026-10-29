@echo off
chcp 65001 > nul
echo Tworzenie poprawnego pliku start.bat z użyciem Twojej Javy 21...

(
echo @echo off
echo "C:\Users\szymo\AppData\Local\Programs\Eclipse Adoptium\jdk-21.0.12.101-hotspot\bin\java.exe" -Xmx2G -Xms2G -jar server.jar nogui
echo pause
) > start.bat

echo Gotowe! Plik start.bat został zaktualizowany i wskazuje bezpośrednio na Javę 21.
echo Teraz możesz uruchomić plik start.bat, aby włączyć serwer.
pause
