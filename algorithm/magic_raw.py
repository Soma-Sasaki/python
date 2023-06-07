deck = ['A_C', 'A_D', 'A_H', 'A_S', '2_C', '2_D', '2_H', '2_S', '3_C', '3_D', '3_H', '3_S', '4_C', '4_D', '4_H', '4_S', \
'5_C', '5_D', '5_H', '5_S', '6_C', '6_D', '6_H', '6_S', '7_C', '7_D', '7_H', '7_S', '8_C', '8_D', '8_H', '8_S', '9_C', '9_D', '9_H', '9_S', \
'10_C', '10_D', '10_H', '10_S', 'J_C', 'J_D', 'J_H', 'J_S', 'Q_C', 'Q_D', 'Q_H', 'Q_S', 'K_C', 'K_D', 'K_H', 'K_S']


def AssistantOrdersCards():
    print("Cards are character strings as shown below.")
    print("Ordering is {}".format(deck))
    cards, card_index, card_suits, card_numbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    i = 0
    while len(cards) != 5:
        print("Please give card {}".format(i+1), end= " ")
        card = input("in above format")
        if card not in deck:
            print("Error!")
            continue
        if card in cards:
            print("Error!")
            continue
        cards.append(card)
        i += 1
        n = deck.index(card)
        card_index.append(n)
        card_suits.append(n % 4)
        card_numbers.append((n // 4) + 1)
        numsuits[n % 4] += 1
        if numsuits[n % 4] > 1:
            pairsuit = n % 4
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

AssistantOrdersCards()

def MagicianGuessCard():
    i = 0
    cards, card_index = [], []
    while len(cards) != 4:
        print("Please give card {}".format(i+1), end=" ")
        card = input("in above format")
        if card not in deck:
            print("Error!")
            continue
        if card in cards:
            print("Error!")
            continue
        cards.append(card)
        n = deck.index(card)
        card_index.append(n)
        if i == 0:
            suit = n % 4
            number = (n // 4) + 1
        i += 1
    if (card_index[1] < card_index[2]) and (card_index[1] < card_index[3]):
        if card_index[2] < card_index[3]:
            distance = 1
        else:
            distance = 2
    elif ((card_index[1] < card_index[2]) and c(ard_index[1] > card_index[3])) or ((card_index[1] > card_index[2]) and (card_index[1] < card_index[3])):
        if card_index[2] < card_index[3]:
            distance = 3
        else:
            distance = 4
    elif (card_index[1] > card_index[2]) and (card_index[1] > card_index[3]):
        if card_index[2] < card_index[3]:
            distance = 5
        else:
            distance = 6
    print(number, distance, suit)
    hiddennumber = (number + distance) % 13
    index = (hiddennumber - 1) * 4 + suit
    print(index)
    print("Hidden card is: {}".format(deck[index]))

MagicianGuessCard()
