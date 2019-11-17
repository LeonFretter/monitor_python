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

    def command(self):
        process_xrandr = Popen(['xrandr'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process_xrandr.communicate()

        stdout_str = stdout.decode('utf-8')
        stdout_lines = stdout_str.splitlines()

        monitors = []

        for line in stdout_lines:
            if ' connected ' in line:
                monitor = self.getMonitor(line)
                monitors.append(monitor)
        
        self.config.write( { 'monitors': monitors } )