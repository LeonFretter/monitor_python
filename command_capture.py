from subprocess import Popen, PIPE, call
from config import Config

class Capture:
    def __init__(self):
        self.config = Config()

    def getMonitor(self, line : str) -> dict:
        words = line.split()
        interface = words[0]
        coords = words[2]

        if ' primary ' in line:
            coords = words[3]

        coords_split = coords.replace('x', ' ').replace('+', ' ').split()
        size = [ coords_split[0], coords_split[1] ]
        offset = [ coords_split[2], coords_split[3] ]

        return {
            'interface': interface,
            'coordinates': {
                'size': size,
                'offset': offset
            }
        }

    def command(self) -> None:
        stdout_lines = self.readXrandr()

        monitors = []

        for line in stdout_lines:
            if ' connected ' in line:
                if '+' in line:
                    monitor = self.getMonitor(line)
                    monitors.append(monitor)
                else:
                    print('Only call capture when all your monitors are activated')
                    exit(1)
        
        monitors = sorted(monitors, key=lambda m: m['coordinates']['offset'][0])
        self.config.write( { 'monitors': monitors } )

    def readXrandr(self) -> 'list[str]':
        process_xrandr = Popen(['xrandr'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process_xrandr.communicate()

        stdout_str = stdout.decode('utf-8')

        return stdout_str.splitlines()