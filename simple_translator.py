def translator(phrase):
    phrase_tobe_displayed=""

    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                phrase_tobe_displayed=phrase_tobe_displayed+"X"
            else:
                phrase_tobe_displayed = phrase_tobe_displayed + "x"
        else:
            phrase_tobe_displayed=phrase_tobe_displayed+letter

    return phrase_tobe_displayed

print("This is a simple translator, which replaces all vowels in a phrase with the letter 'X' \n")
print(translator(input("Enter a phrase to be translated:\n")))
