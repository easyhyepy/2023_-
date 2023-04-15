#key 정상인지 확인하고, int형태로 변환 후
#key가지고 암복호화 table 미리 만들어두기기

def keyMultCipher(key):
    #key가 1개고, str이나 int일 때可
    if ( type(key) == str ) and ( len(key) == 1):
        #key는 정수라 ord(char->int), 대문자로 통일 
        key = ord(key.upper()) - 65
    elif type(key) == int:
        key = key % 26
    else:
        print("키 부적절 ")
    
    ##key검사: 곱셈암호 가능한 키 12가지
    assert key in [1,3,5,7,9,11,15,17,19,21,23,25], "26과 서로소가 아니여서 BadKey다."
    
    encMap = {}
    decMap = {}
    for i in range(26):
        ##곱셈암호 정의대로
        enc_idx = (i*key)%26
        
        #아스키를 문자로 = chr(__+65)
        ##dec = enc에서 key-value 반대로 바꾼 것 (역연산)
        encMap[chr(i+65)] = chr(enc_idx+65)
        decMap[chr(enc_idx+65)] = chr(i+65)
        
    return encMap, decMap



def multCipher(msg, key, mode="encrypt"):
    #mode: encryption / decryption -> 모드 확인 후 출력.
    assert mode in ['encrypt', 'decrypt']
    if mode == "encrypt":
        print("Encrypting...")
    else:
        print("Decrypting...")
    
    #암복호화 테이블 생성 - 위에 정의된 함수 이용
    encMap, decMap = keyMultCipher(key) 
    
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
print (multCipher(msg, 'F', 'encrypt'))
        
