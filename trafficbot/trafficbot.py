from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import random

# List of SoundCloud tracks to rotate through
track_urls = [
    "https://soundcloud.com/schymoney/schyslust-worldwide",
    "https://soundcloud.com/schymoney/schyslust-antisocial",
    "https://soundcloud.com/schymoney/schyslust-off-1",
    "https://soundcloud.com/schymoney/thats-alright"
]

driver_path = "chromedriver.exe"

options = Options()
options.add_argument("--incognito")
options.add_argument("--mute-audio")
options.add_argument("--headless")

mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
}
options.add_experimental_option("mobileEmulation", mobile_emulation)

service = Service(driver_path)
play_count = 0

# Loop through tracks forever
while True:
    url = random.choice(track_urls)
    play_count += 1
    print(f"Play #{play_count}: {url}")

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        listen_time = random.randint(35, 70)
        print(f"Listening for {listen_time} seconds...")
        time.sleep(listen_time)
        driver.quit()
        cooldown = random.randint(15, 45)
        print(f"Cooldown for {cooldown} seconds...\n")
        time.sleep(cooldown)

    except Exception as e:
        print(f"Error during play #{play_count}: {e}")
        try:
            driver.quit()
        except:
            pass
        print("Retrying after 60 seconds...")
        time.sleep(60)