from config import Config

def listPresets():
    the_config = Config()
    presets = the_config.read()

    for key in presets.keys():
        print(key)