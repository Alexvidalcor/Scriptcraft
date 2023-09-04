# Native libraries
import os

# General variables
codePath = ".local/share/applications"
codeFiles = ["code.desktop", "code-url-handler.desktop"]
xorgLine = "Exec=/usr/share/code/code"
waylandLine = "Exec=/usr/share/code/code --ozone-platform-hint=auto"


# Logic

print("-------\nStarting script - Wayland in vscode\n -------")

if codePath.startswith(".local"):
    print("Codepath in home")
    homeUser = os.path.expanduser("~")
    print("-------")

print(f"Path used: {homeUser}/{codePath}\n -------")

for file in os.listdir(f"{homeUser}/{codePath}"):
    if file in codeFiles:

        print(f"File detected: {file}")
        
        with open(f"{homeUser}/{codePath}/{file}", "rt") as f:
            s = f.read()

        if waylandLine not in s:       
            with open(f"{homeUser}/{codePath}/{file}", "wt") as f:
                f.write(s.replace(xorgLine, waylandLine))
                print(f"File modified: {file}\n-------")
        else:
            print(f"File not modified: {file}\n-------")

    
print("Finished, please reboot the computer\n -------")
