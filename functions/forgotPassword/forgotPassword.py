from selenium.webdriver.common.by import By
import time


class ForgotPassword:
    # defino los diferentes selectores
    def __init__(self, driver):
        self.driver = driver

        # forgot password form
        self.forgot_pass_locator = (By.XPATH, "//a[contains(.,'Olvidé mi contraseña')]")
        self.email_input_locator = (By.XPATH, "//input[contains(@id,'email')]")
        self.btn_enviar = (By.XPATH, "//input[contains(@value,'ENVIAR')]")

        # Alerta datos no coinciden
        self.alert_validator = (By.XPATH, "//h2[@class='swal2-title'][contains(.,'No hemos encontrado ningun registro en base a la información ingresada, por favor verifiquela y continue.')]")

    # Método para ingresar el email
    def email_validator(self, email):
        self.driver.find_element(*self.forgot_pass_locator).click()
        self.driver.find_element(*self.email_input_locator).clear()
        self.driver.find_element(*self.email_input_locator).send_keys(email)

    # Método que obtiene el texto de la alerta
    def alert_content(self):
        return self.driver.find_element(*self.alert_validator).text

    # Método validar el email en la base de datos
    def form_validator(self, email):
        time.sleep(1)
        self.email_validator(email)
        time.sleep(2)
        self.driver.find_element(*self.btn_enviar).click()

    # Finaliza el chrome driver
    def close(self):
        self.driver.close()
