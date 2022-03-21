import mysql.connector as conn

# geckos is a list of token public keys. None if it is not used.
class Helper(object):
    def __init__(self, conn_obj, db_name):
        self.cursor = conn_obj.cursor()
        self.conn = conn_obj
        self.cursor.execute("USE {}".format(db_name))

    def close(self):
        self.cursor.close()
        self.conn.close()


    def getTokenByQrId(self,qr_id):
        _query = "SELECT * FROM `prodtable` WHERE qr_id='{0}'".format(qr_id)
        self.cursor.execute(_query)
        print(self.cursor.rowcount)
        token_id, qr_id, ipfs_link, is_minted, owner_address, is_being_minted, tx_id = self.cursor.fetchall()[0]
        return (token_id, qr_id, ipfs_link, is_minted, owner_address, is_being_minted, tx_id)

    def mintTokenByQrID(self,qr_id,owner_address,tx_hash):
        _queryMINTED = "UPDATE `prodtable` SET `is_being_minted`='TRUE',`owner_address`='{0}',`tx_id`='{2}' WHERE `qr_id`='{1}'".format(owner_address, qr_id,tx_hash)
        # _queryOWNER = "UPDATE FROM `prodtable` SET `owner_address`='{0}' WHERE `qr_id`='{1}'".format(owner_address,qr_id)
        self.cursor.execute(_queryMINTED)
        # self.cursor.execute(_queryOWNER)
        self.conn.commit()      

    def mintToken(self,qr_id):
        _queryMINTED = "UPDATE `prodtable` SET `is_minted`='TRUE' WHERE `qr_id`='{0}'".format( qr_id)
        # _queryOWNER = "UPDATE FROM `prodtable` SET `owner_address`='{0}' WHERE `qr_id`='{1}'".format(owner_address,qr_id)
        self.cursor.execute(_queryMINTED)
        # self.cursor.execute(_queryOWNER)
        self.conn.commit()      
        

    def setTxHashByQrID(self,qr_id,tx_hash):
        _queryTx = "UPDATE `prodtable` SET `tx_id`='{0}' WHERE `qr_id`='{1}'".format(tx_hash, qr_id)
        self.cursor.execute(_queryTx)
        self.conn.commit()      
        