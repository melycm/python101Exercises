name = input("Enter your name here: ")
sentence = "Hello {}, your name has {} letters in it! Awesome!".format(name, len(name))
upper_sentence = sentence.upper()
print(upper_sentence)