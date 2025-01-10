from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


file_path = "/Users/tuanadurmus/Desktop/Tiktok Kasım 2024.txt"

tiktok_data = []

with open(file_path, "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 1):  # Process two lines at a time (Date & Link)
        if i + 1 < len(lines):
            date_line = lines[i].strip()
            link_line = lines[i + 1].strip()
            
            if date_line.startswith("Date:") and link_line.startswith("Link:"):
                date = date_line.replace("Date: ", "").strip()
                url = link_line.replace("Link: ", "").strip()
                tiktok_data.append({"date": date, "url": url})




def get_tiktok_hashtags(video_url):
    """Extract hashtags from a TikTok video using Selenium."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(video_url)
        wait = WebDriverWait(driver,10)  # Allow content to load

        # Extract hashtags from the video description
        hashtags_elements = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//strong[contains(text(), '#')]"))
        )
        hashtags = [element.text for element in hashtags_elements]
    
    except Exception as e:
        hashtags = f"Error: {e}"
    
    driver.quit()
    return hashtags if hashtags else "No hashtags found"

# Process each TikTok video
results = []
for data in tiktok_data:
    date, url = data["date"], data["url"]
    hashtags = get_tiktok_hashtags(url)
    results.append({"date": date, "url": url, "hashtags": hashtags})
    time.sleep(2)  # Avoid rate limiting

# Display results
df = pd.DataFrame(results)

# Display results
print(df)

# Optionally, save to a CSV file
df.to_csv("tiktok_hashtags.csv", index=False)
print("Results saved to tiktok_hashtags.csv")

