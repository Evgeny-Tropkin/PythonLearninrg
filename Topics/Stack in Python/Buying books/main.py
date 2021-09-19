count = int(input())
actions = [None]
for _ in range(count):
    current_action = input()
    if current_action.startswith("READ"):
        printed_action = actions.pop()[4::]
        print(printed_action)
    else:
        actions.append(current_action)
