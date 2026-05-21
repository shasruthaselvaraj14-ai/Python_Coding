None selected

Skip to content
Using Gmail with screen readers
Enable desktop notifications for Gmail.
   OK  No thanks
2 of 94
(no subject)
Inbox

akkshetha m
Attachments
9:52 AM (15 minutes ago)
to me


 28 Attachments
  •  Scanned by Gmail
import os

folder_path = r"D:\shasrutha\python"  
file_name = "a.txt"

full_path = os.path.join(folder_path, file_name)

try:
    with open(full_path, "r", encoding="utf-8") as file:
        text = file.read()

    print("--- File Content ---")
    print(text)

    
    target_char = "e"
    char_count = text.lower().count(target_char.lower())

   
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)

    
    words = text.split()
    clean_words = [word.strip(".,!?;:") for word in words]
    sorted_words = sorted(clean_words, key=str.lower)

    print(f"\n1. The character '{target_char}' appears {char_count} times.")
    print(f"2. Total vowels in the file: {vowel_count}")
    print("3. Words sorted alphabetically:")
    print(sorted_words)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found in '{folder_path}'.")   
triggering path file.py
Displaying triggering path file.py.
