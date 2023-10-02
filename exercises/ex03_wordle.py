"""Structured Wordle."""
__author__ = "730670385"

def main() -> None:
    """The entrypoint of the program and the main game loop."""
    user_turns: int = 1
    secret_word: str = "codes"
    user_guess: str = ""
    win: bool = False
    while not win and user_turns < 7:
        print(f"=== Turn {user_turns}/6 ===")
        user_guess = input_guess(len(secret_word))
        if user_guess == secret_word:
            print(emojified(user_guess, secret_word))
            win = True
        else:
            print(emojified(user_guess, secret_word))
            user_turns = user_turns + 1
    if not win and user_turns == 7:
        print("X/6 - Sorry, try again tomorrow!")
    if win:
        print(f"You won in {user_turns}/6 turns!")


def contains_char(str_search: str, chr_search: str) -> bool:
    """Searches an input string for an input character at any index and returns T or F."""
    assert len(chr_search) == 1
    i: int = 0
    while i < len(str_search):
        if chr_search == str_search[i]:
            return True
        i += 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Gaining the T or F values from contains_chr and concatenating the box emojis."""
    wordle_boxes: str = ""
    secret_indice: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(user_guess) == len(secret_word)
    while secret_indice < len(secret_word):
        if user_guess[secret_indice] == secret_word[secret_indice]:
            wordle_boxes = wordle_boxes + GREEN_BOX
        else:
            if contains_char(secret_word, user_guess[secret_indice]):
                wordle_boxes = wordle_boxes + YELLOW_BOX
            else:
                wordle_boxes = wordle_boxes + WHITE_BOX
        secret_indice += 1
    return wordle_boxes

def input_guess(expected_length: int) -> str:
    """Given a user input, checks that input with length of secret word. Returns user word of correct length."""
    user_word: str = input(f"Enter a {expected_length} character word: ")
    if len(user_word) == expected_length:
        return user_word
    else:
        while len(user_word) != expected_length:
            user_word = input(f"That was not {expected_length} chars! Try Again: ")
        return user_word

if __name__ == "__main__":
    main()