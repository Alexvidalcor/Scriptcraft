# VSCode Wayland Script

This script configures Visual Studio Code desktop entries to automatically use the Wayland display server when available. It is specifically designed for environments where user `.desktop` files are located within the `~/.local/share/applications` directory.

## How It Works

1. **Set Variables:** The script sets the path to the `.desktop` files and specifies which ones to modify.
2. **Verify Paths:** It checks if the provided path starts with `.local` and then expands the user's home directory.
3. **Modify Files:** The script reads the specified `.desktop` files and checks if they are set to use Wayland. If not, it updates the `Exec` line to include the appropriate option for Wayland.
4. **Reboot Recommendation:** After modifying the files, the script suggests rebooting the computer to apply the changes.

## Usage

1. **Clone or Download:** Clone this repository or download the script file.
2. **Run the Script:** Execute the script using Python:

    ```sh
    python Vscode-wayland.py
    ```

3. **Reboot:** After running the script, restart your computer to apply the changes.

## Requirements

- Python 3.x
- Visual Studio Code installed
- The `.desktop` files for Visual Studio Code should be located in `~/.local/share/applications`.

## Disclaimer

This script modifies system files. Make sure to have a backup before running it. Use it at your own risk.

On the other hand. this script was created for academic purposes and is not intended for professional use. There is no guarantee that it will function properly.