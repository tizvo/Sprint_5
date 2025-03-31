from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    # Тест проверяет вход в систему с использованием заранее сгенерированных данных.
    def test_login_with_generated_credentials(self, driver, wait, credentials):
        # Шаг 1: Открыть страницу логина
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Шаг 2: Ввести email и пароль
        email_field = wait.until(EC.element_to_be_clickable(Locators.LOGIN_EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(credentials["email"])
        
        password_field = wait.until(EC.element_to_be_clickable(Locators.LOGIN_PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(credentials["password"])

        # Шаг 3: Нажать кнопку "Войти"
        login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        login_button.click()

        # Шаг 4: Проверить, что произошел успешный вход (пользователь оказался на главной странице)
        wait.until(EC.url_contains("https://stellarburgers.nomoreparties.site/"))
        assert "https://stellarburgers.nomoreparties.site/" in driver.current_url