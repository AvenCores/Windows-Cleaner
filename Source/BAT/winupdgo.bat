@ECHO OFF
cd %windir%\SoftwareDistribution\Download\
del /q /f /s %windir%\SoftwareDistribution\Download\*.*
rd /q /s %windir%\SoftwareDistribution\Download\