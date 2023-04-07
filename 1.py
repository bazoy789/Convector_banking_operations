
def card1(card):
    f = []
    card = card.split(" ")
    card = card[0] + " **" + card[1][17:]
    f.append(card)
    return " ".join(f)

print(card1("Счет 89685546118890842412"))