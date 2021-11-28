# CZ4010-Project-PasswordManager
## Disclaimer 
Our password management tool can securely encrypt a password and store it while being encrypted, however other components also play a part, as a saying goes “A chain is only as strong as its weakest link” this applies to security as well. Some basic guidelines to help ensure that the vault is safe despite some passwords are being exposed:
Do not reuse password
Ensure password complexity, for example ensure minimum character length of 8 including alphanumeric, symbols and spaces. (best if generated through reputable or well made password management tools)
Do not share password with anyone, including family or friends
Do not write password down on a piece of paper that is visible to everyone
Do not use common passwords that could be easily broken through the use of a dictionary attack.

## Group Members
### -Gerald Lim Ze Yang
* Contributions - Password Vault, Database(Login, Signup), Auto clear Clipboard, Auto Lock, Search, Slides, README, Product Demo
### -Ng Chun Kai
* Contributions - Password Generator, settings, Add Account, Video Editing,Slides, README, Product Demo

## Motivation 
A lot of people in the world like to share or use the same password, else they choose a simple password. A research in America, 41% of online adults share their passwords, 39% say they use the same passwords for many of their online accounts, and 25% admit they use simpler passwords because they are easier to remember. This shows how vulnerable it is, for example having the same password means once an account is compromised, other accounts can be in jeopardy. Using a simple password can lead to a dictionary attack which could cause the account to be in danger.

In order to solve this problem and also apply what we have learnt, we decided to create a password manager ourselves, which will help us better understand the implementation of cryptography, and apply what we have learned in lessons into a practical tool. This will also let us learn more about cryptography and its inner workings.

## Research 
### Selecting a Encryption Cipher
#### [**Advanced Encryption Standard (AES)**](https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html)
AES is implemented in software and hardware throughout the world to encrypt sensitive data. It is essential for government computer security, cybersecurity and electronic data protection. AES is implemented in a wide range of applications as it is defined as the standard by NIST. AES has been adopted by the U.S. government. It has been around for 20-30 years and it is still secured with currently no known vulnerabilities. Has many modes of operation such as Propagating cipher block chaining (PCBC), cipher block chaining (CBC), Electronic codebook (ECB), Galois/counter (GCM). 

#### [**AES(CBC)**](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode)
Cipher block chaining (CBC) is a mode of operation for a block cipher -- one in which a sequence of bits are encrypted as a single unit, or block, with a cipher key applied to the entire block. Cipher block chaining uses what is known as an initialization vector (IV) of a certain length. With the use of a single encryption key, a large amount of data can be encrypted and decrypted. CBC mode, identical blocks do not have the same cipher. It allows parallel decryption to speed up decryption process
### Selecting a Hashing Library 
#### [**Scrypt**](https://docs.python.org/3/library/hashlib.html)
Scrypt is a password-based key derivation function created by Collin Percival, originally designed and used for Tarsnap online backup system. The algorithm is designed to make it costly to perform large-scale custom hardware attacks, by requiring large amounts of memory. However it is also computationally expensive, at the same time harder to implement.
#### [**PBKDF2_HMAC**](https://docs.python.org/3/library/hashlib.html)
PBKDF2 applies a pseudorandom function, such as hash-based message authentication code(HMAC), to the input password alongside salt values and repeats the process many times to produce a key, which can be used as a cryptographic key. The added computational work makes the password harder to crack, also known as key stretching. 
SHA 512 is part of the SHA 2 family which is a set of cryptographic hash functions designed by the United States National Security Agency (NSA) and first published in 2001 
#### Final selection for Hashing Library 
We have chosen PBKDF2_HMAC SHA512 mainly for the fact it is more widely used in today's world and it is less demanding on the system. We had also decided the number of key iterations to be 200,000.
We made this choice based on another password manager, [**lastpass**](https://support.logmeininc.com/lastpass/help/about-password-iterations-lp030027), which is one of the better password managers in the market. They use PBKDF2_SHA256 with 100,100 iterations as the default key generation. Our key generator will be more secure as it will make it more difficult for a computer to check that any 1 password is the correct Master Password during a compromising attack.
### Selecting a Cryptographically Secure PRNG library 
A pseudo-random number generator (PRNG) produces a stream of variates that are independent and statistically indistinguishable from a random sequence.
#### [**PyCryptodome**](https://pycryptodome.readthedocs.io/en/latest/src/random/random.html)
PyCryptodome is a self-contained Python package of low-level cryptographic primitives. It supports Python 2.7, Python 3.5 and newer, and PyPy. PyCryptodome is a fork of PyCrypto. 
It supports Authenticated encryption modes (GCM, CCM, EAX, SIV, OCB), Random numbers get sourced directly from the OS (and not from a CSPRNG in userspace), Password-protected PKCS#8 key containers, which we need for this project.
#### [**secret**](https://docs.python.org/3/library/secrets.html)
The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

#### Final selection for Cryptographically Secure PRNG library 
We chose PyCryptodome because it is widely used and tested and as we also used it for encryption and decryption we decided not to install an additional library as it may cause more attack vectors if more libraries are installed.
### Selecting a Cloud Storage
#### Google Firebase
Firebase is a cloud-hosted real time document store. iOS, Android, and JavaScript clients share one Realtime Database instance and automatically receive updates with the newest data. It is also one of the cheaper alternatives when compared to others at its level.
#### Amazon DynamoDB
Developers describe Amazon DynamoDB as "Fully managed NoSQL database service". All data items are stored on Solid State Drives (SSDs), and are replicated across 3 Availability Zones for high availability and durability. 
#### Final selection for Cloud Storage 
The main reason we chose Google Firebase is for its Realtime Database as enables real time syncing of data which helps when syncing data of the password vault. Google Firebase is also very easy to set up as compared to Amazon and there is also a lot of documentation on how to set it up.
## Design
### How we secure our Application
#### Generation and application of Authentication key
To generate the authentication key, we used 200,000 rounds of PBKDF2-SHA512. To authenticate when users login we use the authentication key and hash it for one more round to generate an authentication hash. This authentication hash will be stored in Google firebase and will be used to authenticate the login user.
#### Encryption and Decryption of password Vault
The password vault will store all the user accounts. This vault will be then stored in the cloud using Google firebase realtime database. The vault is encrypted using the Authentication key with AES-CBC with a 16 bytes IV. After the user have login successfully the encrypted vault will be retrieved from the realtime database and will be decrypted locally using the Authentication key
#### Generate Secure random passwords
To generate a secure random password we make use of the pycryptodome Crypto.Random module. The password will be generated based on what the user has chosen for example to include symbols and digits to the generated password. The user will also be able to generate according to their desired length which is capped to 64 characters.

![plot](https://github.com/glws967/CZ4010-Project-PasswordManager/blob/main/images/imp.png?raw=true)
#### Login/Authentication
1. Generate key using username and password (Using PBKDF2 SHA512 and 200000 round keys)
2. Generate Authentication Hash using the Key (Using PBKDF2 SHA512 and 1 round key)
3. Retrieve Stored Authentication Hash and Encrypted vault from firebase
4. Compare Stored Authentication Hash with Generated Authentication hash
5. Successfully logged in and do Vault Decryption
#### Vault Encryption
1. Add padding to the end of the plaintext vault
2. Generate a 16 bytes PRNG Initialization vector (IV)
3. Encrypt the vault with AES-256 bit CBC Mode, using the key and IV
4. Return IV+Encrypted Vault
#### Vault Decryption
1. Remove the first 16 bytes of IV from the encrypted vault
2. Decrypt the Encrypted vault with AES-256 bit CBC Mode, Using the key and IV
3. Remove the padding at the end of the vault


## Security
### Confidentiality
- To achieve this in our project, we make use of the cryptographic algorithms AES(CBC) and hashing algorithm PBKDF2_SHA512.

- The entire vault is being encrypted and decrypted locally before sending it to the firebase for storage, this ensures confidentiality of the vault as without decrypting it, the vault will be just a cipher text. This also ensures that no man in the middle attack is possible as we are not sending the key to the database, the key is generated locally.

- By default all account's password added by the user in the GUI is concealed/masked so to prevent shoulder surfing.

- The application allow auto locking so that if the user is away from their computer and forgot to lock their computer the application will lock itself so to prevent other people from accessing the app.

### Authentication and Integrity
When the user login,  Authentication Hash and Encrypted vault will be retrieved from the firebase. The Authentication hash is then compared with the user input. If these are identical, the user will be successfully authenticated and the Vault will be decrypted. Which ensures Authentication and Integrity.

### Availability 
We used cloud storage as it allows constant availability to the data needed for the application as Google is a major player in this field and data being stored with them are also being backed up, in many different places, thus even if something were to happen to a certain database, the data won't be lost. The code is also easily configurable so in case of a sudden incident we could also switch to Amazon cloud or Microsoft Azure.

### Other Features 
#### Auto clear clipboard
After pasting the password to the website intended, the password itself is still stored in the clipboard, which can still be retrieved if intended, thus if an attacker has physical access to the computer after the user, the attacker can find out the password. This prevents websites from sniffing user’s clipboard.Therefore we have come out with the feature of auto clear clipboard, in which users can set a time interval before the clipboard is being automatically cleared.

![plot](https://github.com/glws967/CZ4010-Project-PasswordManager/blob/main/images/clipboard.png?raw=true)

#### Auto Lock after computer idle
This feature is to lock the vault after the computer is idle, this is to prevent unintended access to the vault, as the vault will contains all the users credentials and password, having access to it is the equivalent of losing lots of accounts, therefore auto locking the vault will reduce the chances of others being able to access the vault. The time before locking can also be set.

![plot](https://github.com/glws967/CZ4010-Project-PasswordManager/blob/main/images/lock.png?raw=true)

#### Cloud storage
To make the password manager more convenient to the user we decided to store the password vault in a cloud storage (Google firebase Realtime Database), as compared to a local storage. As long as the user has an internet connection they will be able to retrieve their password easily.

## Development
### Python
#### Integrated Development Environment
Visual studio Code - For developing the entire application, including graphical user interface (GUI)
#### Libraries
-**Pyqt5** => GUI for password manager  
-**Pyrebase 4** => To connect to google firebase alongside Pycryptodome  
-**Hashlib** => For generation of authentication key and authentication hash  
-**Pycryptodome** => For AES 256 bit (CBC) encryption and PRNG generator  

### Google Firebase 
Cloud-hosted real time database, to allow access to the vault anytime anywhere.


## Use of the code
Make sure the latest Python 3 is installed.

1. Clone this repository 
2. Install the following libraries using the following:  
3. pip install pyqt5  
4. pip install pyrebase4  
5. Run login.py       

![plot](https://github.com/glws967/CZ4010-Project-PasswordManager/blob/main/images/login.png?raw=true)

6. Register for an account if you don't have one, else good to go  

Or you can just download the ‘login.exe’ file under the releases pages.

## Glossary
AES - Advanced Encryption Standard  
CBC - Cipher-Block Chaining  
GUI - Graphical User Interface  
HMAC - Hash-Based Message Authentication Code  
NIST- National Institute of Standards and Technology  
PBKDF - Password-Based Key Derivation  
PRNG - Pseudo-Random Number Generator  
SHA - Secure Hash Algorithms  
