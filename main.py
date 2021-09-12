import sys
from command_set import Set
from command_capture import Capture
from command_list import listPresets

if len(sys.argv) < 2:
    print('Usage: main.py <command> <options>')
    exit()

args = sys.argv[1:]
command = args[0]

if command == 'capture':
    if len(sys.argv) < 3:
        print("Usage: main.py capture <label>")
    label = args[1]
    command_capture = Capture()
    command_capture.command(label)
elif command == 'set':
    if len(sys.argv) < 3:
        print("Usage: main.py set <label>")
    label = args[1]
    command_set = Set()
    command_set.command(label)
elif command == 'list':
    listPresets()

else:
    print('Unrecognized command')
    exit()