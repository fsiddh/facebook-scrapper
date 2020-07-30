import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def get_credentials():
    config_data = None
    with open('readme.json') as json_file:
        config_data = json.load(json_file)
    return config_data['facebook']       


if __name__ == "__main__":
    print("Web Scrapping Application Started ...")
    chromedriver_path = r"D:\Work\Webscrapper\chromedriver.exe"
    driver_obj = webdriver.Chrome(chromedriver_path)
    driver_obj.maximize_window()
    driver_obj.get("https://www.facebook.com")
    user_detail = get_user_name_password()

    username_element = driver_obj.find_element_by_id("email")
    password_element = driver_obj.find_element_by_id("pass")
    submit_btn_element = driver_obj.find_element_by_id("loginbutton")

    username_element.send_keys(user_detail["user_name"])
    password_element.send_keys(user_detail["password"])
    submit_btn_element.click()
    wait = WebDriverWait(driver_obj, 5)

