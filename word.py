import random

# Word list for the puzzle
word_list = ['python', 'programming', 'computer', 'chatbot', 'algorithm', 'development']

def word_game():
    print("Welcome to the Word Game Puzzle!")
    print("Unscramble the letters to form the correct word.")
    print("Type 'quit' to exit the game.\n")
    
    while True:
        # Select a random word from the list
        word = random.choice(word_list)
        scrambled_word = ''.join(random.sample(word, len(word)))
        
        print(f"Scrambled word: {scrambled_word}")
        user_guess = input("Your guess: ").lower()
        
        if user_guess == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        elif user_guess == word:
            print("Correct! Well done!\n")
        else:
            print(f"Wrong! The correct word was '{word}'. Try another!\n")

# Start the game
if __name__ == "__main__":
    word_game()
