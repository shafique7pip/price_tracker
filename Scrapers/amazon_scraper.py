from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_amazon_price(url):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Setup the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # Open the URL
    driver.get(url)
    
    try:
        # Extract the product title
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'productTitle'))
        )
        title = title_element.text.strip()
        
        # Extract the price using JavaScript
        price_script = "return document.querySelector('span.a-price-whole') ? document.querySelector('span.a-price-whole').innerText : 'Price not found';"
        price = driver.execute_script(price_script)
        
        return title, price
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Title not found", "Price not found"
    
    finally:
        driver.quit()

# Example usage
url = 'https://www.amazon.com/dp/B09F3P3DQD'
product_name, product_price = get_amazon_price(url)
print(f"Product: {product_name}, \nPrice: {product_price}")