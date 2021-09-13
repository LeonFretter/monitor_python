from config import Config
from subprocess import Popen, PIPE

class Set():
    def __init__(self) -> None:
        config = Config()
        self.config = config.read()

    def command(self, label: str) -> None:
        monitors = self.config[label]
    
        command = ['xrandr']

        for monitor in monitors:
            state = monitor['state']

            interface = monitor['interface']
            command.append('--output')
            command.append(interface)

            if state == 'off':
                command.append('--off')
            else:
                offset = monitor['coordinates']['offset']
                command.append('--pos')
                command.append(offset[0] + 'x' + offset[1])
                command.append('--auto')
                if monitor['primary'] == True:
                    command.append('--primary')

        process = Popen(command, stdout=PIPE, stderr=PIPE)
        process.communicate()