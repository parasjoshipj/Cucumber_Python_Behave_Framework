import allure
from allure_commons.types import AttachmentType
#from behave_reportportal.behave_agent import create_rp_service, BehaveAgent
#from behave_reportportal.config import read_config
from selenium import webdriver

from Utilities import configReader
from allure_behave.hooks import allure_report

#allure_report("allure")

def before_scenario(context, driver):
    browser_name = configReader.readConfig("info basic", "browser")

    if browser_name.__eq__("chrome"):

        context.driver = webdriver.Chrome("webdriver/chromedriver.exe")
        #   driver.implicitly_wait(10)
        context.driver.implicitly_wait(10)
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(configReader.readConfig("info basic", "url"))


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context,step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="failed_screenshot"
                      ,attachment_type=AttachmentType.PNG)


