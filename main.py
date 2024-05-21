from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # pin_input = WebDriverWait(chr_driver, 10).until(
    #    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Please enter your PIN to take the survey.']")))

    pin_input.send_keys("xxxxxxxx")

    # Click Next
    next_button = chr_driver.find_element(By.XPATH, "//button[text()='Next']")
    next_button.click()

    # Rate overall satisfaction (replace with your desired rating)
    satisfaction_rating = WebDriverWait(chr_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Very satisfied']"))
    )
    satisfaction_rating.click()

    # Click Next
    next_button = chr_driver.find_element(By.XPATH, "//button[text()='Next']")
    next_button.click()

    # Rate likelihood to recommend (replace with your desired rating)
    recommendation_rating = WebDriverWait(chr_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='8']"))
    )
    recommendation_rating.click()

    # Click Next
    next_button = chr_driver.find_element(By.XPATH, "//button[text()='Next']")
    next_button.click()

    # Enter feedback (replace with your feedback)
    feedback_input = WebDriverWait(chr_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea"))
    )
    feedback_input.send_keys("You guys are great")

    # Click Next
    next_button = chr_driver.find_element(By.XPATH, "//button[text()='Next']")
    next_button.click()

    # Rate specific aspects (replace with your desired ratings)
    # Example for Store Cleanliness:
    cleanliness_rating = WebDriverWait(chr_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Very satisfied']/preceding-sibling::input[@type='radio']"))
    )
    cleanliness_rating.click()

    # Repeat for other aspects...

    # Click Next
    next_button = chr_driver.find_element(By.XPATH, "//button[text()='Next']")
    next_button.click()

    # Enter additional feedback (replace with your feedback)
    additional_feedback_input = WebDriverWait(chr_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea"))
    )
    additional_feedback_input.send_keys("Bring more items that are fresh")

    # Click Next
    next_button = chr_driver.find_element(By.XPATH, "//button[text()='Next']")
    next_button.click()

    # Enter staff feedback (optional, replace with your feedback)
    staff_feedback_input = WebDriverWait(chr_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea"))
    )
    staff_feedback_input.send_keys("The cashier was very friendly and helpful.")

    # Click Next
    next_button = chr_driver.find_element(By.XPATH, "//button[text()='Next']")
    next_button.click()

    # Close the browser
    # chr_driver.quit()



browser_function()


# Close the browser
# driver.quit()