"""Day 4 solution"""
import re
SCRATCHCARDS = [re.sub(r'Card \d+: ', '', line).strip('\n').split('|') for line in open("input.txt", "r").readlines()]  # Add input.txt in the directory
TOTAL_CARDS = len(SCRATCHCARDS)


def get_total_wins(scratchcard):
    winning = scratchcard[0].split()
    numbers = scratchcard[1].split()
    return len(set(winning) & set(numbers))


# Total points
total_1 = 0
for card in SCRATCHCARDS:
    total_winning = get_total_wins(card)
    if total_winning > 0:
        total_1 += 2 ** (total_winning - 1)

# Total scratchcards
i = 0
scratchcards_times = [1] * TOTAL_CARDS
total_2 = 0
while i < TOTAL_CARDS:
    print(f'WORKING WITH SCRATCHCARD {i}')
    total_2 += 1
    total_winning = get_total_wins(SCRATCHCARDS[i])
    for j in range(total_winning):
        scratchcards_times[i + j + 1] += 1
    scratchcards_times[i] -= 1
    if scratchcards_times[i] == 0:
        i += 1

print(f'Total points: {total_1}')
print(f'Total scratchcards: {total_2}')
