from PIL import Image
import subprocess

def capture_screenshot(output="screen.png"):
    subprocess.run("adb shell screencap -p /sdcard/screen.png", shell=True)
    subprocess.run(f"adb pull /sdcard/screen.png {output}", shell=True)
    print("Screenshot captured.")

def crop_images(image_path, crop_coordinates):
    image = Image.open(image_path)
    for name, coords in crop_coordinates.items():
        cropped = image.crop(coords)
        cropped.save(f"{name}.png")
    print("Images cropped successfully.")
