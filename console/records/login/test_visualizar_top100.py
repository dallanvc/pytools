# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.common import InvalidSelectorException, NoSuchElementException
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
    self.driver.find_element(By.ID, "username_aside").send_keys("Testjordan01")
    self.driver.find_element(By.ID, "password_aside").send_keys("Testjordan01")
    time.sleep(2)
    # 6| click | linkText=INGRESAR |
    self.driver.find_element(By.ID, "login_button_aside").click()
    time.sleep(10)
    self.driver.find_element(By.ID, "contentModalPlayerOculto").click()
    # 7 | type | id=idAliraCampo | 850
    self.driver.find_element(By.ID, "idAliraCampo").send_keys("850")
    # 8 | click | css=button:nth-child(4) |
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
    # 9 | mouseOver | css=.item-prev > button |
    flag_modal = False
    flag_modal_2 = False

    try:
      wait=WebDriverWait(driver=self.driver, timeout=10)
      modal=wait.until(EC.visibility_of_element_located((By.ID, "formEliminarBono")))
      modal.find_element(By.LINK_TEXT, "ACTIVAR LUEGO").click()
      flag_modal = True

      wait = WebDriverWait(driver=self.driver, timeout=10)
      modal = wait.until(EC.visibility_of_element_located((By.ID, "popupContent")))

      flag_modal_2 = True
      links = modal.find_elements(By.CSS_SELECTOR, "a")
      for link in links:
        if link.text == "ENTENDIDO":
          link.click()
          time.sleep(10)



    except (Exception, NoSuchElementException) as e:
      # Bajar cursor
      self.driver.execute_script("window.scrollTo(0,600)")
      self.vars["window_handles"] = self.driver.window_handles
      try:
        menutouchCarrusel_promociones = self.driver.find_element(By.CSS_SELECTOR, ".menutouchCarrusel_promociones")
        gamecarrusels = menutouchCarrusel_promociones.find_elements(By.CSS_SELECTOR, ".gamecarrusel")
        for gamecarrusel in gamecarrusels:
          txt1 = gamecarrusel.find_element(By.CSS_SELECTOR, ".txt1").text
          if txt1 == "TOP 100":
            print("Encontro top 100")
            a = gamecarrusel.find_element(By.CSS_SELECTOR, "a")
            url = a.get_attribute("href")
            self.driver.get(url)
        flag_modal = False
        flag_modal_2 = False

      except Exception as e:

        print(e)

    try:
      if flag_modal is True and flag_modal_2 is True:
        menutouchCarrusel_promociones = self.driver.find_element(By.CSS_SELECTOR, ".menutouchCarrusel_promociones")
        gamecarrusels = menutouchCarrusel_promociones.find_elements(By.CSS_SELECTOR, ".gamecarrusel")
        for gamecarrusel in gamecarrusels:
          txt1 = gamecarrusel.find_element(By.CSS_SELECTOR, ".txt1").text
          if txt1 == "TOP 100":
            print("Encontro top 100")
            a = gamecarrusel.find_element(By.CSS_SELECTOR, "a")
            url = a.get_attribute("href")
            self.driver.get(url)
    except Exception as e:
      print(e)

    """
    Jordan
    """

    time.sleep(5)

    #END
    #self.driver.find_element(By.CSS_SELECTOR, ".boton:nth-child(2)").click()


#Click activar torneo



    #self.driver.find_element(By.ID, "").click()


  #BOTON promocion verano



  ##probar codigo



  
test_login_ingreso_happy = TestLoginingresoHappy()