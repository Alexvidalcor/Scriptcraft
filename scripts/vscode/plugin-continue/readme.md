# Vscode-compose_Continue-ollama

This repository contains a Bash script to set up and manage Docker services for various machine learning models using Docker Compose.

## Script Description

The provided Bash script (`compose-ollama.sh`) performs the following tasks:

### Start Docker Services

- Uses Docker Compose to start all defined services as per `Vscode-compose_Continue-ollama.yaml`.

### Run Commands in Containers

- Executes various commands in different Docker containers to run specific machine learning models.
  - Runs GPT model (`codellama:7b`) in the `Vscode-cont_Continue-gpt` container.
  - Runs Autocomplete model (`starcoder2:3b`) in the `Vscode-cont_Continue-autocomplete` container.
  - Runs Embeddings model (`codellama:7b`) in the `Vscode-cont_Continue-embeddings` container.

### Restart Docker Services

- Restarts all Docker services to ensure the environment is correctly initialized.

## Usage

### Prerequisites

- Docker and Docker Compose must be installed and properly configured on your system.

### Steps to Run the Script

1. Clone the repository and navigate to the directory containing the script.
2. Ensure `compose-ollama.sh` has execute permissions. If not, make it executable:
   ```bash
   chmod +x compose-ollama.sh
   ```

3. Execute the script:
   ```bash
    ./compose-ollama.sh
   ```

### Output
Upon successful execution, the script will produce the following output:

    ```bash
    All services started and commands executed successfully.
    ```


## Disclaimer

This script was created for academic purposes and is not intended for professional use. There is no guarantee that it will function properly.
