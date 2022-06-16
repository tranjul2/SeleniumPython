from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

# TestCase(https://www.thetestingworld.com/testings/)
# Step 1: Open Browser
path="C:\\Users\\Cryst\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)

# Step 2: Enter URL
driver.get("http://www.theTestingWorld.com/testings")

# Step 3: Maximize browser
driver.maximize_window()

# Fetching Element Text
print("Text on Link is : " + driver.find_element_by_class_name("displayPopup").text)

# Fetching attribute value of Element
print("Value of Button is " + driver.find_element_by_xpath(("//input[@type='submit']")).get_attribute("value"))


