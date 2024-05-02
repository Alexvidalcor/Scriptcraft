#!/bin/bash

set -e

echo "Starting services..."
docker-compose -f Vscode-compose_Continue-ollama.yaml -p Vscode-compose_Continue-ollama up -d || { echo "Failed to start services"; exit 1; }

echo "Running GPT command..."
docker exec Vscode-cont_Continue-gpt ollama run codellama:7b-instruct || { echo "Failed to execute on GPT container"; exit 1; }

echo "Running Autocomplete command..."
docker exec Vscode-cont_Continue-autocomplete ollama run ollama run starcoder2:3b || { echo "Failed to execute on Autocomplete container"; exit 1; }

echo "Running Embeddings command..."
docker exec Vscode-cont_Continue-embeddings ollama run codellama:7b-instruct || { echo "Failed to execute on Embeddings container"; exit 1; }

echo "All services started and commands executed successfully."
