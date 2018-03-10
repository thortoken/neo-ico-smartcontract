"""
Thor Token ICO Smart Contract
===================================

Author: Leo Rong
Email: leo@thortoken.com

Date: March 8, 2018

Based on thor NEP-5 ICO template by Thomas Saunders

Date: Jan 29, 2018

"""
from thor.txio import get_asset_attachments
from thor.token import *
from thor.crowdsale import *
from thor.nep5 import *
from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.Neo.Storage import *

ctx = GetContext()
NEP5_METHODS = ['name', 'symbol', 'decimals', 'totalSupply', 'balanceOf', 'transfer', 'transferFrom', 'approve', 'allowance']


def Main(operation, args):
    """

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return:
        bytearray: The result of the operation
    """

    trigger = GetTrigger()

    # This is used in the Verification portion of the contract
    # To determine whether a transfer of system assets ( NEO/Gas) involving
    # This contract's address can proceed
    if trigger == Verification():

        # check if the invoker is the owner of this contract
        is_owner = CheckWitness(TOKEN_OWNER)

        # If owner, proceed
        if is_owner:

            return True

        # Otherwise, we need to lookup the assets and determine
        # If attachments of assets is ok
        attachments = get_asset_attachments()
        return can_exchange(ctx, attachments, True)

    elif trigger == Application():

        for op in NEP5_METHODS:
            if operation == op:
                return handle_nep51(ctx, operation, args)

        if operation == 'deploy':
            return deploy()

        elif operation == 'circulation':
            return get_circulation(ctx)

        elif operation == 'ico_sold':
            return get_ico_token_sold(ctx)

        # the following are handled by crowdsale

        elif operation == 'mintTokens':
            # Add a check to see if ico is paused manually
            if Get(ctx, ICO_IN_PROGRESS_KEY):
                return perform_exchange(ctx)
            return False

        elif operation == 'crowdsale_register':
            return kyc_register(ctx, args)

        elif operation == 'crowdsale_status':
            return kyc_status(ctx, args)

        elif operation == 'airdrop':
            return drop_tokens(ctx, args)

        elif operation == 'pause_ico':
            return change_ico_status(False)

        elif operation == 'start_ico':
            return change_ico_status(True)

        elif operation == 'thor_hammer':
            return True

        return 'unknown operation'

    return False


def deploy():
    """

    :param token: Token The token to deploy
    :return:
        bool: Whether the operation was successful
    """
    if not CheckWitness(TOKEN_OWNER):
        print("Must be owner to deploy")
        return False

    if not Get(ctx, 'initialized'):
        # do deploy logic
        Put(ctx, 'initialized', 1)
        Put(ctx, TOKEN_OWNER, TOKEN_INITIAL_AMOUNT)

        # Default to false - manually flip the switch
        Put(ctx, ICO_IN_PROGRESS_KEY, True) 

        result = add_to_ico_token_sold(ctx, 0)
        result = add_to_circulation(ctx, TOKEN_INITIAL_AMOUNT)

        return True

    return False

def change_ico_status(status):
    """

    :param status: a boolean to switch ico status to live or paused
    :return:
        bool: Whether the operation was successful
    """
    if not CheckWitness(TOKEN_OWNER):
        print("Must be owner to change ico status")
        return False

    Put(ctx, ICO_IN_PROGRESS_KEY, status)
    return True
