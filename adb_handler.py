import subprocess

def adb_tap(x, y):
    subprocess.run(f"adb shell input tap {x} {y}", shell=True)
    print(f"Tapped at coordinates: ({x}, {y})")
