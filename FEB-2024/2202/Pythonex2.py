def atm_operation(type_of_money_in_bank, our_money_in_account):
    type_of_money_in_bank.sort(reverse=True) #sort money from high to low value
    our_wallet = [] #our wallet is out of money so we need to withdraw :(
    for money in type_of_money_in_bank:
        while our_money_in_account >= money:
            our_money_in_account -= money #machine give it to us
            our_wallet.append(money) #Store that one into our wallet
    if our_money_in_account != 0:
        raise ValueError("Your input is not valid, try again later")
    return our_wallet #its time to double check our money

# 2 example
print(atm_operation([1, 5, 10, 25, 100], 15))  # Output: [10,5]
print(atm_operation([1, 4, 15, 20, 50], 23))  # Output: [15,4,4]
