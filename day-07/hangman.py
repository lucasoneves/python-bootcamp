import random

words = ['piano', 'guitarra', 'bateria', 'microfone', 'baixo', 'teclado']
chosen_word = random.choice(words)
word_length = len(chosen_word)
lives = 6
display = ''
list_word = ['_'] * (len(chosen_word))
points = 0

for position in range(word_length):
    display += '_'
print(*display)
        
while lives > 0:
    user_choice = input("Digite uma letra: ")
    for index, item in enumerate(chosen_word):
        if user_choice == item:
            points += 1
            list_word[index] = item

    print(*list_word)
    
    if points == len(chosen_word):
        lives = 0
        print(f"Você acertou a palavra {chosen_word}")