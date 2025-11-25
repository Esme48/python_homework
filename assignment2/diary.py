#Task 1

with open('diary.txt', 'a') as file:
    first_line = input("What happened today?")
    while True:
        second_line = input("What else?")
        if second_line.lower() == 'done for now':
            break
    file.write(first_line + second_line + '\n')