# Hangman – Python Mini Project

The classic word-guessing game in the terminal. Guess the hidden word one letter at a time before the hangman drawing is complete.

## Features

- Random words from 4 categories (Animals, Fruits, Countries, Programming)
- ASCII-art hangman that grows with each wrong guess
- 6 wrong guesses allowed
- Shows letters already guessed
- Rejects invalid or repeated guesses
- Tracks wins and losses

## How to Run

Make sure you have **Python 3** installed. No extra packages are needed.

```bash
cd hangman
python hangman.py
```

## Example

```
Category: Fruits

  +---+
  O   |
  |   |
      |
     ===

Word: m a _ _ o
Wrong guesses left: 4
Guessed: a, e, m, o, s
Guess a letter:
```

## Add Your Own Words

Edit the `WORDS` dictionary at the top of `hangman.py` to add new categories or words.

## Concepts Used

- `random` module
- Sets
- String methods and `join`
- Loops and conditionals
