import json

ranges= [0,200, 1000, 10000, 1000000]

def get_range_of_balance(balance):
    for thresold in ranges:
        if balance>thresold:
            return thresold


with open('wallet_balance.json', 'r') as f:
    wallet_balance= json.loads(f.read())

distribution= {0:0,
    200:0,
    1000:0,
    10000:0,
   100000:0}

for wallet, balance in wallet_balance.items():
    thresold= get_range_of_balance(balance)
    distribution[thresold]+=1


