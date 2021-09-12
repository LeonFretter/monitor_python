from subprocess import Popen, PIPE, call
from config import Config
from functools import cmp_to_key

def compareMonitors(monitor_1 : dict, monitor_2 : dict) -> int:
    if 'coordinates' in  monitor_1:
        if 'coordinates' in monitor_2:
            x_1 = int(monitor_1['coordinates']['offset'][0])
            x_2 = int(monitor_2['coordinates']['offset'][0])
            if x_1 < x_2:
                return -1
            elif x_1 > x_2:
                return 1
            else:
                return 0
        else:
            return -1
    else:
        if 'coordinates' in monitor_2:
            return 1
        else:
            return 0

class Capture:
    def __init__(self):
        self.config = Config()

    def getMonitor(self, line : str) -> dict:
        words = line.split()
        interface = words[0]
        coords = words[2]

        if ' primary ' in line:
            coords = words[3]

        if '+' in line:
            coords_split = coords.replace('x', ' ').replace('+', ' ').split()
            size = [ coords_split[0], coords_split[1] ]
            offset = [ coords_split[2], coords_split[3] ]

            return {
                'interface': interface,
                'state': 'on',
                'coordinates': {
                    'size': size,
                    'offset': offset
                }
            }
        else:
            return {
                'interface': interface,
                'state': 'off',
            }

    def command(self, label : str) -> None:
        stdout_lines = self.readXrandr()

        monitors = []

        for line in stdout_lines:
            if ' connected ' in line:
                monitor = self.getMonitor(line)
                monitors.append(monitor)
        
        current_config = self.config.read()

        monitors.sort(key=cmp_to_key(compareMonitors))  #= sorted(monitors, key=compareMonitors)
        current_config[label] = monitors

        self.config.write(current_config)

    def readXrandr(self) -> 'list[str]':
        process_xrandr = Popen(['xrandr'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process_xrandr.communicate()

        stdout_str = stdout.decode('utf-8')

        return stdout_str.splitlines()