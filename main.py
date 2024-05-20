from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# https://stackoverflow.com/questions/47508518/google-chrome-closes-immediately-after-being-launched-with-selenium
def browser_function():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(options=chr_options)
    chr_driver.get("https://www.talktostopandshop.com")

    # Wait for the page to load
    chr_driver.implicitly_wait(10)

    pin_input = chr_driver.find_element(By.ID, "QR~QID277") 

    # Enter the PIN
    # Remove spaces before entering
    pin_input.send_keys("XXXxxxXXX")

    next_button = chr_driver.find_element(By.XPATH, "//button[@class='NextButton Button']")

    # Click on the "Next" button
    next_button.click()



browser_function()


# Close the browser
# driver.quit()