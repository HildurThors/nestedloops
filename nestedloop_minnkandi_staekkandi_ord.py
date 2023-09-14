sentence = input("Write a sentence: ")

# Remove any leading or trailing whitespace
sentence = sentence.strip()

# Loop through the sentence and print out each substring
for i in range(len(sentence)):
    print(sentence[i:])
for i in range(len(sentence)):
    print(" " * i + sentence[i:])