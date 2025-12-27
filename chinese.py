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




print("// --- HSK1 DATA START ---")

for i, item in enumerate(hsk_list):
    hanzi = item    
    en_translation  = hsk_list[hanzi]['translations']['en']
    
    # Use pypinyin library to convert Hanzi into numbered Pinyin
    pinyin_list = pinyin(hanzi, style=Style.TONE3)    
    numbered_pinyin = ' '.join([' '.join(sublist) for sublist in pinyin_list])

    print(f'const char p_{i}[] PROGMEM = "{numbered_pinyin}";')
    print(f'const char e_{i}[] PROGMEM = "{en_translation}";')

print("")
print("struct Flashcard {")
print("  const char* pinyin;")
print("  const char* english;")
print("};")

print("")
print("const Flashcard deck[] PROGMEM = {")

for i in range(len(hsk_list)):
    comma = "," if i < len(hsk_list) - 1 else ""
    print(f"  {{p_{i}, e_{i}}}{comma}")

print("};")
print("const int cardCount = sizeof(deck) / sizeof(deck[0]);")
print("// --- HSK1 DATA END ---")
print("")
