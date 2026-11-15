total_chores = 4
original_count = total_chores
print(f"you have {total_chores} to complete today")
completed_count = 0
chore_num = 1
while chore_num <= total_chores:
    next_chore = ""
    if chore_num == 1:
        next_chore = "make your bed"
    elif chore_num == 2:
        next_chore = "make the project"
    elif chore_num == 3:
        next_chore = "go to market"
    else:
        next_chore = "read a book"
    answer = input(f"have you completed: {next_chore}(yes/no)")
    if answer == "yes":
        completed_count = completed_count + 1
        chore_num = chore_num + 1
print("===ALL CHORES COMPLETED===")
print(f"remaning chores:{total_chores - completed_count} ")
print(f"completed chores: {completed_count}")
