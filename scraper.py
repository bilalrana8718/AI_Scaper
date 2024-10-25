import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup



def scrape_website(website):
    # Replace 'YOUR_CHROMEDRIVER_PATH' with the actual path to your ChromeDriver executable

    chrome_driver_path = 'chromedriver.exe'
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        html = driver.page_source
        time.sleep(10)

        return html
    except webdriver.WebDriverException as e:
        print(f"Error: {e}")
        return None
    
def extract_body(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(['script' , 'style']):
        script_or_style.extract()

    cleaned_body = soup.get_text(separator='\n')
    # print(cleaned_body, "before splitting")
    cleaned_body = '\n'.join(line.strip() for line in cleaned_body.splitlines() if line.strip())
    # print(cleaned_body, "before splitting")

    return cleaned_body

def split_dom(dom_content, max_length=6000):
    return [
        dom_content[i:i+max_length]
        for i in range(0, len(dom_content), max_length)
    ]
