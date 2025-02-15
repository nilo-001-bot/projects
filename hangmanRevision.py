import random

words = ["cyberpunk", "banana", "pineapple", "Elden"]

def hangman(tries):
    stages = [
        """
        -------
        |      |
        |
        |
        |
        |
    -----
        """,
        """
        -------
        |      |
        |      o
        |
        |
        |
    -----
        """,
        """
        -------
        |      |
        |      o
        |      |
        |
        |
    -----
        """,
        """
        -------
        |      |
        |      o
        |     /|
        |
        |
    -----
        """,
        """
        -------
        |      |
        |      o
        |     /|\\
        |
        |
    -----
        """,
        """
        -------
        |      |
        |      o
        |     /|\\
        |      |
        |     /
    -----
        """,
        """
        -------
        |      |
        |      o
        |     /|\\
        |      |
        |     / \\
    -----
        """
        
        
    
    ]
    return stages[tries]


def displayHint(hint):
    print("".join(hint))
    
def displayanswer(answer):
    print(answer)
    


def main():
    answer = random.choice(words)
    tries = 0
    hint = ["_"] * len(answer)
    is_running = True
    guessed_words = []

    while is_running:
        print(hangman(tries))
        displayHint(hint)
        
        word = input("Enter your guess: ").lower()
        
        if len(word) != 1 or not word.isalpha():
            print("Invalid input")
            continue
        
        if word in guessed_words:
            print(f"Already guessed {word}")
            continue
        guessed_words.append(word)
        
        
        
        
        if word in answer:
            for i in range(len(answer)):
                if answer[i] == word:
                    hint[i] = word
        else:
            tries += 1
            
        if "_" not in hint:
            print(hangman(tries))
            displayanswer(answer)
            print("You win")
            is_running  = False
            
        elif tries >= 6:
            print(hangman(tries))
            displayanswer(answer)
            print("You Lose")
            is_running  = False
            




if __name__ == "__main__":
    main()