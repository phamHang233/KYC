import json
import time
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

from src.databases.mongodb_etl import MongoDB as ETL
from src.databases.mongodb_klg import MongoDB as KLG

from src.databases.postgresql import PostgresDB

postgres_db = PostgresDB()
mongo_etl = ETL(db_prefix='ethereum')
mongo_klg = KLG()
# provider_uri = "https://rpc.ankr.com/eth"

# _w3 = Web3(HTTPProvider(provider_uri))
# _w3.middleware_onion.inject(geth_poa_middleware, layer=0)
#
#
# def check_address(address):
#     return Web3.isAddress(address)
#
#
# def checksum_address(address):
#     return Web3.toChecksumAddress(address)


# def is_contract(address):
#     code = _w3.eth.getCode(checksum_address(address))
#     code_str = code.hex()
#     if code_str == '0x':
#         return False
#     else:
#         return True

start_block = mongo_etl.get_block_number_from_timestamp({
    'timestamp': {
        '$lte': time.time() - 3600 * 24*7
        }
    })

# def get_token_addr(chain_id):
#     token_info= mongo_klg.get_top_token(chain_id)
#     token_addrs={}
#     for info in token_info:
#         address = info['address']
#         token_addrs[address]= info
#     with open('token_address.json', 'w') as f:
#         json.dump(token_addrs, f)


cursors= mongo_etl.get_documents('transactions', {'block_number': {
        '$gte'> start_block
        }})
print("get all transaction")

wallets =[]
wallet_balance= {}
miss_balance_wallet=[]
count_number=0
for cursor in cursors:
    wallet = cursor['from_address']
    if wallet not in wallets:
        count_number+=1
        wallets.append(wallet)
        if count_number%10000==0:
            print(f'get {count_number} wallet')


with open('wallet_list.json', 'w') as f:
    json.dump(wallets, f )

print('get all wallets')
for wallet in wallets:
    info = mongo_klg.get_wallets_info(wallet)
    if info is not None and 'balanceInUSD' in info:
        wallet_balance[wallet] = info['balanceInUSD']
    else:
        miss_balance_wallet.append(wallet)
with open('wallet_balance.json', 'w') as f:
    json.dump(wallet_balance, f)
# get_token_addr('0x1')
#
