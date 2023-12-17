import unittest
import time
from utilities.utilities import WebDriverElements
from functions.loginValidations.loginValidations import LoginValidations


class LoginValidationsTests(unittest.TestCase):
    def setUp(self):
        self.driver_paths = WebDriverElements()
        self.driver = self.driver_paths.get_driver()
        self.driver.get("https://test.conectadosmexico.com/login")

    # Login exitoso
    def test_01_login_exitoso(self):
        loginValidations = LoginValidations(self.driver)
        loginValidations.login('1052369858', '12130562LSTST;a')
        # Assert para validar que se visualiza el dashboard de la pagina principal

        current_url = self.driver.current_url
        expected_dashboard_utl = "https://test.conectadosmexico.com/home"
        self.assertEqual(current_url, expected_dashboard_utl)

    # Valida que el campo Username sea obligatorio
    def test_02_validate_user_name(self):
        loginValidations = LoginValidations(self.driver)
        loginValidations.login2('', '')

        # Assert para validar la alerta del check obligatorio
        expected_text = "¡Para poder iniciar sesión, es necesario marcar la casilla de mayoria de edad!"
        alert_text = loginValidations.check_required()
        self.assertEqual(alert_text, expected_text, f"NO se está validando que el campo Username sea requerido. "
                                                    f"Se esperaba: '{expected_text}', pero se obtuvo: '{alert_text}'.")

    # Finaliza el test
    def tearDown(self):
        time.sleep(1)
        print('¡Se ha completado el Test Aumatico!')
        loginValidations = LoginValidations(self.driver)
        loginValidations.close()

    if __name__ == '__main__':
        unittest.main()
