# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDevopstest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_devopstest(self):
    self.driver.get("http://localhost/")
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("Ali Imran")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".App").click()
  
