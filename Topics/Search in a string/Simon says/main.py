def what_to_do(instructions):
    simon_says = "Simon says"
    action = "I won't do it!"
    if instructions.startswith(simon_says):
        action = "I " + instructions[len(simon_says) + 1::]
    if instructions.endswith(simon_says):
        action = "I " + instructions[:len(instructions) - len(simon_says) - 1:]

    return action
