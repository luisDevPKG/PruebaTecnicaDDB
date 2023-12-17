import unittest
import time
from utilities.utilities import WebDriverElements
from functions.forgotPassword.forgotPassword import ForgotPassword


class ForgotPassValidationsTests(unittest.TestCase):
    def setUp(self):
        self.driver_paths = WebDriverElements()
        self.driver = self.driver_paths.get_driver()
        self.driver.get("https://test.conectadosmexico.com/login")

    # Validacion formulario olvide contraseña exitoso
    def test_01_validar_info_db(self):
        forgotPassword = ForgotPassword(self.driver)
        forgotPassword.form_validator('luchitofmos@gmail.com')
        # Assert para validar la alerta del check obligatorio
        expected_text = "No hemos encontrado ningun registro en base a la información ingresada, por favor verifiquela y continue."
        alert_text = forgotPassword.alert_content()
        self.assertEqual(alert_text, expected_text, f"NO se está validando que el correo ingresadoi esté registrado. "
                                                    f"Se esperaba: '{expected_text}', pero se obtuvo: '{alert_text}'.")

    # Finaliza el test
    def tearDown(self):
        time.sleep(1)
        print('¡Se ha completado el Test Aumatico!')
        loginValidations = ForgotPassword(self.driver)
        loginValidations.close()

    if __name__ == '__main__':
        unittest.main()