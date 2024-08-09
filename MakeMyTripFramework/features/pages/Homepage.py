import time

from features.pages.BasePage import BasePage


class Homepage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    departure_button_xpath = "//div[@class='searchWidgetContainer']//div[@class='fsw ']/div[@class='fsw_inner returnPersuasion']//div[@class='flt_fsw_inputBox dates inactiveWidget ']//label[@for='departure']"
    left_calender_header_xpath = "(//div[@class='DayPicker-Caption'])[2]"
    right_calender_header_xpath = "(//div[@class='DayPicker-Caption'])[2]"
    calenderelementsDic = {
        "left_calender_header_xpath": "(//div[@class='DayPicker-Caption'])[2]",
        "right_calender_header_xpath": "(//div[@class='DayPicker-Caption'])[2]",
        "departure_button_id" : "departure",
        "calendernextbutton_xpath" : "//span[@class='DayPicker-NavButton DayPicker-NavButton--next']",



    }

    def mmtCalenderInteract(self,monthdate):
        self.mmtCalender(monthdate)
        time.sleep(10)



    def clickoncalender(self):

        self.clickOnElement("departure_button_xpath", self.departure_button_xpath)
        #time.sleep()
