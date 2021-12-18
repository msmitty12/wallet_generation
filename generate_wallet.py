from bitcoinaddress import Wallet

wallet = Wallet()
print(wallet.key.__dict__)
print(wallet.key.__dict__['mainnet'].__dict__)
print(wallet.key.__dict__['testnet'].__dict__)
print(wallet.address.__dict__)
print(wallet.address.__dict__['mainnet'].__dict__)
print(wallet.address.__dict__['testnet'].__dict__)

private_key = wallet.key.mainnet.wif

wallet_address = wallet.address.mainnet.pubaddr1
public_key = wallet.address.pubkey
print("private")
print(private_key)
print("public")
print(public_key)
print("address")
print(wallet_address)
