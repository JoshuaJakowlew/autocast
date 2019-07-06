import time
import random
import keyboard
import psutil
import json

def init():
    config = load_config()
    return config

def perform(config):
    if keyboard.is_pressed(config["trigger"]):
        for key in config["keys"]:
            press_key(key["key"], key["delay"])

def press_key(key, delay):
    random_delay = get_delay(delay)
    keyboard.press(key)
    time.sleep(random_delay)
    print("key = {}, delay = {}".format(key, random_delay))
    keyboard.release(key)
    
def get_delay(delay):
    factor = 10 ** 9
    low  = int(delay["min"] * factor)
    high = int(delay["max"] * factor)
    return random.randint(low, high) / factor

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
