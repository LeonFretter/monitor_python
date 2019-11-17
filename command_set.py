from config import Config
from subprocess import Popen, PIPE

class Set():
    def __init__(self) -> None:
        config = Config()
        self.config = config.read()
        
    def validate(self, options: list, monitors: list) -> bool:
        only_zero = True

        if len(monitors) != len(options):
            print('No. of options not equal to no. of monitors')
            exit()

        for option in options:
            if option != '0' and option != '1':
                print('Option may only be 0 or 1')
                exit()
            if option == '1':
                only_zero = False

        if only_zero == True:
            print('At least one monitor needs to be activated!')
            exit()

    def prepare(self, monitors: list) -> None:
        for monitor in monitors:
            coordinates = monitor['coordinates']
            size = coordinates['size']
            offset = coordinates['offset']

            size[0] = int( size[0] )
            size[1] = int( size[1] )
            offset[0] = int( offset[0] )
            offset[1] = int( offset[1] )


    def command(self, options: list) -> None:
        monitors = self.config['monitors']
        
        self.validate(options, monitors)
        self.prepare(monitors)

        command = ['xrandr']
        x_subtract = 0

        for i, monitor in enumerate(monitors):
            offset = monitor['coordinates']['offset']
            offset[0] -= x_subtract

            interface = monitor['interface']
            command.append('--output')
            command.append(interface)
            
            if options[i] == '0':
                x_subtract += monitor['coordinates']['size'][0]
                command.append('--off')
            else:
                command.append('--pos')
                command.append(str( offset[0] ) + 'x' + str( offset[1] ))
                command.append('--auto')
        
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        process.communicate()