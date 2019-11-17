import sys
from command_set import Set
from command_capture import Capture

if len(sys.argv) < 2:
    print('Usage: TODO')

args = sys.argv[1:]
command = args[0]

if command == 'capture':
    command_capture = Capture()
    command_capture.command()
elif command == 'set':
    options = args[1:]
    command_set = Set()
    command_set.command(options)

else:
    print('Unrecognized command')
    exit()