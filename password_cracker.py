import hashlib

def crack_sha1_hash(hash, use_salts = False):




    # Open the file in read mode
    with open('top-10000-passwords.txt', 'r') as file:
        # Read each line in the file
        for line in file:

            password=line.rstrip('\n')

            
            if not use_salts:
                sha=SHA1(password)

                if sha==hash:
                    return password

            else :

                with open('known-salts.txt', 'r') as saltsFile:

                    for saltLine in saltsFile :
                        
                        salt=saltLine.rstrip('\n')

                        saltedPasswordAppend=password+salt

                        saltedPasswordPrepend=salt+password

                        sha=SHA1(saltedPasswordAppend)

                        if sha==hash:
                            return password

                        sha=SHA1(saltedPasswordPrepend)
                            
                        if sha==hash:
                            return password
                            
    return "PASSWORD NOT IN DATABASE"
            









# SHA1 hex digest for some input string
def SHA1(msg: str) -> str:
    return hashlib.sha1(msg.encode()).hexdigest()