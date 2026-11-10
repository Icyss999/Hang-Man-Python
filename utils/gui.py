def clear_screen():
    for i in range(30):
        print()

def draw_hangman(wrong):
    head = " "
    body = " "
    left_arm = " "
    right_arm = " "
    left_leg = " "
    right_leg = " "

    if wrong >= 1:
        head = "O"
    if wrong >= 2:
        body = "|"
    if wrong >= 3:
        left_arm = "<"
    if wrong >= 4:
        right_arm = ">"
    if wrong >= 5:
        left_leg = "("
    if wrong >= 6:
        right_leg = ")"

    print("  +----+")
    print("  |    |")
    print("  |    " + head)
    print("  |   " + left_arm + body + right_arm)
    print("  |   " + left_leg + " " + right_leg)
    print("  |")
    print("=========")

def format_time(seconds):
    minutes = seconds // 60
    secs = seconds % 60

    if minutes < 10:
        min_text = "0" + str(minutes)
    else:
        min_text = str(minutes)

    if secs < 10:
        sec_text = "0" + str(secs)
    else:
        sec_text = str(secs)

    return min_text + ":" + sec_text

def mask_word(word, guessed_letters):
    masked = ""
    for ch in word:
        if ch == " " or ch == "-":
            masked = masked + ch + " "
        elif ch in guessed_letters:
            masked = masked + ch + " "
        else:
            masked = masked + "_ "
    return masked

def print_hint(hint):
    width = 50
    prefix = "Hint: "
    rest = hint.strip()

    while len(rest) > width:
        cut = rest.rfind(" ", 0, width)
        if cut <= 0:
            cut = width
        print(prefix + rest[0:cut])
        prefix = "      "
        rest = rest[cut:].strip()
    print(prefix + rest)