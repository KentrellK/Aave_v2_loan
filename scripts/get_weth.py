from scripts.helpful_scripts import get_account
from brownie import interface, config, network, Wei
from web3 import Web3


def main():
    get_weth()


def get_weth():
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": Wei("0.01 ether")})
    tx.wait(1)
    print("Received 0.1 WETH")
    return tx
