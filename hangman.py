def word_get():
    words = open("words.txt", "r")
    lineRead = words.readline()
    word_list = []
    hint_list = []
    i = 0

    while lineRead != "":
        split_words = lineRead.split(", ")
        word_list.append(split_words[0])
        hint_list.append(split_words[1])
        i += 1
        lineRead = words.readline()

    words.close()
    number = random.randint(0, i - 1)
    word_choice = word_list[number]
    # print(word_choice)
    hint = hint_list[number]
    # print(hint)
    return word_choice, hint


def guess_validate(wrong_guesses, word_choice, word_display, guessed):
    guessed_before = False
    user_guess = input("Please guess a letter or the word: ")
    # print(guessed)

    # checks that the letter/word hasn't already been guessed
    for i in range(0, len(guessed)):
        if guessed[i] == user_guess:
            guessed_before = True

    # isaplha() checks that the input is a string made of letter
    if user_guess.isalpha() and not guessed_before:
        guessed.append(user_guess)
        # print(guessed)
        # returns it as upper case
        return user_guess.upper()
    elif guessed_before:
        print("You've already guessed that")
        hangman_guessing(wrong_guesses, word_choice, word_display, guessed)
    else:
        print("Invalid guess")
        hangman_guessing(wrong_guesses, word_choice, word_display, guessed)


def hangman_display(wrong_guesses):
    dead = ['''
              o
             /|\\
              |
             / \\
            ''',
            '''
              o
             /|\\
              |
             / 
            ''',
            '''
              o
             /|\\
              |

            ''',
            '''
              o
             /|
              |

            ''',
            '''
              o
              |
              |

            ''',
            '''
              o
              |
              
             
            ''']

    return dead[wrong_guesses]


def hangman():
    print("---------")
    print(" Hangman")
    print("---------")

    word_choice, hint = word_get()
    word_display = []
    for i in range(0, len(word_choice)):
        word_display.append("_")
        i += 1

    wrong_guesses = 0
    guessed = []
    print(hangman_display(wrong_guesses))
    print(word_display)

    hangman_guessing(wrong_guesses, word_choice, word_display, guessed)


def hangman_guessing(wrong_guesses, word_choice, word_display, guessed):
    while wrong_guesses < 5:
        guessed_letter = False
        user_guess = guess_validate(wrong_guesses, word_choice, word_display, guessed)
        blank = 0
        for i in range(0, len(word_display)):
            if word_display[i] == '_':
                blank += 1
        if blank > 0:
            if len(user_guess) > 1:
                if user_guess == word_choice:
                    print("Congratulations!")
                    print("You guessed the word!")
                    break
                else:
                    print("Incorrect guess!")
                    wrong_guesses += 1
                    print(hangman_display(wrong_guesses))
                    print(word_display)

            else:
                for i in range(0, len(word_choice)):
                    if user_guess == word_choice[i]:
                        print("You guessed a letter!")
                        guessed_letter = True
                        word_display[i] = user_guess

                if not guessed_letter:
                    print("Incorrect guess!")
                    wrong_guesses += 1

                print(hangman_display(wrong_guesses))
                print(word_display)
        else:
            print("Congratulations!")
            print("You guessed the word!")
            break

    print("You had too many wrong guesses and DIED")
    print("Better luck next time!")
