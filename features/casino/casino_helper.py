from datetime import time
from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from core.util.debug.trace_helper import TraceHelper


class CasinoHelper:
    def __init__(self, driver, url="", page=0, reload=False, layouts=[], target_urls=[], table_page_total=0):
        self.driver = driver
        self.url = url
        self.page = page
        self.reload = reload
        self.layouts = layouts
        self.target_urls = target_urls
        self.table_page_total = table_page_total
        self.sheets = []
        self.trace_helper = TraceHelper()

    def login_col(self):
        #Ingresar URL
        self.driver.get(self.url)
        # 2 | setWindowSize | 1065x817 |
        self.driver.maximize_window()
        # 3 | click | INGRESAR
        header = self.driver.find_element(By.CSS_SELECTOR, "header")
        buttons = header.find_elements(By.CSS_SELECTOR, "a")
        for button in buttons:
            if button.text == "INGRESAR":
                button.click()
                sleep(5)

        # 4 Seleccionar ir a casino
        wait = WebDriverWait(self.driver, 60)
        target_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cardDondeVamosCasino > button")))
        target_button.click()


    def iniciar_sesion(self):
        # Mi menu
        header = self.driver.find_element(By.CSS_SELECTOR, "header.o-header")
        buttons = header.find_elements(By.CSS_SELECTOR, "button")
        for button in buttons:
            if "INICIAR SESIÓN" == button.text:
                button.click()
                sleep(5)

    def usuario_password_nivel(self, nivel=1):
        print(f"nivel {nivel}")

        if nivel == 1:
            self.driver.find_element(By.ID, "username_aside").send_keys("PruebasFide1")
            self.driver.find_element(By.ID, "password_aside").send_keys("Fide2021")
        elif nivel == 2:
            self.driver.find_element(By.ID, "username_aside").send_keys("PruebasFide4")
            self.driver.find_element(By.ID, "password_aside").send_keys("Fide2021")
        elif nivel == 3:
            self.driver.find_element(By.ID, "username_aside").send_keys("PruebasFide9")
            self.driver.find_element(By.ID, "password_aside").send_keys("Fide2021")
        elif nivel == 4:
            self.driver.find_element(By.ID, "username_aside").send_keys("Testing08")
            self.driver.find_element(By.ID, "password_aside").send_keys("Testing08")
        elif nivel == 5:
            self.driver.find_element(By.ID, "username_aside").send_keys("Testing09")
            self.driver.find_element(By.ID, "password_aside").send_keys("Testing09")
        elif nivel == 6:
            self.driver.find_element(By.ID, "username_aside").send_keys("Testing10")
            self.driver.find_element(By.ID, "password_aside").send_keys("Testing10")
        elif nivel == 7:
            self.driver.find_element(By.ID, "username_aside").send_keys("Testing11")
            self.driver.find_element(By.ID, "password_aside").send_keys("Testing11")
        elif nivel == 8:
            self.driver.find_element(By.ID, "username_aside").send_keys("Testing13")
            self.driver.find_element(By.ID, "password_aside").send_keys("Testing13")
        elif nivel == 9:
            self.driver.find_element(By.ID, "username_aside").send_keys("Testing06")
            self.driver.find_element(By.ID, "password_aside").send_keys("Testing06")
        elif nivel == 0:
            self.driver.find_element(By.ID, "username_aside").send_keys("PruebasFide5")
            self.driver.find_element(By.ID, "password_aside").send_keys("Fide2021")

        self.driver.find_element(By.ID, "login_button_aside").click()
        sleep(10)

    def cerrar_sesión_col(self):
        # Mi menu
        header = self.driver.find_element(By.CSS_SELECTOR, "header.o-header")
        micuenta = header.find_elements(By.CSS_SELECTOR, "a")
        for button in micuenta:
            if button.accessible_name == "person MI CUENTA":
                button.click()
                sleep(5)
        # Cerrar sesión
        aside = self.driver.find_element(By.CSS_SELECTOR, "aside.o-aside.fixed-right")
        cerrarsesión = aside.find_elements(By.CSS_SELECTOR, "a")
        for buttond in cerrarsesión:
            if buttond.text == "CERRAR SESIÓN":
                buttond.click()
                sleep(6)

    def ingresar_promociones(self):

        # self.driver.find_element(By.ID,"gtm--menu-aside-promociones").click()
        try:
            # self.driver.find_element(By.ID,"gtm--menu-aside-promociones")
            aside = self.driver.find_element(By.CSS_SELECTOR, ".o-aside.fixed-left")
            prombuttons = aside.find_elements(By.CSS_SELECTOR, "a")
            for buttonmen in prombuttons:
                if buttonmen.text == "PROMOCIONES":
                    buttonmen.click()
                    sleep(10)
        except (Exception, StopIteration) as e:
            print(f"{e}")

    def ingresar_menu(self):

        sodesktop = self.driver.find_element(By.CSS_SELECTOR, ".show-only--desktop")
        menubutton = sodesktop.find_elements(By.CSS_SELECTOR, "a")
        for buttonmen in menubutton:
            if buttonmen.text == "menu":
                buttonmen.click()

    # SELECCIONAR NIVELES DE AD PROMOS 1(2143),2(1385),3(4120),4(9333),5(2322),6(1722),7(2275),8(14455),9(4026),0(3337)
    def id_nivel(self, nivel=1):
        print(f"nivel {nivel}")
        btn_container = self.driver.find_element(By.ID, "contentModalPlayerOculto")
        btn_oculto = btn_container.find_element(By.CSS_SELECTOR, "button")
        btn_oculto.click()
        if nivel == 1:
            self.driver.find_element(By.ID, "idAliraCampo").send_keys("2143")
        elif nivel == 2:
            self.driver.find_element(By.ID, "idAliraCampo").send_keys("1385")
        elif nivel == 3:
            self.driver.find_element(By.ID, "idAliraCampo").send_keys("4120")
        elif nivel == 4:
            self.driver.find_element(By.ID, "idAliraCampo").send_keys("9333")
        elif nivel == 5:
            self.driver.find_element(By.ID, "idAliraCampo").send_keys("2322")
        elif nivel == 6:
            self.driver.find_element(By.ID, "idAliraCampo").send_keys("1722")
        elif nivel == 7:
            self.driver.find_element(By.ID, "idAliraCampo").send_keys("2275")
        elif nivel == 8:
            self.driver.find_element(By.ID, "idAliraCampo").send_keys("14455")
        elif nivel == 9:
            self.driver.find_element(By.ID, "idAliraCampo").send_keys("4026")
        elif nivel == 0:
            self.driver.find_element(By.ID, "idAliraCampo").send_keys("3337")
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()

    def saltar_promoción_verano(self):

        flag_modal = False
        flag_modal_2 = False

        try:
            wait = WebDriverWait(driver=self.driver, timeout=10)
            modal = wait.until(EC.visibility_of_element_located((By.ID, "formEliminarBono")))
            modal.find_element(By.LINK_TEXT, "ACTIVAR LUEGO").click()
            flag_modal = True

            wait = WebDriverWait(driver=self.driver, timeout=10)
            modal = wait.until(EC.visibility_of_element_located((By.ID, "popupContent")))

            flag_modal_2 = True
            links = modal.find_elements(By.CSS_SELECTOR, "a")
            for link in links:
                if link.text == "ENTENDIDO":
                    link.click()
                    sleep(5)

        except (Exception, NoSuchElementException) as e:

            print(self.trace_helper.get_trace_str(e))

    def bajar_cursor(self, x=0, y=0):

        self.driver.execute_script(f"window.scrollTo(0,{y})")
        sleep(7)