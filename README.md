A simple python cli that allows a fast (de)activation of connected monitors.
Needs a system that has the `xrandr` commmand available.

# Install
Either run the program directly via python, or add an alias to your .bashrc, or add a shell-script that calls this program via python to a path that is included in your PATH environment-variable.
Exemplary alias is given below:
## Alias
`alias monitor = python3 /path/to/monitor/main.py`

All the below-notes assume that this program is available as `monitor` in your terminal.

# Usage
## Capture
Configure your monitors via your system-settings.
Then
`monitor capture <label>` will store the configuration in a config.json file local to this program.

## Set
After having captured one or more layouts, `monitor set <label>` lets you switch between them.

## List
`monitor list` prints out the labels of your configured layouts.