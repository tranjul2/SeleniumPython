import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Open Browser
path="C:\\Users\\Cryst\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)

# Step 2: Enter URL
driver.get("http://www.theTestingWorld.com/testings")

# Step 3: Maximize browser
driver.maximize_window()

driver.find_element_by_name("fld_username").send_keys("Hello")

act = ActionChains(driver)
#act.send_keys(Keys.TAB).perform()
#act.key_down(Keys.CONTROL).send_keys('a').perform()
act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()
time.sleep(10)