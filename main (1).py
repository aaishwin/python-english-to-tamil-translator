""" Growing up, it was often very difficult for me to explain
things to my parents in a way that they can understand. This is why I set out to make
an English-to-Tamil translator in Python. It would use a text file as a database of sorts,
and it would replace the English word you typed, with the Tamil equivalent. Right now it is a bit limited, as I had to
populate the text file myself, since I could not find a text file in the desired format. This is why
my project also supports adding new translations into the file.
"""
import os
import string

def load_translations(file_path):
    """
    This function will Load translations from the text file into a dictionary.
    Each line should be in the format: English,Tamil
    """
    translations = {}
    try:
        """encoding='utf-8', uses the unicode transformation format, 
                    which would allow us to use all unicode characters, which would help to make sure that 
                    tamil characters will be printed"""
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):  # Skip empty lines or commented lines
                    continue
                try:
                    #This will split the line into English and Tamil parts
                    english, tamil = line.split(',', 1)
                    # This will normalize the case and strip the spaces
                    translations[english.strip().lower()] = tamil.strip()
                except ValueError:
                    # this will help us Handle invalid lines
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        # This will create a new file if it doesn't exist
        print(f"Error: The file '{file_path}' does not exist. Creating a new file.")
        open(file_path, 'w').close()
    return translations

def save_translations(file_path, english, tamil):
    """
    This function will save a new translation into the file.
    """
    # This adds a new translation to the file
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"{english.strip().lower()},{tamil.strip()}\n")

def sentence_translations(sentence, translations):
    """
    This function will translate a sentence from English to Tamil.
    Words without a Tamil equivalent will remain unchanged.
    """
    # this will remove punctuation from the sentence
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    # Split the sentence into words
    words = sentence.split()
    translated_words = []
    for word in words:
        # Translate each word or leave unchanged if no translation exists
        tamil_word = translations.get(word.lower(), "தொகுப்பு இல்லை")
        print(f"Translating '{word}' -> '{tamil_word}'")  # Debug translation
        translated_words.append(tamil_word)
    return " ".join(translated_words)

def main():
    # This will look for the file in the downloads folder
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_path = os.path.join(downloads_folder, 'translations.txt')
    translations = load_translations(file_path)

    if not translations:
        print("No translations found. Please add the appropriate translation by pressing option 2")

    print("Welcome to my English-to-Tamil translator! What task would you like to complete today?")

    while True:
        # give the user a menu of options
        print("\nHere are your options:")
        print("1. Do you want me to translate a sentence for you?")
        print("2. Do you want to add a new translation?")
        print("3. Do you want to exit?")
        choice = input("What is your choice (1/2/3?): ").strip()

        if choice == '1':
            # Translate a sentence
            sentence = input("Enter a word or sentence in English: ").strip()
            translated_sentence = sentence_translations(sentence, translations)
            print(f"Translated sentence is:\n{translated_sentence}")

        elif choice == '2':
            # This will add a new translation
            english_word = input("Enter a word in English: ").strip().lower()
            tamil_word = input(f"Enter the Tamil equivalent for '{english_word}': ").strip()
            if english_word in translations:
                print("This word has already been accounted for. Thank you ")
            else:
                translations[english_word] = tamil_word
                save_translations(file_path, english_word, tamil_word)
                print("Translation has been added! Thank you!")

        elif choice == '3':
        #This is how you will exit the program.

                print("Thank you for your time! Goodbye!")
                break

        else:
            # This will deal with any invalid input (anything that is not 1,2,or 3)
            print("That is not a valid input. Please select either 1, 2, or 3. Thank you!")

if __name__ == "__main__":
    main()
#this makes sure that the projects functions are only run when the script is run directly