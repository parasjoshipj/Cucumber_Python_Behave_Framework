import time

from features.pages.BasePage import BasePage


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    closeIcon_xpath = "//span[@class='commonModal__close']"
    loginButton_xpath = "//span[text()='Log in']"
    mailIconButton_xpath = "//span[text()='Email']"
    emailTextBox_id = "email"
    nextButton_xpath = "//span[text()='Next']"
    maybelaterButton_xpath = "//button[text()='Maybe later']"



    def loginpage(self):
        self.clickOnElement("closeIcon_xpath", self.closeIcon_xpath)
        #time.sleep(10)

    def verifythePageTitle(self, title):
        self.verifyTitle(title)



















