# from numpy.ma.core import maximum
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)


def find_winner(bid_dictionary):
    winner = ""
    maximum_bid = 0
    for key in bid_dictionary:
        if bid_dictionary[key] > maximum_bid:
            winner = key
            maximum_bid = bid_dictionary[key]


    print(f"{winner} is the winner with bid of ${maximum_bid}.")

flag = False

bidding_dictionary = {}
while not flag:


    names = input("Enter your name:\n")
    bid = int(input("Enter the bid amount:\n"))



    bidding_dictionary[names] = bid


    more_bidder_present = input("Type \'yes\' if there is another bidder else type \'no\' \n").lower()
    if more_bidder_present == "no":
        flag = True
        find_winner(bidding_dictionary)
    else:
        print("\n" * 20)



