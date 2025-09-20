# convert-mp3-to-text

This project converts MP3 audio files to text using AI models from the `faster-whisper` library.

## Key Features

*   **MP3 to Text Conversion:** Transcribes audio from MP3 files into readable text.
*   **Faster-Whisper Integration:** Utilizes the `faster-whisper` library for efficient and accurate transcription.
*   **CUDA Support:** Leverages GPU acceleration (CUDA) for faster processing when available. Falls back to CPU if CUDA is not available.
*   **Model Size Selection:** Allows selection of different Whisper model sizes (e.g., "small", "base") to balance accuracy and speed.
*   **Detailed Output:** Provides timestamps for each transcribed segment.
*   **Debug Mode:** Prints transcribed segments to the console during processing for debugging purposes.
*   **UTF-8 Encoding:** Saves the transcribed text to a file using UTF-8 encoding to support a wide range of characters.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/versaagonon/convert-mp3-to-text.git
    cd convert-mp3-to-text
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install faster-whisper torch
    ```

    If you intend to use CUDA, ensure you have the appropriate NVIDIA drivers and CUDA toolkit installed.  Refer to the PyTorch documentation for CUDA setup instructions.

## Usage

1.  **Prepare your MP3 file:** Place the MP3 audio file you want to transcribe in the same directory as the `mp3totext.py` script.

2.  **Run the script:**

    Modify the `if __name__ == "__main__":` block in `mp3totext.py` to specify your input and output file names, as well as the desired model size. For example:

    ```python
    if __name__ == "__main__":
        transcribe_to_txt("my_audio.mp3", "my_output.txt", model_size="base", debug=True)
    ```

    Then, execute the script:

    ```bash
    python mp3totext.py
    ```

    This will transcribe "my\_audio.mp3" and save the output to "my\_output.txt". The transcribed segments will also be printed to the console if `debug=True`.

## Tech Stack and Dependencies

*   **Python:** Programming language.
*   **faster-whisper:**  For fast and accurate speech recognition.
*   **torch:** PyTorch for tensor computations and CUDA support.

## Suggestions for Improvements

1.  **Command-Line Arguments:** Implement command-line argument parsing (e.g., using `argparse`) to allow users to specify input file, output file, model size, and debug mode directly from the command line, rather than modifying the script.  This would make the script more flexible and user-friendly.

2.  **Error Handling:** Add more robust error handling to gracefully handle cases such as invalid input files, missing dependencies, or CUDA initialization failures.  Provide informative error messages to the user.

3.  **Progress Bar:** Integrate a progress bar to visually indicate the transcription progress, especially for large audio files. This would improve the user experience by providing feedback on the script's progress.
