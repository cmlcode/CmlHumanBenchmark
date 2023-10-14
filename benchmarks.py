from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import mss
import numpy as np
import time

class Benchmarks:
    def __init__(self, driver: webdriver.Chrome):
        self.homepage = "https://humanbenchmark.com/tests/"
        self.driver = driver
    def play_reaction_time(self, subpage = 'reactiontime'):
        def play_game(game_element: WebElement, num_rounds = 5, click_color = [106,219,75,255]):
            game_location = game_element.location
            monitor = {"top": game_location["y"]+300, "left": game_location["x"], "width": 200, "height": 200}
            with mss.mss() as sct:
                while num_rounds > 0:
                    img_array = np.array(sct.grab(monitor))
                    matches = np.all(img_array == click_color, axis=2)
                    if np.any(matches):
                        game_element.click()
                        time.sleep(0.1)
                        game_element.click()
                        num_rounds -= 1
        def find_game(driver: webdriver.Chrome, class_name) -> WebElement:
            return driver.find_element(By.CLASS_NAME, class_name)
        def get_score(class_name = 'css-0'):
            return self.driver.find_element(By.CLASS_NAME, class_name).get_attribute("innerHTML")[:-2]
        
        self.driver.implicitly_wait(2)
        self.driver.get(self.homepage + subpage)
        game_element = find_game(driver = self.driver, class_name = "view-splash")
        game_element.click()
        play_game(game_element = game_element)
        return get_score()
    