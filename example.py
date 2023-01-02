mel = []
chels = []
max = []

card_players = [mel, chels, max]

cards = [
    "2 of Hearts",
    "3 of Hearts",
    "4 of Hearts",
    "5 of Hearts",
    "6 of Hearts",
    "7 of Hearts",
    "8 of Hearts",
    "9 of Hearts",
    "10 of Hearts",
    "Jack of Hearts",
    "Queen of Hearts",
    "King of Hearts",
    "Ace of Hearts"
    ]


def deal_cards():
    while len(cards) >= 1:
        for player in card_players:
            try:
                player.append(cards.pop(0))
            except IndexError:
                break

deal_cards()
print(f"Mel's cards: {mel}")
print(f"Chels' cards: {chels}")
print(f"Max's cards: {max}")
