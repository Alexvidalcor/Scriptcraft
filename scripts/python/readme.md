# Python environment creator

This script automates the creation of a Python virtual environment on Linux systems (Fedora or Ubuntu). It performs the following steps:
1. Checks the operating system.
2. Updates package repositories.
3. Verifies and installs the virtual environment package.
4. Creates the specified virtual environment.
5. Activates the environment and installs dependencies from `requirements.txt`.

## How to Use

1. Run the script:
    ```bash
    ./creation-env.py
    ```

2. Follow the prompts to enter the environment name and root password.

## Functions

### CheckOS
Identifies the host operating system.

### CreateEnv
Creates the Python virtual environment based on the identified OS.

## Error Handling
Raises an exception if the root password is incorrect.

## Dependencies
- Python 3
- `virtualenv`
- `requirements.txt` in the current directory

## Disclaimer

This script was created for academic purposes and is not intended for professional use. There is no guarantee that it will function properly.