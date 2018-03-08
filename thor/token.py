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

TOKEN_INITIAL_AMOUNT = 50000000 * 100000000  # 50m to owners * 10^8 

# for now assume 1 dollar per token, and one neo = 100 dollars * 10^8
TOKENS_PER_NEO = 100 * 100000000

# for now assume 1 dollar per token, and one gas = 35 dollars * 10^8
TOKENS_PER_GAS = 30 * 100000000

# maximum amount you can mint in the limited round ( 20 neo/person * 100 Tokens/NEO * 10^8 )
MAX_EXCHANGE_LIMITED_ROUND = 20 * 100 * 100000000

# when to start the crowdsale
# To-Do: Update this block time
BLOCK_SALE_START = 2500

# when to end the initial limited round
LIMITED_ROUND_END = 2500 + 5760

# when to end the tokensale - 30 days after the end of limited round
BLOCK_SALE_END = 2500 + 172800

ICO_IN_PROGRESS_KEY = b'ico_in_progress'

KYC_KEY = b'kyc_ok'

LIMITED_ROUND_KEY = b'r1'

def crowdsale_available_amount(ctx):
    """

    :return: int The amount of tokens left for sale in the crowdsale
    """

    in_circ = Get(ctx, TOKEN_CIRC_KEY)

    available = TOKEN_TOTAL_SUPPLY - in_circ

    return available


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

    :return:
        int: Total amount in circulation
    """
    return Get(ctx, TOKEN_CIRC_KEY)
