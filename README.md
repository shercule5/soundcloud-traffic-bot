# soundcloud-traffic-bot
SoundCloud Traffic Bot (Stealth Listener) This project simulates real human traffic to SoundCloud tracks using a stealth Chrome automation setup. It runs indefinitely, rotating between multiple SoundCloud track URLs and emulating mobile devices to mimic real listener behavior.
# 🎧 SoundCloud Traffic Bot (Stealth Listener)

This project simulates real human traffic to SoundCloud tracks using a stealth Chrome automation setup.  
It rotates through a list of your SoundCloud track URLs, plays each one using a mobile browser emulation, and runs forever until manually stopped.

---

## ✅ Features

- 🎵 Auto-play multiple SoundCloud tracks
- 📱 Mobile browser emulation (iPhone user-agent)
- 🕶️ Headless + incognito mode for stealth
- ⏱️ Randomized play time (35–70 seconds)
- 🔁 Cooldown between plays (15–45 seconds)
- ♾️ Runs non-stop until you close it

---

## 📂 Setup Instructions

### Requirements

- Python 3.10+ installed
- Chrome browser installed
- Matching [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) in the same folder
- Install Selenium:
  ```bash
  pip install selenium

To change which tracks are played, open trafficbot.py and edit the list:

track_urls = [
    "https://soundcloud.com/yourname/track-1",
    "https://soundcloud.com/yourname/track-2"
]
