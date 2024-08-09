import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.Homepage import Homepage
from features.pages.LoginPage import Login


@given('launch chrome browser')
def launchBrowser(context):
    context.logi = Login(context.driver)
    context.logi.loginpage()

@when('user verify the Title of the Page "{title}"')
def verifythetitle(context, title):
    context.logi.verifythePageTitle(title)

@when(u'click on departure date')
def clickondeparture(context):
    context.homepage = Homepage(context.driver)
    context.homepage.clickoncalender()



@when(u'enter the date "{date}"')
def handlemmtcalender(context, date):

    context.homepage.mmtCalenderInteract(date)





