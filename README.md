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
You should have all connected monitors activated, and configured
in the correct layout.
Then
`monitor capture` will store the configuration in a config.json file local to this program.

## Set (without preset)
After having captured your layout, calling `monitor set $options`, substituting $options with a sequence of 1s and 0s with length equal to the amount of your monitors will activate(1) or deactivate(0) the respective monitor. Monitors are indexed from left ro right.

## Preset
After having captured your layout, calling `monitor preset $label $options` substituting options as described above, and using as $label a string without whitespace that should not begin with 0 or 1 will store your given options under a preset named $label.

## Set (with preset)
Set your monitors to a previously created preset by calling `monitor set $preset_label` where $preset_label is the label used as $label in a previous call to `monitor preset`.