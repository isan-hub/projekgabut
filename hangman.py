import random
import sys

WORDS = [
    "python", "komputer", "sekolah", "program", "internet",
    "belajar", "game", "sains", "matematika", "musik"
]

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\  |
    / \  |
        ==="""
]

MAX_WRONG = len(HANGMAN_PICS) - 1

def pick_word():
    return random.choice(WORDS)

def display_state(word, guessed, wrong):
    print(HANGMAN_PICS[wrong])
    shown = " ".join([c if c in guessed else "_" for c in word])
    print("\nKata: ", shown)
    print("Tebakan: ", " ".join(sorted(guessed)))
    print(f"Sisa kesempatan: {MAX_WRONG - wrong}\n")

def main():
    word = pick_word()
    guessed = set()
    wrong = 0

    print("=== Selamat datang di Hangman ===")
    while True:
        display_state(word, guessed, wrong)

        if wrong >= MAX_WRONG:
            print(f"Kamu kalah! Kata yang benar: {word}")
            break

        if all(c in guessed for c in word):
            print(f"Selamat! Kamu berhasil menebak kata: {word}")
            break

        guess = input("Masukkan satu huruf (atau ketik 'exit' untuk keluar): ").lower().strip()
        if not guess:
            continue
        if guess == "exit":
            print("Keluar. Terima kasih sudah bermain!")
            sys.exit(0)
        if len(guess) != 1 or not guess.isalpha():
            print("Masukkan hanya 1 huruf.\n")
            continue

        if guess in guessed:
            print("Kamu sudah menebak huruf itu sebelumnya.\n")
            continue

        if guess in word:
            print("Tepat!\n")
            guessed.add(guess)
        else:
            print("Salah!\n")
            guessed.add(guess)
            wrong += 1

if __name__ == "__main__":
    main()
