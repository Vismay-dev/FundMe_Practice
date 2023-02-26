from brownie import network, accounts, config, MockV3Aggregator

DECIMALS = 18
STARTING_PRICE = 2*(10**8)

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]

LOCAL_BLOCKCHAINS = ['development','ganache-local']

def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAINS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_mocks():
    print('Deploying Mocks...')
    if len(MockV3Aggregator) <=0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {'from':get_account()})            
    print('Mocks Deployed!')