
from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(r"C:\Users\Kushal Raju\Downloads\chromedriver_win32\chromedriver.exe")

    elif browser=='firefox':
        driver=webdriver.Firefox()
    return driver

def pytest_addoption(parser):          #This will get value from command line called as hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):                  #This will return browser value to setup method
    return request.config.getoption("--browser")

######pytest HTML reports##########
def pytest_configure(config):
    config._metadata['Project Name'] = 'Amazon Framework'  #hook for adding environment info to HTML Report
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Kushal'

@pytest.mark.optionalhook
def pytest_metdata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
