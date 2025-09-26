from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_instagram_follow_count(username):
    # Set up the WebDriver (this will automatically manage your ChromeDriver)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Go to the Instagram profile page
    driver.get(f'https://www.instagram.com/{username}/')

    # Wait for the page to load completely (adjust the time if needed)
    time.sleep(3)

    try:
        # Find the number of followers, following, and posts by using class names
        followers = driver.find_element(By.XPATH, "//a[contains(@href, '/followers')]/span").text
        following = driver.find_element(By.XPATH, "//a[contains(@href, '/following')]/span").text
        posts = driver.find_element(By.XPATH, "//span[contains(@class, 'g47SY')]").text

        print(f"Instagram Profile: {username}")
        print(f"Followers: {followers}")
        print(f"Following: {following}")
        print(f"Posts: {posts}")
        
    except Exception as e:
        print("Error while fetching data:", e)
    
    # Close the browser after scraping
    driver.quit()

# Example usage
username = 'instagram'  # Replace with the desired username
get_instagram_follow_count(username)
