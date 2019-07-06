import libs.autocast as autocast

def main():
    config = autocast.init()
    if not config:
        print("Config not found!")
    else:
        perform(config)
def perform(config):
    print("Config loaded")
    print("Trigger key is \"{}\"".format(config["trigger"]))
    while True:
        autocast.perform(config)

if __name__ == "__main__":
    main()