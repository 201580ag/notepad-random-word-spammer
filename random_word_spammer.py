import pyautogui
import pyperclip
import time
import random

def read_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def get_random_word(words_list, used_words):
    if not words_list:
        return "Notepad file is empty."

    unique_words = set(words_list) - set(used_words)
    if not unique_words:
        return "No more words are available."

    return random.choice(list(unique_words))

def main():
    file_path = './text_file.txt'  # Please enter the proper path to the Notepad file
    words_list = read_words_from_file(file_path)
    used_words = []

    a = 0
    cho = float(input("Please enter seconds: \n"))
    bun = int(input("How many times do you repeat it?: \n"))
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    while a < bun:
        a = a + 1
        random_word = get_random_word(words_list, used_words)
        if random_word == "No more words are available.":
            print(random_word)
            break

        used_words.append(random_word)
        print("Randomly selected words:", random_word)
        pyperclip.copy(random_word)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(cho)

    print(f"I've got a total of {a} chats")

if __name__ == "__main__":
    main()