correct = input()
incorrect = input()

steps = 0
outer_index = 0
for i in range(min(len(correct), len(incorrect))):
    if correct[i] == incorrect[i]:
        outer_index += 1
        continue
    else:
        break

print(len(correct) - outer_index + len(incorrect) - outer_index)



    


