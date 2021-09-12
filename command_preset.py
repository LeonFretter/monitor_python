import json
import os

class Preset:
    def __init__(self) -> None:
        folder_path = os.path.abspath(os.path.dirname(__file__))
        preset_path = folder_path + '/presets.json'
        self.preset_file = open(preset_path, 'r+')

    def savePreset(self, label: str, preset: 'list[str]') -> None:
        presets = json.load(self.preset_file)
        presets[label] = preset

        self.preset_file.seek(0)
        json.dump(presets, self.preset_file, indent=4)
    
    def loadPreset(self, label: str) -> 'list[str]':
        presets = json.load(self.preset_file)
        return presets[label]