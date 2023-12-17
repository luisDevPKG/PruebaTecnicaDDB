from selenium.webdriver.common.by import By
from utilities import utilities


class LoginValidations:
    # defino los diferentes selectores
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.XPATH, "//input[contains(@name,'sap_number')]")
        self.password_locator = (By.XPATH, "//input[contains(@id,'password')]")
        self.check_terms_conditions = (By.XPATH, "//label[contains(@for,'tyc')]")
        self.login_button_locator = (By.XPATH, "//button[@type='button'][contains(.,'ingresar')]")
        self.locator_validator = (By.XPATH, "//strong[contains(.,'¡Para poder iniciar sesión, es necesario marcar la casilla de mayoria de edad!')]")

    # Metodo para ingresar el usuario en el formulario
    def enter_user_name(self, username):
        self.driver.find_element(*self.username_locator).clear()
        self.driver.find_element(*self.username_locator).send_keys(username)

    # Metodo para ingresar el password en el formulario
    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).clear()
        self.driver.find_element(*self.password_locator).send_keys(password)

    # Clic en el check de terminos y condiciones
    def terms_conditios_check(self):
        self.driver.find_element(*self.check_terms_conditions).click()

    # Método que hace clic en el boton del login
    def click_login_button(self):
        self.driver.find_element(*self.login_button_locator).click()

    # Método que valida que el check terminos sea obligatorio
    def check_required(self):
        return self.driver.find_element(*self.locator_validator).text

    # Método que realiza el proceso de login completo
    def login(self, username, password):
        self.enter_user_name(username)
        self.enter_password(password)
        self.terms_conditios_check()
        self.click_login_button()

    # Método que realiza el proceso de login sin marcar el check
    def login2(self, username, password):
        self.enter_user_name(username)
        self.enter_password(password)
        self.click_login_button()

    # Finaliza el chrome driver
    def close(self):
        self.driver.close()