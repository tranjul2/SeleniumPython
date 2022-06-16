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

# Fetching Title
print("Title of page is " + driver.title)

# Fetch URL of Page
print("Page URL is " + driver.current_url)


# Fetch Complete Page HTML
print("*****************************************************************************************************")
print(driver.page_source)

print("********************************************************************************************************")