from random import randrange
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.action_chains import ActionChains

def play(browser, canvas):
    width = canvas.rect["width"]
    dropx = randrange(5, width - 5) - width // 2    
    
    action = ActionChains(browser)    
    action.move_to_element_with_offset(canvas, dropx, 30)
    action.click()
    action.perform()

def print_logs(browser):
    for entry in browser.get_log("browser"):
        if entry["level"] == "INFO":
            print(" ".join(entry["message"].split()[2:]))

# Capture console logs
options = Options()
options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

browser = webdriver.Chrome(options=options)
browser.get("file:///home/gg/Desktop/suika-game/index.html")

# Game UI
canvas = browser.find_element(value="game-ui")

while(True):
    print_logs(browser)
    play(browser, canvas)
