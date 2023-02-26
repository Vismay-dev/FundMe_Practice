from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAINS
from scripts.deploy import deploy_fund_me
from brownie import accounts, exceptions, network

import pytest

def test_can_fund_and_withdraw():

    account = get_account()
    fundMe = deploy_fund_me()
    entranceFee = fundMe.getEntranceFee() + 100

    tx1 = fundMe.fund({'from':account, 'value': entranceFee})
    tx1.wait(1)

    assert fundMe.addressToAmountFunded(account.address) == entranceFee

    tx2 = fundMe.withdraw({'from':account})
    tx2.wait(1)

    assert fundMe.addressToAmountFunded(account.address) == 0

def test_onlyOwner_can_withdraw():

    if(network.show_active() not in LOCAL_BLOCKCHAINS):
        pytest.skip('Only for local testing')

    fundMe = deploy_fund_me()
    badActor = accounts.add()

    with pytest.raises(exceptions.VirtualMachineError):
        fundMe.withdraw({'from':badActor})
    








