# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo
print(logo)


# Todo3

continue_bidding = 'yes'

bids = {}



# Todo 4
# comparing the price

def find_highest_bidder(bidding_dicionary):
    winner = ""
    # max(bidding_dicionary, key=bidding_dicionary.get)
    let_highest_bid = 0
    for bidder in bidding_dicionary:
        bid_amount = bidding_dicionary[bidder]
        if bid_amount > let_highest_bid:
            let_highest_bid = bid_amount
            winner = bidder


    print(f"The winner is {winner} with a bid of ${let_highest_bid}.")

i = 0
while continue_bidding == 'yes':
    i+=1
# Todo1
    name = input("What is your name?: ")
    price = int(input("What is your Bidding price?: $"))

# Todo2
    bids[name] = price

# Todo3
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 100)
    if continue_bidding == 'no':
        find_highest_bidder(bids)





