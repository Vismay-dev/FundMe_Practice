from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAINS

def deploy_fund_me():
    account = get_account()

    if(network.show_active() not in LOCAL_BLOCKCHAINS):
        priceFeedAddress = config['networks'][network.show_active()]['eth_usd_priceFeed']
    else:
        deploy_mocks()
        priceFeedAddress = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
            priceFeedAddress,
            {'from':account}, publish_source = config['networks'][network.show_active()].get('verify'))
    
    print(f'Contract deployed to {fund_me.address}')

    return fund_me

def main():
    deploy_fund_me()


