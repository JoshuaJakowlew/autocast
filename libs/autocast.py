import time
import random
import keyboard
import psutil
import json

def init(process_name):
    if not get_process_running(process_name):
        return False
    config = load_config()
    return config

def get_process_running(name):
    if name in (p.name() for p in psutil.process_iter()):
        return True
    return False

def perform(config):
    if keyboard.is_pressed(config["trigger"]):
        for key in config["keys"]:
            press_key(key["key"], key["delay"])

def press_key(key, delay={"min": 0.1, "max": 0.3}):
    rand_delay = (random.random() * (delay["max"] - delay["min"]) + delay["min"])
    delay_factor = random.random()
    keyboard.press(key)
    time.sleep(delay["min"])
    #time.sleep(rand_delay * delay_factor)
    keyboard.release(key)
    #time.sleep(rand_delay * (1 - delay_factor))
    
def load_config():
    with open('config.json') as config_file:
        data = json.load(config_file)
        config = {
            "trigger": '',
            "keys": []
        }
        config["trigger"] = data["trigger"]
        for key in data["keys"]:
            config["keys"].append(key)
        print(config)
        return config
