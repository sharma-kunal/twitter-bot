from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
import time


# Function to LOGIN to Twitter with the given E-Mail ID and PASSWORD
def log_in(email_id, id_password):
    email = browser.find_element_by_css_selector('.js-username-field')
    email.send_keys(email_id)

    password = browser.find_element_by_css_selector('.js-password-field')
    password.send_keys(id_password)
    password.submit()
    time.sleep(1)


def timeout(xpath):
    try:
        WebDriverWait(browser, delay).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    except TimeoutException as ex:
        print(str(ex))
        browser.close()


if __name__ == "__main__":
    delay = 10
    tweet_link = input("Please Enter Tweet Link: ")

    # Either you can use the given ID and PASSWORD for testing purposes or may give the
    # input for your ID and PASSWORD by uncommenting the lines 38 and 39.

    email_id = "kuunaalsharma88@gmail.com"
    id_password = "SeekNDestroy@twitter"

    # email_id = input("Please Enter the mail id: ")
    # id_password = input("Please Enter the password: ")

    browser = webdriver.Firefox()
    browser.get('https://twitter.com/login')

    # LOGGING IN
    try:
        log_in(email_id, id_password)
    except WebDriverException:
        browser.get('https://twitter.com/login')
        log_in(email_id, id_password)

    # Getting to the provided tweet link
    browser.get(tweet_link)
    timeout("//div[@data-testid='DashButton_ProfileIcon_Link']")

    # Getting the username of user
    name = browser.find_element_by_xpath("//div[@data-testid='DashButton_ProfileIcon_Link']")
    n = list(name.get_attribute('aria-label').strip().split())
    user_name = n[-1]

    # Replying to the tweet as given in the file having file name `tweet_reply.txt`.
    timeout("//div[@aria-label='Reply' and @role='button']")
    x = browser.find_element_by_xpath("//div[@aria-label='Reply' and @role='button']")
    webdriver.ActionChains(browser).move_to_element(x).click(x).perform()

    file = open('tweet_reply.txt', 'r')
    timeout("//div[@role='textbox']")
    text_box = browser.find_element_by_xpath("//div[@role='textbox']")
    text_box.send_keys("@" + str(user_name) + " ")
    for line in file:
        text_box.send_keys(line)
    timeout("//div[@role='button' and @data-testid='tweetButton']")

    # Submitting the reply
    x = browser.find_element_by_xpath("//div[@role='button' and @data-testid='tweetButton']")
    webdriver.ActionChains(browser).move_to_element(x).click(x).perform()
