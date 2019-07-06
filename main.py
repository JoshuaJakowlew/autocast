import libs.autocast as autocast

_PROCESS_NAME = "dota2.exe"

def main():
    config = autocast.init(_PROCESS_NAME)
    if not config:
        print("Process \"{}\" not found!".format(_PROCESS_NAME))
    else:
        perform(config)
def perform(config):
    print("Config loaded")
    print("Trigger key is \"{}\"".format(config["trigger"]))
    while True:
        autocast.perform(config)

if __name__ == "__main__":
    main()