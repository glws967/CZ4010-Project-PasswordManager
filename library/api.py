import base64
import json

import pyrebase

from library.crypto import decryptVault, encryptVault, getAuthHash, getKey
from library.usersession import usersession

def getConfig():
    config={"apiKey": "AIzaSyCRrMaXBPx_GVbBJZzaaFsZxEeOGeh13xk",
            "authDomain": "cz4010project.firebaseapp.com",
            "databaseURL": "https://cz4010project-default-rtdb.asia-southeast1.firebasedatabase.app",
            "projectId": "cz4010project",
            "storageBucket": "cz4010project.appspot.com",
            "messagingSenderId": "292722857382",
            "appId": "1:292722857382:web:522e87a4bef65ff4ffab67",
            "measurementId": "G-PHMDGQ089W"}
    return config

def initializeDatabaseConnection():
    firebase = pyrebase.initialize_app(config=getConfig())
    global db 
    db = firebase.database()
        
def login(username, password):
    authHash = getAuthHash(username, password)
    dbAuthHash = str(db.child("CZ4010DB").child("users").child(username).child('authHash').get().val())
    if  dbAuthHash == base64.b64encode(authHash).decode():
        cipher = base64.b64decode(str(db.child("CZ4010DB").child("users").child(username).child('vault').get().val()))
        lock = db.child("CZ4010DB").child("users").child(username).child('lock').get().val()
        clipboard = db.child("CZ4010DB").child("users").child(username).child('clipboard').get().val()
        key = getKey(username, password)
        vaultStrings = decryptVault(cipher, key)
        vaultDictionary = json.loads(vaultStrings)
        session = usersession(username, authHash, key, clipboard, lock)
        session.clearVault()
        session.dictionaryToVault(vaultDictionary)
        return session
    else:
        return False

def createNewAccount(username, password):
    authHash = getAuthHash(username, password)
    snapshot = db.child("CZ4010DB").child("users").child(username)
    if str(snapshot.child('userName').get().val()) == username:
        return False
    else:
        key = getKey(username, password)
        vault = []
        session = usersession(username, authHash, key,5000,0, vault)
        updateVault(session)
        return session        

def updateVault(session):
    snapshot = db.child("CZ4010DB").child("users").child(session.userName)
    vaultDict = session.vaultToDictionary()
    encryptedVault = encryptVault(json.dumps(vaultDict), session.key)
    body = {
        'userName': session.userName,
        'authHash': base64.b64encode(session.authHash).decode(),
        'clipboard' : session.clipboard,
        'lock': session.lock,
        'vault': base64.b64encode(encryptedVault).decode(),
    }
    snapshot.update(body)



