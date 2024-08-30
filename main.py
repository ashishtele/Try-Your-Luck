from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

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


def book_DMV():
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(options=chr_options)

    # Set the URL of the CT DMV road test scheduling page
    url = "https://www.dmvroadtest.ct.gov/dmv/do-it-online/Scheduling/RescheduleAppointment"

    # Set the PIN for the existing appointment
    pin = "1234"

    # Set the desired location
    location = "Hamden Office, 1965 State Street, Hamden, CT 06517"

    # Set the desired time slot
    time_slot = "12:15 pm"

    # Set the refresh interval in seconds (15 minutes)
    refresh_interval = 900

    #driver = webdriver.Chrome(ChromeDriverManager().install())

    # Wait for the page to load
    chr_driver.implicitly_wait(10)

    # Open the CT DMV road test scheduling page
    chr_driver.get(url)

    # Click the "Reschedule Appointment" button
    reschedule_button = chr_driver.find_element(By.XPATH, "//a[contains(text(), 'Reschedule Appointment')]")
    reschedule_button.click()

    # Enter the PIN and click the "Submit" button
    pin_input = chr_driver.find_element(By.ID, "Pin")
    pin_input.send_keys(pin)
    submit_button = chr_driver.find_element(By.XPATH, "//input[@value='Submit']")
    submit_button.click()


    # Wait for the appointment details to load
    WebDriverWait(chr_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped']")))

    # Click the "Reschedule" button
    reschedule_button = chr_driver.find_element(By.XPATH, "//input[@value='Reschedule']")
    reschedule_button.click()

    # Select the desired location from the dropdown
    location_dropdown = Select(chr_driver.find_element(By.ID, "ddlLocation"))
    location_dropdown.select_by_visible_text(location)

    # Wait for the available slots to load
    WebDriverWait(chr_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped']")))

    # Continuously check for the desired time slot
    while True:
        # Refresh the available slots
        refresh_button = chr_driver.find_element(By.ID, "btnRefresh")
        refresh_button.click()

        # Wait for the available slots to load
        WebDriverWait(chr_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped']")))

        # Check if the desired time slot is available
        time_slots = chr_driver.find_elements(By.XPATH, "//table[@class='table table-striped']//td[1]")
        available_slots = chr_driver.find_elements(By.XPATH, "//table[@class='table table-striped']//td[2]")

        for i in range(len(time_slots)):
            if time_slots[i].text == time_slot and available_slots[i].text != "0 spots":
                # Select the desired time slot
                time_slot_radio = chr_driver.find_element(By.XPATH, f"//label[contains(text(), '{time_slot}')]/preceding-sibling::input")
                time_slot_radio.click()

                # Click the "Continue" button
                continue_button = chr_driver.find_element(By.XPATH, "//input[@value='Continue']")
                continue_button.click()

                # You can add further steps here to finalize the appointment

                # Exit the loop
                break

        # Wait for the refresh interval
        time.sleep(refresh_interval)

#browser_function()
book_DMV()

# Close the browser
# driver.quit()