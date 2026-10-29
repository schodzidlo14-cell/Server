@echo off
chcp 65001 > nul
echo Naprawianie pliku server.properties (wyłączanie online-mode)...

powershell -Command "$content = Get-Content 'server.properties'; $content = $content -replace 'online-mode=true', 'online-mode=false'; Set-Content 'server.properties' $content"

echo Gotowe! Tryb online został wyłączony.
echo Teraz zrestartuj serwer (wyłącz i włącz ponownie start.bat).
pause
