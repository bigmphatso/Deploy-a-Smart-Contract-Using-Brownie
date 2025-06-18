from brownie import accounts, config, yourcontract_name, network
from dotenv import load_dotenv
import os

# NOTE: yourcontract_name is a placeholder that should be replaced with your real contract placed in directory contracts/

load_dotenv()

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_contract():
    account = get_account()
    print(f"We're using the account: {account}")
    print("Deploying to Sepolia...")

    brds_contract = yourcontract_name.deploy({"from": account})
    print(f"Smart Contract Deployed at: {brds_contract.address}")


def main():
    deploy_contract()
