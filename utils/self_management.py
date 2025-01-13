import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def handle_self_management(driver):
    self_management = {
        "1": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]",
        "2": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[2]",
        "3": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[3]",
        "4": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[4]",
        "5": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[2]/div[5]",
    }

    self_management_audio = {
        "audio1": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/button[1]",
        "audio2": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/button[2]",
        "audio3": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/button[3]",
        "audio4": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/button[4]",
        "audio5": "/html[1]/body[1]/app-root[1]/app-main-layout[1]/main[1]/app-home[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/button[5]",
    }

    # Select a random self-management option
    random_self_management = random.choice(list(self_management.values()))

    # Wait for the element to be clickable
    self_management_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, random_self_management))
    )

    # Hover over the element
    actions = ActionChains(driver)
    actions.move_to_element(self_management_element).perform()

    time.sleep(2)  # Wait for hover effect

    # Attempt to click the element
    try:
        self_management_element.click()
    except Exception as e:
        print(f"Error clicking element: {str(e)}")
        driver.execute_script("arguments[0].click();", self_management_element)

    time.sleep(2)

    # Check the selected option and trigger the corresponding audio
    for key, value in self_management.items():
        if random_self_management == value:
            audio_key = f"audio{key}"
            try:
                # Wait for audio button to be clickable
                audio_element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self_management_audio[audio_key]))
                )
                # Click the audio button
                audio_element.click()
            except Exception as e:
                print(f"Error clicking audio element: {str(e)}")
                # If regular click fails, use JavaScript click
                audio_element = driver.find_element(By.XPATH, self_management_audio[audio_key])
                driver.execute_script("arguments[0].click();", audio_element)
            break

    time.sleep(4)
