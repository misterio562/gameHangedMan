import random
import os
from drawHangedMan import drawHangedMan

words = ["PESCADO", "CALAMAR", "PULPO", "TIBURON", "ALMEJA", "CANGREJO"]


def selectWord(listWords):
    word = random.choice(listWords)
    return word


def letterEmpty(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    print(result)


def guessWord(word):

    guessed_letters = []
    attempts = 0

    while True:

        letterEmpty(word, guessed_letters)

        riddle = input("Adivina la letra o la palabra completa: ").upper()

        if len(riddle) == 1:
            if riddle in guessed_letters:
                os.system('clear')
                print(
                    "Ya adivinaste esta letra                   Intentos: ", attempts+1, "/7")
                drawHangedMan(attempts)

            elif riddle not in word:
                os.system('clear')
                print(
                    "La letra no está en la palabra, intenta otra vez                   Intentos: ", attempts+1, "/7")
                attempts += 1
                drawHangedMan(attempts)
                if attempts == 7:
                    print("La palabra correcta era: ", word)
                    break
            else:
                os.system('clear')
                print(
                    "¡Bien hecho!, la letra está en la palabra                   Intentos: ", attempts+1, "/7")
                drawHangedMan(attempts)
                guessed_letters.append(riddle)
                
        elif len(riddle) == len(word):
            if riddle == word:
                os.system('clear')
                drawHangedMan(attempts)
                wordWithSpace = " ".join(word)
                print(wordWithSpace)
                print("¡Felicidades!, has adivinado la palabra")
                break
            else:
                os.system('clear')
                print(
                    "La palabra no es correcta, intenta de nuevo                   Intentos: ", attempts+1, "/7")
                attempts += 1
                drawHangedMan(attempts)
                if attempts == 7:
                    print("La palabra correcta era: ", word)
                    break
        else:
            os.system('clear')
            print(
                "Palabra incorrecta, intentalo de nuevo                    Intentos: ", attempts+1, "/7")
            attempts += 1
            drawHangedMan(attempts)
            if attempts == 7:
                print("La palabra correcta era: ", word)
                break

    response = input("¿Quieres volver a intentarlo? S/N: ").upper()
    if response == "S":
        os.system('clear')
        playGame()
    else:
        print("¡Gracias por jugar <3!")


def playGame():
    word = selectWord(words)
    guessWord(word)


if __name__ == "__main__":
    playGame()
