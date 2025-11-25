#Task 1

with open('diary.txt', 'a') as file:
    first_line = input("What happened today?")
    file.write(first_line + '\n')
    while True:
        second_line = input("What else?")
        file.write(second_line + '\n')
        if second_line.lower() == 'done for now':
            break