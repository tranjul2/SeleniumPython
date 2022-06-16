from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# Step 1: Open Browser
path="C:\\Users\\Cryst\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)

# Step 2: Enter URL
driver.get("http://www.theTestingWorld.com/")

# Step 3: Maximize browser
driver.maximize_window()

act = ActionChains(driver)

# Click operation
#act.click().perform()
#act.click(driver.find_element_by_xpath("//a[text()='Quick Demo']")).perform()

# Context Click (Right Click)
#act.context_click().perform()
#act.context_click(driver.find_element_by_xpath("//a[text()='Quick Demo']")).perform()

#act.double_click().perform()
#act.double_click(driver.find_element_by_xpath("//a[text()='Quick Demo']")).perform()

act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()

