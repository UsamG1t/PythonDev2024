import random
import sys

def ask(prompt: str, valid: list[str] = None) -> str:
    while True:
        word = input(prompt)
        if not valid or word in valid:
            break
    return word

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def bullcows(guess: str, secret: str) -> (int, int):
    bulls = cows = 0
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return (bulls, cows)

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = random.choice(words)
    guess = None
    try_count = 0

    while guess != secret:
        guess = ask("Введите слово: ", words)
        b, c = bullcows(guess, secret)
        inform("Быки: {}, Коровы: {}", b, c)
        try_count += 1

    return try_count


with open("eng_words.txt", 'r') as f:
    words = f.read().split('\n')    
print(gameplay(ask, inform, words))