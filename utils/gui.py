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
