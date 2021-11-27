# CZ4010-Project-PasswordManager
Disclaimer 
Our password management tool can securely encrypt a password and store it while being encrypted, however other components also play a part, as a saying goes “A chain is only as strong as its weakest link” this applies to security as well. Some basic guidelines to help ensure that the vault is safe despite some passwords are being exposed:
Do not reuse password
Ensure password complexity, for example ensure minimum character length of 8 including alphanumeric, symbols and spaces. (best if generated through reputable or well made password management tools)
Do not share password with anyone, including family or friends
Do not write password down on a piece of paper that is visible to everyone
Do not use common passwords that could be easily broken through the use of a dictionary attack.

## Group Members
-Gerald Lim Ze Yang
* Contributions - Password Vault, Database(Login, Signup), Auto clear Clipboard, Auto Lock, Search, Slides, README, Product Demo
-Ng Chun Kai
* Contributions - Password Generator, settings, Add Account, Video Editing,Slides, README, Product Demo

##Motivation 
A lot of people in the world like to share or use the same password, else they choose a simple password. A research in America, 41% of online adults share their passwords, 39% say they use the same passwords for many of their online accounts, and 25% admit they use simpler passwords because they are easier to remember. This shows how vulnerable it is, for example having the same password means once an account is compromised, other accounts can be in jeopardy. Using a simple password can lead to a dictionary attack which could cause the account to be in danger.

In order to solve this problem and also apply what we have learnt, we decided to create a password manager ourselves, which will help us better understand the implementation of cryptography, and apply what we have learned in lessons into a practical tool. This will also let us learn more about cryptography and its inner workings.

##Research 

### Selecting a Encryption Cipher

#### [**Advanced Encryption Standard (AES)**](https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html)

AES is implemented in software and hardware throughout the world to encrypt sensitive data. It is essential for government computer security, cybersecurity and electronic data protection. AES is implemented in a wide range of applications as it is defined as the standard by NIST. AES has been adopted by the U.S. government. It has been around for 20-30 years and it is still secured with currently no known vulnerabilities. Has many modes of operation such as Propagating cipher block chaining (PCBC), cipher block chaining (CBC), Electronic codebook (ECB), Galois/counter (GCM). As such we have found and compared 2 most commonly used encryption modes GCM and CBC and made a comparison of them.


AES(CBC) problem
https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
CBC mode problem is an error of one plaintext will affect all of the subsequent blocks. At the same time CBC is vulnerable to multiple types of attacks such as :
Chosen plaintext attack(CPA) where attacks with a set of chosen plaintexts and obtain respective ciphertext.
Chosen Ciphertext Attack(CCA) where attacks with a set of chosen ciphertexts to obtain respective plaintexts.
Padding oracle attack, which is an attack which uses the padding validation of a cryptographic message to decrypt the ciphertext.

AES(CBC) VS AES(GCM)
https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#gcm-mode
Both the AES-CBC and AES-GCM are able to secure your valuable data with a good implementation. But to prevent complex CBC attacks such as Chosen Plaintext Attack(CPA) and Chosen Ciphertext Attack(CCA) it is necessary to use Authenticated Encryption. 
So the best option for that is GCM. AES-GCM is written in parallel which means throughput is significantly higher than AES-CBC by lowering encryption overheads.GCM mode will accept pipelined and parallelized implementations and have minimal computational latency in order to be useful at high data rates.
