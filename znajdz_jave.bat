@echo off
chcp 65001 > nul
echo Szukam Javy 21 w systemie...
echo.

for /f "tokens=*" %%i in ('where java 2^>nul') do (
    echo Znaleziono: %%i
    "%%i" -version
    echo -----------------------------------
)

echo Jeśli masz Javy w innych miejscach, poszukaj w folderach takich jak:
echo C:\Program Files\Java\
echo C:\Program Files\Eclipse Adoptium\
echo C:\Program Files\Microsoft\
echo C:\Users\%USERNAME%\AppData\Local\Programs\
echo.
pause
