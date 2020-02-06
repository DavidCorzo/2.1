import subprocess, sys, time, os

if __name__ == "__main__":
    path = os.getcwd() + "\\autogit.ps1" 
    path = path.replace("\\","/")
    print(f"==========> {path}")
    p = subprocess.Popen(["powershell.exe", path], stdout=sys.stdout)
    p.communicate()
    print("Done?")
    time.sleep(5)
