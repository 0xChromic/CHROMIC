from flask import Flask
from flask import render_template
from flask_cors import CORS, cross_origin
from sql_queries import Helper
import mysql.connector as conn
from web3 import Web3
import json
import os

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


with app.app_context():


   INFURA = os.environ.get("INFURA")

   w3 = Web3(Web3.HTTPProvider(INFURA))

   db = conn.connect(
       host= os.environ.get("HOST"),
       user= os.environ.get("DB_USERNAME"),
       password=("DB_PASSWORD"),
       port=("DB_PORT"),
    )

   PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

   PUBLIC_KEY = os.environ.get("PUBLIC_KEY")

   ABI = json.loads('[ { "inputs": [ { "internalType": "address", "name": "minter_", "type": "address" } ], "name": "addMinter", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "approved", "type": "address" }, { "indexed": true, "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "operator", "type": "address" }, { "indexed": false, "internalType": "bool", "name": "approved", "type": "bool" } ], "name": "ApprovalForAll", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "approve", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "grantRole", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "string", "name": "symbol", "type": "string" }, { "internalType": "string", "name": "tokenURI_", "type": "string" } ], "name": "initialize", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to_", "type": "address" } ], "name": "mint", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "minter_", "type": "address" } ], "name": "removeMinter", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "renounceRole", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "revokeRole", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "indexed": true, "internalType": "bytes32", "name": "previousAdminRole", "type": "bytes32" }, { "indexed": true, "internalType": "bytes32", "name": "newAdminRole", "type": "bytes32" } ], "name": "RoleAdminChanged", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "indexed": true, "internalType": "address", "name": "account", "type": "address" }, { "indexed": true, "internalType": "address", "name": "sender", "type": "address" } ], "name": "RoleGranted", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "indexed": true, "internalType": "address", "name": "account", "type": "address" }, { "indexed": true, "internalType": "address", "name": "sender", "type": "address" } ], "name": "RoleRevoked", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" }, { "internalType": "bytes", "name": "_data", "type": "bytes" } ], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "operator", "type": "address" }, { "internalType": "bool", "name": "approved", "type": "bool" } ], "name": "setApprovalForAll", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": true, "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "transferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "newURI", "type": "string" } ], "name": "updateMetadata", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "DEFAULT_ADMIN_ROLE", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "getApproved", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" } ], "name": "getRoleAdmin", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "getRoleMember", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" } ], "name": "getRoleMemberCount", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes32", "name": "role", "type": "bytes32" }, { "internalType": "address", "name": "account", "type": "address" } ], "name": "hasRole", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "operator", "type": "address" } ], "name": "isApprovedForAll", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "METADATA_ROLE", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "MINTER_ROLE", "outputs": [ { "internalType": "bytes32", "name": "", "type": "bytes32" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "tokenId", "type": "uint256" } ], "name": "ownerOf", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes4", "name": "interfaceId", "type": "bytes4" } ], "name": "supportsInterface", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "tokenByIndex", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "uint256", "name": "index", "type": "uint256" } ], "name": "tokenOfOwnerByIndex", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "tokenID", "type": "uint256" } ], "name": "tokenURI", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" } ]')

   CHAINLINK_ABI = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'

   CONTRACT_ADDR= os.environ.get("CONTRACT_ADDRESS")

   CHAINLINK_ORACLE_ADDR = os.environ.get("CHAINLINK_ORACLE_ADDRESS")

   ChainlinkOracle = web3.eth.contract(address=CHAINLINK_ORACLE_ADDR, abi=CHAINLINK_ABI)

   HelperNFT = w3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDR), abi=ABI)

   CHAINID = os.environ.get("CHAIN_ID")

   gh = Helper(db, "defaultdb")

   lastCheckedPrice = 1


@app.route("/")
@cross_origin()
def hello_world():
    return "hello world"


@app.route("/mint/<qr_id>/<address>", methods = ['GET','POST'])
@cross_origin()
def mint(qr_id,address):
    gh = Helper(db, "defaultdb")
    
    qr_id, token_id, ipfs_link, is_minted, owner_address, is_being_minted, tx_hash = gh.getTokenByQrId(qr_id)
    
    if is_minted == "FALSE":
        # PRECOMPUTE HASH
        signed_mint_tx = mintTransaction(address)
        # block DB Values
        txhash = w3.toHex(w3.keccak(signed_mint_tx.rawTransaction))
        gh.mintTokenByQrID(qr_id, str(address), str(txhash))

        # send signed mint transaction
        hashs =w3.toHex(w3.eth.send_raw_transaction(signed_mint_tx.rawTransaction))

        gh.mintToken(qr_id)

    # getValuesBackImmediately
    qr_id, token_id, ipfs_link, is_minted, owner_address, is_being_minted, tx_hash = gh.getTokenByQrId(qr_id)


    return {
        "qr_id": qr_id,
        "token_id": token_id,
        "ipfs_link": ipfs_link,
        "owner_address": owner_address,
        "tx_hash": tx_hash,
        "is_minted": is_minted,
        "is_being_minted": is_being_minted,
    }

def mintTransaction(owner_address):
    gh = Helper(db, "defaultdb")
    addr = Web3.toChecksumAddress(str(owner_address))
    nonce = w3.eth.get_transaction_count(PUBLIC_KEY) 
    print(nonce)
    mint_tx = HelperNFT.functions.mint(addr).buildTransaction({
                                                'chainId': CHAINID,
                                                'gas': 300000,
                                                'gasPrice': w3.toWei('35', 'gwei'),
                                                'nonce': nonce,
                                            })
    signed_tx = w3.eth.account.sign_transaction(mint_tx, private_key=PRIVATE_KEY)
    return signed_tx

@app.route("/<qr_id>", methods = ['GET','POST'])
@cross_origin()
def get(qr_id):

    qr_id, token_id, ipfs_link, is_minted, owner_address, is_being_minted, _ = gh.getTokenByQrId(qr_id)

    return {
        "qr_id": qr_id,
        "token_id": token_id,
        "ipfs_link": ipfs_link,
        "owner_address": owner_address,
        "is_minted": is_minted,
        "is_being_minted": is_being_minted,
    }

@app.route("/token/<token_id>", methods = ['GET'])
@cross_origin()
def tokenABI(token_id):

    image_ipfs = imageToDisplay()
    return {
        "description": "CHROMIC NFT EXAMPLE",
        "image": image_ipfs,
        "ipfs_link": ipfs_link,
        "name": "Chromic NFT #" + token_id
    }

def imageToDisplay():
    returns = ChainlinkOracle.functions.latestRoundData().call()
    latestPrice = returns[1]/(10^8)

    difference = latestPrice/lastCheckedPrice

    if difference > 1.05:
        return os.environ.get("INCREASING_IMAGE")
    elif difference < 0.95:
        return os.environ.get("DECREASING_IMAGE")
    else:
        return os.environ.get("NORMAL_IMAGE")



if __name__ == '__main__':
    app.run(debug=True)
