"""Фикстуры для тестов."""

import os
import tempfile

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver(request):
    """Создаёт и уничтожает драйвер Firefox с уникальным профилем."""
    profile_dir = tempfile.mkdtemp()
    
    options = Options()
    options.profile = profile_dir
    
    service = Service()
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            safe_name = "".join(c for c in request.node.name if c.isalnum() or c in ("-", "_")).rstrip()
            screenshot_path = os.path.join(screenshots_dir, f"{safe_name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")
        except Exception:
            pass

    driver.quit()


@pytest.fixture(autouse=True)
def accept_cookies(driver):
    """Принимает куки перед каждым тестом."""
    try:
        btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'да все привыкли')]"))
        )
        btn.click()
    except Exception:
        pass
    yield