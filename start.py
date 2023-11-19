import subprocess
import time

if __name__ == "__main__":
    print("Starting Model Service")
    subprocess.Popen("runModel.bat")
    time.sleep(5)
    print("=" * 80)
    subprocess.Popen("runAdmin.bat")
