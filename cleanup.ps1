#Cleanup dla wszystkich userów
Get-ChildItem 'C:\Users\*\Downloads\*' | 
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem 'C:\Users\*\Documents\*' | 
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem 'C:\Users\*\AppData\Local\Google\Chrome\User Data\Default\History' | 
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem 'C:\Users\*\AppData\Local\Google\Chrome\User Data\Default\Cache' | 
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem 'C:\Users\*\AppData\Local\Google\Chrome\User Data\Default\Top Sites' | 
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem 'C:\Users\*\AppData\Local\Google\Chrome\User Data\Default\Sessions' | 
    Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

#Status aktywacji
$activationStatus = slmgr /xpr
Write-Host "Status aktywacji: $activationStatus"

#Wyczyszczenie konsoli
cls
echo "-------------------------------------------"

#Sterowniki i BIOS
echo "Sterownik karty graficznej"
Get-WmiObject Win32_VideoController | format-table Name, DriverVersion, DriverDate
echo "-------------------------------------------"
echo "Wersja BIOSu"
Get-WmiObject -Class Win32_BIOS | format-table Name