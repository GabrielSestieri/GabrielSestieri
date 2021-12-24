import random
import os

def read_words(path): 
    words= {}
    f = open(path, encoding = 'utf-8')
    for line in f: 
        if line.startswith('#'):
            categories = (line[1:]).strip()
            words[categories] = ''
            if categories == 'Animals':
                words[categories] = []
            elif categories == 'Careers':
                words[categories] = []
            elif categories == 'Capital cities':
                words['Capital cities'] = []
            elif categories == 'Idioms':
                words[categories] = []
            elif categories == 'Vegetables':
                words[categories] = []
            elif categories == 'Musical instruments':
                words[categories] = []
        else:
            phrases = (line.strip())
            words[categories].append(phrases)
    return words  
    f.close()

def select_word(words):
    word = list(words.keys())
    random_category = random.choice(word)
    random_phrase = random.choice(words[random_category])
    return random_phrase, random_category
    
def mask_word(phrase, correct_guesses, char):
    correct_letters = []
    masked_word = ''
    for letter in phrase:
        if letter.isalpha() == True: 
            correct_letters.append(letter) 
            if letter in correct_letters:
                if letter in correct_guesses:
                    letter = letter
                    masked_word += letter
                else:
                    letter = char
                    masked_word += letter
                
        elif letter.isalpha() == False:
                letter = letter
                masked_word = masked_word + letter     
    return masked_word

def get_guess(letters):
    user_guess = input("Enter a letter: ")
    guess = user_guess.lower()
    if guess.isalpha() == False:
        print("Invalid guess, letters only! Try again.")
        return guess
    elif len(guess) > 1:
        print("One letter only! Try again.")
        return guess
    elif guess in letters:
        print("You already guessed this letter! Try again.")
        return guess
    elif guess.isalpha() == True:
        return guess
      
def play_game(words):
    a, b = select_word(words)
    phrase = a
    category = b
    user_guesses = []
    count = 0
    char = '_ ' 
    while count < 6:
        print("\nThe category is " + category)
        masked = mask_word(phrase, user_guesses, char) 
        print('')
        print(masked)
        print("Here are your guesses: {}".format(user_guesses))
        print("Incorrect guesses: {}".format(count))
        #os.system("clear")
        if char not in masked:
            print("Congratulations, you won!")
            break
        letter_guess = get_guess(user_guesses)
        user_guesses.append(letter_guess)
        if len(letter_guess) != 1:
            count = count
        elif letter_guess not in phrase:
            os.system("clear")
            count += 1
            if count == 1:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (o  <  o)         ")
                print(" |                      ")
                print("_|__                    ")
            elif count == 2:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (o  <  o)         ")
                print(" |      (   )           ")
                print("_|__                    ")
            elif count == 3:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (o  <  o)         ")
                print(" |     c(   )           ")
                print("_|__                    ")
            elif count == 4:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (o  <  o)         ")
                print(" |     c(   )ɔ          ")
                print("_|__                    ")
            elif count == 5:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (o  <  o)         ")
                print(" |     c(   )ɔ          ")
                print("_|__     ^              ")
            elif count == 6:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (x  <  x)         ")
                print(" |     c(   )ɔ          ")
                print("_|__     ^ ^            ")
        elif letter_guess in phrase:
            os.system("clear")
            if count == 0:
                print("  ________              ")
                print(" |        |             ")
                print(" |                      ")
                print(" |                      ")
                print("_|__                    ")
            elif count == 1:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (o  <  o)         ")
                print(" |                      ")
                print("_|__                    ")
            elif count == 2:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (o  <  o)         ")
                print(" |      (   )           ")
                print("_|__                    ")
            elif count == 3:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (o  <  o)         ")
                print(" |     c(   )           ")
                print("_|__                    ")
            elif count == 4:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (o  <  o)         ")
                print(" |     c(   )ɔ          ")
                print("_|__                    ")
            elif count == 5:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (o  <  o)         ")
                print(" |     c(   )ɔ          ")
                print("_|__     ^              ")
            elif count == 6:
                print("  ________              ")
                print(" |        |             ")
                print(" |    (x  <  x)         ")
                print(" |     c(   )ɔ          ")
                print("_|__     ^ ^            ")
        if count == 6:
            print("Sorry, you're out of guesses!")
            print("The word was {}".format(phrase))      
    
def main(path):
    final = read_words(path)
    play_game(final)
    
    
if __name__ == '__main__':
    main('words_by_category.txt')
    


