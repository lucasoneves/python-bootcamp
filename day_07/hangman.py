import random

words = ['guitarra', 'medico', 'exames', 'panela', 'metallica', 'slayer', 'estojo', 'casa']
chosen_word = random.choice(words)
word_length = len(chosen_word)
lives = 6
game_over = False
typed_words = []
list_word = ['_'] * (word_length)
points = 0

print(*list_word)
        
while not game_over:
    user_choice = input("Digite uma letra: ")
    if user_choice in typed_words:
        print(f"Você já digitou essa letra! Ainda tem {lives} chances")
    else:
        for index, item in enumerate(chosen_word):                    
            if user_choice == item:
                list_word[index] = item
                typed_words.append(item)
                points += 1
                print("Acertou", user_choice)
    
    if user_choice not in list_word and user_choice not in typed_words:
        typed_words.append(user_choice)
        lives -= 1
        print(f"Não tem a letra {user_choice}! Você tem {lives} chances")
    
    print(*list_word)
    
    if lives == 0:
        game_over = True
        print("Você perdeu!! ")
    
    if points == word_length:
        game_over = True
        print(f"Você acertou a palavra {chosen_word}")