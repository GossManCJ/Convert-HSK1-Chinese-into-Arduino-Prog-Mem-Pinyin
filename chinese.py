import requests
import json
from pypinyin import pinyin, Style


file_path = '/home/cj-goss/Documents/HSK1 Mandarin for ARDUINO/hsk1-words.json'

try:
    with open(file_path, 'r') as file:
        # Parse into py object
        hsk_list = json.load(file)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from the file '{file_path}'. Check if it is a valid JSON file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n--- COPY EVERYTHING BELOW THIS LINE ---\n")

print("// --- HSK1 DATA START ---")
print("#include <avr/pgmspace.h>")
print("")

#print(f"{hsk_list['零']}")

for i, item in enumerate(hsk_list):
    hanzi = item    
    en_translation  = hsk_list[hanzi]['translations']['en']
    
    # Use pypinyin library to convert Hanzi into numbered Pinyin
    pinyin_list = pinyin(hanzi, style=Style.TONE3)
    
    numbered_pinyin = ' '.join([' '.join(sublist) for sublist in pinyin_list])
    print(numbered_pinyin)

    
    
