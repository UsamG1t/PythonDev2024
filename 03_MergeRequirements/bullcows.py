import random
import cowsay
import sys
import io

MyCow = cowsay.read_dot_cow(io.StringIO("""
$the_cow = <<EOC;
         $thoughts
          $thoughts
           ______
          (/\\  /\\)
          (\\/  \\/)
          (  **  )
          ( WWWW )
          ( MMMM )
           ------

.
EOC
"""))


def ask(prompt: str, valid: list[str] = None) -> str:
    while True:
        word = input(cowsay.cowsay(prompt, cowfile = MyCow))
        # word = input(cowsay.cowsay(prompt, cow = cowsay.get_random_cow()))
        if not valid or word in valid:
            break
    return word

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(cowsay.cowsay(format_string.format(bulls, cows), cow = cowsay.get_random_cow()))

def bullcows(guess: str, secret: str) -> (int, int):
    bulls = cows = 0
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return (bulls, cows)

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = guess = ""
    length = 5 if len(sys.argv) == 2 else int(sys.argv[2])
    while len(secret) != length:
        secret = random.choice(words)
    try_count = 0

    while guess != secret:
        guess = ask("Введите слово: ", words)
        b, c = bullcows(guess, secret)
        inform("Быки: {}, Коровы: {}", b, c)
        try_count += 1

    return try_count


with open(sys.argv[1], 'r') as f:
    words = f.read().split('\n')    
print(gameplay(ask, inform, words))