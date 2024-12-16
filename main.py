from screenshot_handler import capture_screenshot, crop_images
from comparison_tool import decide_best_option
from adb_handler import adb_tap
import json

def main():
    # Load configuration
    with open("config.json", "r") as f:
        config = json.load(f)
    
    # Step 1: Take and Crop Screenshots
    capture_screenshot("screen.png")
    crop_images("screen.png", config["crop_coordinates"])
    
    # Step 2: Compare and Decide Best Option
    best_option = decide_best_option(config["options"])
    print(f"Best Option: {best_option}")
    
    # Step 3: Automate Tap
    adb_tap(*config["tap_coordinates"][best_option])
    print("Task Complete!")

if __name__ == "__main__":
    main()
