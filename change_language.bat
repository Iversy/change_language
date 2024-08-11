@echo off
taskkill /F /IM pythonw.exe
start /MIN pythonw.exe %USERPROFILE%\Documents\change_language\change_language.py