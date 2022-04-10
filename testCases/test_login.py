import pytest
from selenium import webdriver
from Utilities.read_Properties import ReadConfig  #To receive data from readproperties file
from pageObjects.LoginPage import Login
from Utilities.customLogger import LogGen   #To access LogGen method from customLogger


class Test_001_Login:
    baseURL=ReadConfig.getApplicationURl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPasssword()

    logger=LogGen.loggen()      #To store logger value in a variable from the customLogger file

    @pytest.mark.regression
    def test_homePageTitle(self,setup):

       self.logger.info("*****************Test_001_Login*****************")
       self.logger.info("*****************verifying home page title*********************")


       self.driver=setup
       self.driver.get(self.baseURL)
       act_title=self.driver.title

       if act_title=="Amazon Sign In":
           assert True
           self.driver.close()
           self.logger.info("********Home Page Title test is passed********")
       else:
           self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
           self.driver.close()
           self.logger.error("********Home Page Title test is Failed********")
           assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("********Verifying Login test**********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.clickcountinue()
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Amazon Sign In":
            assert True
            self.logger.info("********Login test is passed********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("********Login test is Failed********")
            assert False