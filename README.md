# notepad-random-word-spammer

## This project is a program that selects random words from among the words in the notepad and repeatedly enters them in the chat window at specified time intervals.

To use the provided code, you will need to install the following Python modules using pip:

1. pyautogui: This module is used to control the mouse and keyboard to interact with the Notepad and paste the random words into the chat window.

```
pip install pyautogui
```

2. pyperclip: This module is used to access the clipboard, allowing you to copy the random words from the Notepad and paste them into the chat window.

```
pip install pyperclip
```

Once you have installed these modules, you can use the code as follows:

1. Save the Python code in a file, for example, `random_word_spammer.py`.
2. Create a text file named `text_file.txt` in the same directory as the Python code. Add words to this file, with each word on a separate line.
3. Open a terminal or command prompt and navigate to the directory containing the Python code and the `text_file.txt`.
4. Run the Python script by executing the command:

```bash
python random_word_spammer.py
```

5. The script will prompt you to enter the time interval in seconds (`cho`) and the number of times you want to repeat the random word spam (`bun`).
6. After entering the time interval and the repetition count, the script will begin pasting random words from the Notepad into the chat window. The script will continue until it reaches the specified number of repetitions or until all available unique words are used.

Please note that the provided code assumes you have Python installed on your system and that you are running the script in an environment that supports the `pyautogui` and `pyperclip` modules. Also, make sure you have a Notepad window open and focused so that the script can interact with it properly.
