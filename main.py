import sys
from command_set import Set
from command_capture import Capture
from command_preset import Preset

if len(sys.argv) < 2:
    print('Usage: main.py <command> <options>')
    exit()

args = sys.argv[1:]
command = args[0]

if command == 'capture':
    command_capture = Capture()
    command_capture.command()
elif command == 'set':
    options = args[1:]
    if options[0] not in ['0', '1']:
        preset_label = options[0]
        command_preset = Preset()
        options = command_preset.loadPreset(preset_label)
    command_set = Set()
    command_set.command(options)
elif command == 'preset':
    command_preset = Preset()
    preset_label = args[1]
    preset_args = args[2:]
    command_preset.savePreset(preset_label, preset_args)

else:
    print('Unrecognized command')
    exit()