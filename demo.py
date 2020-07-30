from selenium import webdriver

if __name__ == '__main__':
    print('Web Scrapping Applicatin Started!')
    chromedriver_path = r"D:\Work\Webscrapper\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver_path)
    driver.maximize_window()
    driver.get("https://www.google.com")

    print(driver.title)

    driver.close()
    # print("Web Scrapping Application Completed!")