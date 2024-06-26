# Music File Processor Script

## Overview
This script processes music files in a specified directory. It iterates over all files and applies a modification function to each file. The processing status is tracked and logged, with periodic updates on the progress. Summary statistics are provided upon completion, including the total number of files processed, errors found, and errors corrected.

## Features
- Iterates through all files in the provided directory and its subdirectories.
- Applies a user-defined file modification function to each file.
- Logs file processing results and errors in a CSV file.
- Provides progress updates at 25%, 50%, and 75% completion.
- Outputs a summary of the total number of files processed, errors found, and errors corrected.

## Dependencies
- `pandas`: For creating and managing the DataFrame.
- `os`: For traversing the directory and handling file paths.

## Setup
Ensure you have the required Python packages installed. You can install the necessary packages using pip:

```sh
pip install pandas
```

## Usage

1. **Update the `musicPath` variable with the path to your music files directory.**
    ```python
    musicPath = "/path/to/your/music/files"
    ```

2. **Run the script.**
    ```bash
    python metadata-changer.py
    ```

# Output

The script generates a CSV file `Scriptcraft-music_logs.csv` in the specified Music directory. This file includes columns like:

- `FileName`: The name of the music file.
- `Artist`: The artist of the music file.
- `Title`: The title of the music file.
- `Format`: The format of the music file.
- `Album`: The album of the music file.
- `Result`: The result of the processing.
- `Error`: Flag indicating if an error occurred.
- `ErrorMessage`: The message describing the error.

These columns log the details of processing each file.

The detailed analysis of the result can be found in the Jupyter Notebook file named: **analysis-results.ipynb**

## Disclaimer

This script was created for academic purposes and is not intended for professional use. There is no guarantee that it will function properly.