import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
import allure
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.index_page import IndexPage
from pages.main_page import MainPage



def pytest_addoption(parser):
    parser.addoption('--browsername', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")  # browser selection

    parser.addoption('--browsermode', action='store', default='start-maximized',  # Browser mode selection
                     help="--headless mode")

@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def get_edge_options():
    options = webdriver.EdgeOptions()
    options.add_argument('edge')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options, request, get_edge_options):
    driver_name = request.config.getoption('browsername')
    driver_mode = request.config.getoption('browsermode')
    driver = None
    if driver_name == 'chrome':

        options = get_chrome_options
        options.add_argument(driver_mode)
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        return driver

    elif driver_name == 'edge':
        options = get_edge_options
        options.add_argument(driver_mode)
        driver = webdriver.Edge((EdgeChromiumDriverManager().install()), options=options)
        return driver





@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    url = 'https://www.saucedemo.com'
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture
def index_page(setup):
    yield IndexPage(setup)

@pytest.fixture()
def main_page(setup):
    yield MainPage(setup)














# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#     marker = item.get_closest_marker("ui")
#     if marker:
#         if rep.when == "call" and rep.failed:
#             try:
#                 allure.attach(item.instance.driver.get_screenshot_as_png(),
#                               name=item.name,
#                               attachment_type=allure.attachment_type.PNG)
#             except Exception as e:
#                 print(e)