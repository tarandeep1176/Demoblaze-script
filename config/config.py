import os
import allure
import time
from Libraries.Libraries import Import_libraries


SCREENSHOT_DIR = "screenshots"

def take_screenshot(name="Screenshot"):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    driver = Import_libraries.get_driver()

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    file_path = f"{SCREENSHOT_DIR}/{name}_{timestamp}.png"

    driver.save_screenshot(file_path)

    allure.attach.file(
        file_path,
        name=name,
        attachment_type=allure.attachment_type.PNG
    )
    return file_path
