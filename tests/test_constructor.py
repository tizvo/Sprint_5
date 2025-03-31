from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class TestConstructorTabs:
    # Тест проверяет, что при выборе вкладки "Булки" она становится активной
    def test_constructor_buns_tab(self, driver, wait):
        # Шаг 1: Открыть главную страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # Ожидаем загрузки страницы
        wait.until(EC.visibility_of_element_located(Locators.BUNS_SECTION))

        # Шаг 2: Нажать на вкладку "Булки" с помощью JavaScript
        buns_element = wait.until(EC.presence_of_element_located(Locators.BUNS_SECTION))
        driver.execute_script("arguments[0].click();", buns_element)

        # Шаг 3: Проверить, что вкладка активна (используя ожидание)
        wait.until(EC.presence_of_element_located(Locators.ACTIVE_TAB))
        is_buns_active = driver.find_element(*Locators.ACTIVE_TAB).get_attribute("class")
        assert "tab_tab_type_current" in is_buns_active, "Ожидалось, что вкладка 'Булки' станет активной, но этого не произошло"

    # Тест проверяет, что при выборе вкладки "Соусы" она становится активной
    def test_constructor_sauces_tab(self, driver, wait):
        # Шаг 1: Открыть главную страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # Ожидаем загрузки страницы
        wait.until(EC.visibility_of_element_located(Locators.SAUCES_SECTION))

        # Шаг 2: Нажать на вкладку "Соусы" с помощью JavaScript
        sauces_element = wait.until(EC.presence_of_element_located(Locators.SAUCES_SECTION))
        driver.execute_script("arguments[0].click();", sauces_element)

        # Шаг 3: Проверить, что вкладка активна (используя ожидание)
        wait.until(EC.presence_of_element_located(Locators.ACTIVE_TAB))
        is_sauces_active = driver.find_element(*Locators.ACTIVE_TAB).get_attribute("class")
        assert "tab_tab_type_current" in is_sauces_active, "Ожидалось, что вкладка 'Соусы' станет активной, но этого не произошло."

    # Тест проверяет, что при выборе вкладки "Начинки" она становится активной
    def test_constructor_fillings_tab(self, driver, wait):
        # Шаг 1: Открыть главную страницу
        driver.get("https://stellarburgers.nomoreparties.site")

        # Ожидаем загрузки страницы
        wait.until(EC.visibility_of_element_located(Locators.FILLINGS_SECTION))