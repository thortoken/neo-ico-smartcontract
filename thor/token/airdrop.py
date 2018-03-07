from boa.blockchain.vm.Neo.Action import RegisterAction
from boa.blockchain.vm.System.ExecutionEngine import GetExecutingScriptHash
from boa.blockchain.vm.Neo.Runtime import Notify,CheckWitness
from thor.token.mytoken import Token
from thor.common.storage import StorageAPI
from boa.code.builtins import range

OnTransfer = RegisterAction('transfer','from', 'to', 'amount')

class Airdrop():

    def airdrop_tokens(self, to_addr, amount, token:Token):
        """

        :param to_addr:single address where token should be airdropped to
        :param amount:amount of token to be airdropped
        :param token:Token A token object with your ICO settings
        :return:
            int: The number of tokens dropped in this invocation
        """
        token_dropped = 0;

        if CheckWitness(token.owner):

            storage = StorageAPI()

            current_in_circulation = storage.get(token.in_circulation_key)

            new_amount = current_in_circulation + amount 

            if new_amount > token.total_supply:
                print("Amount in list would overflow the total supply")
                return False

            sender = GetExecutingScriptHash()

            storage.put(to_addr, amount)

            # dispatch transfer event
            OnTransfer(sender, to_addr, amount)
            token_dropped = amount

            # update the in circulation amount
            token.add_to_circulation(amount, storage)

        return token_dropped
