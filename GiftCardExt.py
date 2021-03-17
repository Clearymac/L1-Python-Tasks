#declaring variables
gift_card = int(input("What is the gift card balance you want to add? "))
games = 35
anime_R34_Skinpack = 3
anime_girl_voicepack = 4
real_anime_texturepack = 6

print("The balance of the card is ${}".format(gift_card))

print("Games are &{}\nThe anime skin pack is ${}\nThe anime girl voice pack is  ${}\nThe realistic anime texturepack is ${}".format(games, anime_R34_Skinpack, anime_girl_voicepack, real_anime_texturepack))

total_cost = anime_girl_voicepack + games + anime_R34_Skinpack + real_anime_texturepack
while gift_card < total_cost:
    print("your gift card balance is too low")
    retard = input("Would you like to top it up?")
    if retard == "no":
        retard = input("Are you sure?")
    elif retard == "yes":
        top_up = input("how much would you like to top up by?")
gift_card = gift_card - total_cost


print("After buying the game and 3 micro transactions, the gift card balance is now ${}".format(gift_card - total_cost))
