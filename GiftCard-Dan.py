#declaring variables
gift_card = 50
games = 35
MT_1 = 3
MT_2 = 4
MT_3 = 6

print("The balance of the card is ${}".format(gift_card))

total_cost = games + MT_1 + MT_2 + MT_3

print("After buying the game and 3 micro transactions, the gift card balance is now ${}".format(gift_card - total_cost))
