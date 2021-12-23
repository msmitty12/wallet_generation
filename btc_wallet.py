from bitcoinaddress import Wallet

wallet = Wallet()

private_key = wallet.key.mainnet.wif
public_key = wallet.address.pubkey
wallet_address = wallet.address.mainnet.pubaddr1

print("private:")
print(private_key)
print("address:")
print(wallet_address)
