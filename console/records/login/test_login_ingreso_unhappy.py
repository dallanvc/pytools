# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestLoginingresoHappy():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def test_loginingresoHappy(self):
    # Test name: Login ingreso Happy
    # Step # | name | target | value
    # 1 | open | https://atlanticcity.pre.tecnalis.com/ |
    self.driver.get("https://atlantic:viQ[3UJ*Rk*Q1zC@atlanticcity.pre.tecnalis.com/")
    # wait = WebDriverWait(self.driver, 10)
    # alert = wait.until(EC.alert_is_present())

    # Enter the username and password
    # alert.send_keys("atlantic")
    # alert.send_keys("\t")  # Tab to the password field
    # alert.send_keys("viQ[3UJ*Rk*Q1zC")

    # Accept the alert
    # alert.accept()
    #time.sleep(1)
    # 2 | setWindowSize | 1065x817 | 
    self.driver.maximize_window()
    # 3 | click | css=.d-xl-block > .btn-casino |
    header = self.driver.find_element(By.CSS_SELECTOR, "header")
    buttons = header.find_elements(By.CSS_SELECTOR, "a")
    for button in buttons:
      if button.text == "INGRESAR":
        button.click()
        time.sleep(5)
    # self.driver.find_element(By.CSS_SELECTOR, ".d-xl-block > .btn-casino").click()
    # 4 click to casino online
    wait = WebDriverWait(self.driver, 60)
    target_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cardDondeVamosCasino > button")))
    target_button.click()
    #time.sleep(10)
    # 5 | type | id=username_aside | Testjordan01
    self.driver.find_element(By.ID, "username_aside").send_keys("Testordan01")
    self.driver.find_element(By.ID, "password_aside").send_keys("Testordan01")
    time.sleep(2)
    # 6| click | linkText=INGRESAR |
    self.driver.find_element(By.ID, "login_button_aside").click()
    time.sleep(10)

    #self.driver.find_element(By.ID, "").click()


  #BOTON promocion verano



  ##probar codigo



  
test_login_ingreso_happy = TestLoginingresoHappy()