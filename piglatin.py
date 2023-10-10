def pig_latin(word):
    vowels = "AEIOUaeiou"
    if word[0] in vowels:
        return word + "way"
    else:
        prefix = ""
        i = 0
        while i < len(word) and word[i] not in vowels:
            prefix += word[i]
            i += 1
        return word[i:] + prefix + "ay"

def convert_to_pig_latin(text):
    words = text.split()
    pig_latin_words = [pig_latin(word) for word in words]
    return " ".join(pig_latin_words)

if __name__ == "__main__":
    input_text = input("Enter text to convert to Pig Latin: ")
    pig_latin_text = convert_to_pig_latin(input_text)
    print("Pig Latin:", pig_latin_text)
You can run this program and enter a sentence or a word, and it will convert it to Pig Latin. It follows a simple set of rules:

If the word starts with a vowel, add "way" to the end of the word.
If the word starts with a consonant, move all the consonants at the beginning of the word to the end and add "ay" after them.
For example:

"apple" becomes "appleway"
"banana" becomes "ananabay"
"hello world" becomes "ellohay orldway"
Feel free to modify and extend this program to suit your needs or add error handling for different cases.





