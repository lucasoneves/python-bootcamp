import random

words = ['piano', 'guitarra', 'bateria', 'microfone', 'baixo', 'teclado']
chosen_word = random.choice(words)
word_length = len(chosen_word)
placeholder = ''

for position in range(word_length):
    placeholder += '_'
print(placeholder)

user_choice = input("Digite uma letra: ")
display = ''

for word in chosen_word:
    if word == user_choice:
        display += word
    else:
        display += '_'
        
print(display)