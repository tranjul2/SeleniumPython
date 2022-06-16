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

# Work on Dropdown
obj = Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text("Male")

# Fetch Selected option
print(obj.first_selected_option.text)

# Fetch All options
print("*****************************************************")
for op in obj.options:
    print(op.text)