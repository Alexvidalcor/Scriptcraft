# Config-AWS

This Python script automates the process of setting up AWS credentials and verifying their validity. The script performs the following functions:

1. **Validates AWS Credentials**: Checks if the provided AWS credentials are valid.
2. **Checks for AWS Configuration Directory**: Ensures the `.aws` directory exists in the user's home directory, creating it if necessary.
3. **Creates or Updates AWS Credentials File**: Writes or updates AWS credentials to the `credentials` file in the `.aws` directory.
4. **Prompts for User Input**: Asks the user for AWS credentials (access key, secret key, and optional session token).

## How to Use

**Run the Script**:
   
   ```sh
   python config-aws.py
   ```

# Obsolete

This project is outdated and does not support key features such as "profiles"
At the time, it made sense, but there are better options available now.

## Disclaimer

This script was created for academic purposes and is not intended for professional use. There is no guarantee that it will function properly.
