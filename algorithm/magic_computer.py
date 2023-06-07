import random

deck = ['A_C', 'A_D', 'A_H', 'A_S', '2_C', '2_D', '2_H', '2_S', '3_C', '3_D', '3_H', '3_S', '4_C', '4_D', '4_H', '4_S', \
'5_C', '5_D', '5_H', '5_S', '6_C', '6_D', '6_H', '6_S', '7_C', '7_D', '7_H', '7_S', '8_C', '8_D', '8_H', '8_S', '9_C', '9_D', '9_H', '9_S', \
'10_C', '10_D', '10_H', '10_S', 'J_C', 'J_D', 'J_H', 'J_S', 'Q_C', 'Q_D', 'Q_H', 'Q_S', 'K_C', 'K_D', 'K_H', 'K_S']


def ComputerAssistant():
    print("Cards are character strings as shown below.")
    print("Ordering is {}".format(deck))
    cards, card_index, card_suits, card_numbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    i = 0
    while len(cards) != 5:
        index = random.randint(0, 51)
        card = deck[index]
        if card in cards:
            continue
        card_index.append(index)
        cards.append(card)
        card_suits.append(card_index[i] % 4)
        card_numbers.append((card_index[i] // 4) + 1)
        numsuits[card_index[i] % 4] += 1
        if numsuits[card_index[i] % 4] > 1:
            pairsuit = card_index[i] % 4
        i += 1
    cardh = []
    for i in range(5):
        if card_suits[i] == pairsuit:
            cardh.append(i)
    hidden, open, distance = outputFirstCard(card_numbers, cardh, cards)
    leftover = []
    for i in range(5):
        if (i != hidden) and (i != open):
            leftover.append(card_index[i])
    sortList(leftover)
    outputNext3Cards(leftover, distance)
    guess = input("What is the hidden card?")
    print(cards[hidden])
    if guess == cards[hidden]:
        print("You are a Mind Reader Extraordinaire!")
    else:
        print("Sorry, not impressed!")


def outputFirstCard(cn, ch, cards):
    distance = (cn[ch[0]] - cn[ch[1]]) % 13
    if distance < 7:
        hidden = ch[0]
        open = ch[1]
    else:
        hidden = ch[1]
        open = ch[0]
        distance = (cn[ch[1]] - cn[ch[0]]) % 13
    print("\nFirst card is: {}".format(cards[open]))
    return hidden, open, distance

def sortList(tlist):
    for i1 in range(0, len(tlist)-1):
        i2 = i1
        for i in range(i1+1, len(tlist)):
            if tlist[i2] > tlist[i]:
                i2 = i
        tlist[i1], tlist[i2] = tlist[i2], tlist[i1]

def outputNext3Cards(lo, distance):
    if distance == 1:
        s, t, f = lo[0], lo[1], lo[2]
    elif distance == 2:
        s, t, f = lo[0], lo[2], lo[1]
    elif distance == 3:
        s, t, f = lo[1], lo[0], lo[2]
    elif distance == 4:
        s, t, f = lo[1], lo[2], lo[0]
    elif distance == 5:
        s, t, f = lo[2], lo[0], lo[1]
    else:
        s, t, f = lo[2], lo[1], lo[0]
    print("Second card is: {}".format(deck[s]))
    print("Third card is: {}".format(deck[t]))
    print("Fourth card is: {}".format(deck[f]))

ComputerAssistant()
