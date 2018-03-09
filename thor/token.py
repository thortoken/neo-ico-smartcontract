"""
Basic settings for an NEP5 Token and crowdsale
"""

from boa.interop.Neo.Storage import *

TOKEN_NAME = 'Thor Token'

TOKEN_SYMBOL = 'THOR'

TOKEN_DECIMALS = 8

# This is the script hash of the address for the owner of the token
# This can be found in ``neo-python`` with the walet open, use ``wallet`` command
TOKEN_OWNER = b'\xcd\xe5\xd2\xde\xad\xcc\xec\x05"\x9e\xe7\x0c\x0e\xd1\xdf\xf7GaL$'

TOKEN_CIRC_KEY = b'in_circulation'

TOKEN_TOTAL_SUPPLY = 100000000 * 100000000  # 100m total supply * 10^8 (decimals)

TOKEN_INITIAL_AMOUNT = 50000000 * 100000000  # 50M to owners * 10^8 

# for now assume 1 dollar per token, and one neo = 100 dollars * 10^8
TOKENS_PER_NEO = 100 * 100000000
TOKENS_PER_NEO_LIMITED_ROUND = 125 * 100000000
TOKENS_PER_NEO_SECOND_ROUND = 110 * 100000000

# for now assume 1 dollar per token, and one gas = 30 dollars * 10^8
TOKENS_PER_GAS = 30 * 100000000
TOKENS_PER_GAS_LIMITED_ROUND = 38 * 100000000
TOKENS_PER_GAS_SECOND_ROUND = 33 * 100000000

# when to start the crowdsale (About 100 blocks before the actual starting time)
# BLOCK_SALE_START = 2012000 # mainnet
BLOCK_SALE_START = 1236562 # testnet
# BLOCK_SALE_START = 1 # privnet

# when to end the initial limited round 24 hours (21 sec/block) 24 * 60 * 60 / 21
# LIMITED_ROUND_END = 2012000 + 4114 # mainnet
LIMITED_ROUND_END = 1236562 + 200 # testnet
# LIMITED_ROUND_END = 2330 # privnet

# when to end the tokensale - 30 days after the end of limited round (21 sec/block) 24 * 60 * 60 * 30 / 21
# BLOCK_SALE_END = 2012000 + 123428 # mainnet
BLOCK_SALE_END = 1236562 + 123428 # testnet
# BLOCK_SALE_END = 2400 # privnet

KYC_KEY = b'kyc_ok'

ICO_IN_PROGRESS_KEY = b'ico_in_progress'

ICO_TOKEN_SOLD_KEY = b'token_sold_in_ico'

# maximum amount you can mint in the limited round 2000 tokens per person ($1/token)
# Note: Bonus is calcuated differently based on anount of token sold so far, see
# crowdsale.py => exchange_token for details. below keys are used in that.
MAX_EXCHANGE_LIMITED_ROUND = 2000 * 100000000

LIMITED_ROUND_KEY = b'r1'

AFTER_LIMITED_ROUND_AMOUNT = 12500000 * 100000000

AFTER_SECOND_ROUND_AMOUNT = 18000000 * 100000000

def add_to_circulation(ctx, amount):
    """
    Adds an amount of token to circlulation

    :param amount: int the amount to add to circulation
    """

    current_supply = Get(ctx, TOKEN_CIRC_KEY)

    current_supply += amount
    Put(ctx, TOKEN_CIRC_KEY, current_supply)
    return True


def get_circulation(ctx):
    """
    Get the total amount of tokens in circulation
    The extra addition is a workaround to get the correct numerical value printed

    :return:
        int: Total amount in circulation
    """
    in_circ = Get(ctx, TOKEN_CIRC_KEY)

    available = TOKEN_TOTAL_SUPPLY - in_circ

    in_circ = TOKEN_TOTAL_SUPPLY - available

    return in_circ


def add_to_ico_token_sold(ctx, amount):
    """
    Adds an amount of token to ico_token_sold

    :param amount: int the amount to add to ico_token_sold
    """

    current_sold = Get(ctx, ICO_TOKEN_SOLD_KEY)

    current_sold += amount
    Put(ctx, ICO_TOKEN_SOLD_KEY, current_sold)
    return True

def get_ico_token_sold(ctx):
    """
    Get the total amount of tokens in ico_token_sold
    The extra addition is a workaround to get the correct numerical value printed

    :return:
        int: Total amount in ico_token_sold
    """
    current_sold = Get(ctx, ICO_TOKEN_SOLD_KEY)

    available = TOKEN_TOTAL_SUPPLY - current_sold

    current_sold = TOKEN_TOTAL_SUPPLY - available

    return current_sold
