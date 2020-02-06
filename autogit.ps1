$path = Get-Location
Write-Host $("CWD ======> {0}" -f $path)
Resolve-Path -LiteralPath 'D:\one\one'
Write-Host "======> Initialize! dgcm "
[string] $date = Get-Date -Format " dddd yyyy-MM-dd HH-mm-ss K"
$date = $date.Replace("(:)", "-")
Write-Host $("{0}" -f $date)
[string] $Message = $( Read-Host "Input commit message ") 
Write-Host ("=====> {0} ==> {1}" -f $date, $Message)
powershell.exe /c "git init"
Write-Host "=====> git init"
powershell.exe /c "git pull"
Write-Host "=====> git pull"
powershell.exe /c "git add ."
Write-Host "=====> git add ."
powershell.exe /c "git status"
Write-Host "=====> git status"
powershell.exe /c "git remote -v"
Write-Host "=====> git remote -v"
powershell.exe /c ('git commit -m "{0}  {1}"' -f $date, $Message)
Write-Host ('=====> git commit -m "{0}  {1}"' -f $date, $Message)
powershell.exe /c "git push origin master"
Write-Host "=====> git push origin master"


