#암호디스크(table) 없이 바로 구현

#한글자(씩) 암호화. char->int / 덧셈 암호화 후, +-65로 아스키문자로 돌려둠.
def encAdd(msg, key):
    cid = ord(msg)
    if cid in range(65,91):
        #암호화
        cid = (cid-65+key) % 26 + 65
        c = chr(cid)
    else:
        c=""
    return c

def decAdd(msg,key):
    cid = ord(msg)
    if cid in range(65,91):
        #복호화
        cid = (cid-65-key) % 26 + 65
        c = chr(cid)
    else:
        c=""
    return c

def addCipher2(msg, key, mode='encrypt'):
    #key가 1개고, str이나 int일 때可
    if ( type(key) == str ) and ( len(key) == 1):
        #key는 정수라 ord(char->int), 대문자로 통일 
        key = ord(key.upper()) - 65
    elif type(key) == int:
        key = key % 6
    else:
        print("키 부적절 ")
    
    #대문자로 변환 -> 한글자씩 암호화 or 복호화
    msg_upper = msg.upper()
    result=""
    
    if mode == "encrypt" :
        print("Encrypting...")
        for m in msg_upper:
            result += encAdd(m,key)     #위에서 만든거 호출
    
    elif mode == "decrypt" :
        print("Decrypting...")
        for m in msg_upper:
            result += decAdd(m,key)     #위에서 만든거 호출
    
    return result

#평문
msg = "crytography"
#암호문
ctxt = addCipher2(msg, 'B', 'encrypt')
print(ctxt)
#되돌리기
print(addCipher2(ctxt, 'B', 'decrypt'))
