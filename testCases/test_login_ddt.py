import pytest
from selenium import webdriver
from Utilities.read_Properties import ReadConfig  #To receive data from readproperties file
from pageObjects.LoginPage import Login
from Utilities.customLogger import LogGen   #To access LogGen method from customLogger
from Utilities import ExcelUtility


class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURl()
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.loggen()      #To store logger value in a variable from the customLogger file


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("*********Test002 DDT Login*******")
        self.logger.info("********Verifying Login test**********")
        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp=Login(self.driver)

        self.rows=ExcelUtility.getRowCount(self.path,'Sheet1')
        print("No of rows in excel",self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=ExcelUtility.readData(self.path,'Sheet1',r,1)
            self.password =ExcelUtility.readData(self.path, 'Sheet1', r, 2)
            self.exp= ExcelUtility.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.clickcountinue()
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_title=self.driver.title
            exp_title="Amazon Sign In"

            if act_title==exp_title :
                if self.exp=="Pass":
                    self.logger.info("*****Test is passed****")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*****Test is Fail****")
                    self.lp.clickLogout();
                    lst_status.append("Fail")







