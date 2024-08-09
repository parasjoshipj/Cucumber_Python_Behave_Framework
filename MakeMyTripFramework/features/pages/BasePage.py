import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Utilities import configReader
from Utilities.generatingLogs import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def clickOnElement(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        #element.click()
        self.driver.execute_script("arguments[0].click();", element)
        log.logger.info("Clicking on an element: " + str(element))

    def clickOnElementJS(self, element):
        self.driver.execute_script("arguments[0].click();", element)
        log.logger.info("Clicking on an element: " + str(element))

    def verifyTitle(self,expected_title):
        getstr = self.driver.title
        assert getstr == expected_title
        #return getstr.__eq__(expected_title)


    def setText(self,locator_type, locator_value,text_to_entered):
        element = self.get_element(locator_type, locator_value)
        #element.click()
        #element.clear()
        element.send_keys(text_to_entered)
        log.logger.info("Typing in an element: " + str(element) + " value entered as : " + str(text_to_entered))

    def get_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def elementContains(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__contains__(expected_text)

    def element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(expected_text)

    def return_and_status(self,privacy_status,first_name_status,last_name_status,email_status,telephone_status,password_status):
        if privacy_status and first_name_status and last_name_status and email_status and telephone_status and password_status:
            return True
        else:
            return False

    def isDisplay(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()

    def mmtCalender(self,datevalue):
        splitdatevalue = datevalue.split(maxsplit=1)
        date = splitdatevalue[0]
        monthandyear = splitdatevalue[1]
        leftsideheader = self.driver.find_element(By.XPATH,"(//div[@class='DayPicker-Caption'])[1]")
        rightsideheader = self.driver.find_element(By.XPATH,"(//div[@class='DayPicker-Caption'])[2]")
        leftdateelement = self.driver.find_element(By.XPATH,"(//div[@class='DayPicker-Month'])[1]//div[@class='DayPicker-Body']//p[1][text()='"+date+"']")
        rightdateelement = self.driver.find_element(By.XPATH,"(//div[@class='DayPicker-Month'])[2]//div[@class='DayPicker-Body']//div[@class='dateInnerCell']/p[text()='"+date+"']")
        calendernextbutton = self.driver.find_element(By.XPATH,"//span[@class='DayPicker-NavButton DayPicker-NavButton--next']")
        leftsideheadervalue = leftsideheader.text
        rightsideheadervalue = rightsideheader.text
        while True :

            if leftsideheadervalue == monthandyear:
                self.driver.find_element(By.XPATH, "(//div[@class='DayPicker-Month'])[1]//div[@class='DayPicker-Body']//p[1][text()='"+date+"']").click()
                break

            else:

                print(calendernextbutton.is_displayed())
                if calendernextbutton.is_displayed():
                    self.clickOnElementJS(calendernextbutton)
                    leftsideheadervalue = leftsideheader.text
                    rightsideheadervalue = rightsideheader.text
                    print(leftsideheadervalue, rightsideheadervalue)



                elif rightsideheadervalue == monthandyear:

                    print("latest value matched")
                    time.sleep(6)
                    self.driver.find_element(By.XPATH, "(//div[@class='DayPicker-Month'])[2]//div[@class='DayPicker-Body']//div[@class='dateInnerCell']/p[text()='"+date+"']").click()
                    #self.clickOnElementJS(rightdateelement)
                    break

                else :
                    print("Wrong date sent")




















