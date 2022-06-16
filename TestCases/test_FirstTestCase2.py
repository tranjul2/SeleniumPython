from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    # TestCase(https://www.thetestingworld.com/testings/)
    # Step 1: Open Browser
    path = "C:\\Users\\Cryst\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)

    # Step 2: Enter URL
    driver.get("http://www.theTestingWorld.com/testings")

    # Step 3: Maximize browser
    driver.maximize_window()

    yield
    # Step 9: Close Browser
    driver.close()



def test_verify_registration(environment_setup):


    # Step 4: Enter Data into textbox
    driver.find_element_by_name("fld_username").send_keys("helloworld")
    driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("testingworldusa@gmail.com")
    driver.find_element_by_name("fld_password").send_keys("abcd1234")
    driver.find_element_by_name("fld_cpassword").send_keys("abcd123")
    driver.find_element_by_name("fld_username").clear()
    driver.find_element_by_name("fld_username").send_keys("abc1234")

    # Step 5: Click on radio button
    #driver.find_element_by_xpath("//input[@value='home']").click()
    driver.find_element_by_xpath("//input[@value='office']").click()

    # Work on Dropdown
    obj = Select(driver.find_element_by_name("sex"))
    #obj.select_by_index(2)
    #obj.select_by_value("2")
    obj.select_by_visible_text("Male")


    # Step 6: Click on Checkbox
    driver.find_element_by_name("terms").click()

    # Step 7: Click on button
    #driver.find_element_by_xpath("//input[@type='submit']").click()

    # Step 8: Click on link
    #driver.find_element_by_link_text("Read Detail").click()

    assert driver.current_url == "https://www.thetestingworld.com/testings/"




