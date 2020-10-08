from pytezos import pytezos
import json
pytezos = pytezos.using( key = "edskRkWyj8xhpUv8ge1B3hQHGki2AtvFox86AVKbftajP7t6Sd3npdGdAYDdpZvoqbvTn5vi1ytFL58B4RmHN7oeQAEh695C3Y" , shell = "carthagenet")
print(pytezos)
def transferRewardsToContractDelegator(rewardEarners):
    for rewardee in rewardEarners:
        targetContract = pytezos.contract(rewardee['address'])
        op = targetContract.getRewardsFromBaker(None).with_amount(rewardee['amount']).operation_group.autofill().sign().preapply()
        op = targetContract.getRewardsFromBaker(None).with_amount(rewardee['amount']).operation_group.autofill().sign().inject(_async=False)
        print(op)


rewardEarners = [{'address' : 'KT1TCHBCrJKdvsLULSRQwdi363CzCPbjnnDr' , 'amount' : 1000 }, {'address' : 'KT1B3J5EHQM92GZH9hRJjAn7Rab16unLoHLx' ,'amount':500}]

transferRewardsToContractDelegator(rewardEarners)