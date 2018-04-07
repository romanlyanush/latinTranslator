# get sentence from user
original = input("Please enter your text here: ").strip().lower()

# split sentence into words
words = original.split()

# loop through words and convert to pig latin
# if the word starts with vowel (aeiou), just add "yay"
# otherwise, move first cosonant cluster to the end, and add "ay" 
new_words = []
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break
        cons = word[:vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
        
# stick words back togather
output = " ".join(new_words)

# output the final string
print(output)
