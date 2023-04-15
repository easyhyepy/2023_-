#key 정상인지 확인하고, int형태로 변환 후
#key가지고 암복호화 table 미리 만들어두기기
def keyAddCipher(key):
    #key가 1개고, str이나 int일 때可
    if ( type(key) == str ) and ( len(key) == 1):
        #key는 정수라 ord(char->int), 대문자로 통일 
        key = ord(key.upper()) - 65
    elif type(key) == int:
        key = key % 6
    else:
        print("키 부적절 ")

    #key가지고 암복호화 테이블 미리 만들어두기
    encMap = {}
    decMap = {}
    for i in range(26):
        enc_idx = (i+key)%26
        dec_idx = (i-key)%26
        encMap[chr(i+65)] = chr(enc_idx+65)
        decMap[chr(i+65)] = chr(dec_idx+65)
    return encMap, decMap
    


def addCipher(msg, key, mode='encrypt'):
    #mode: encryption / decryption
    #모드 확인 후 출력.
    assert mode in ['encrypt', 'decrypt']
    if mode == "encrypt":
        print("Encrypting...")
    else:
        print("Decrypting...")
    
    #암복호화 테이블 생성 - 위에 정의된 함수 이용
    encMap, decMap = keyAddCipher(key)
    
    #대문자로 변환 -> 한글자씩 암호화 or 복호화
    msg_upper = msg.upper()
    result=""
    for m in msg_upper:
        if m in encMap.keys():
            if mode == 'encrypt':
                result+=encMap[m]
            else:       #'decrypt'
                res+=decMap[m]
    return result
                
 
#평문  
msg = "hello"
#암호문 출력
print (addCipher(msg, 'C', 'encrypt'))
    
