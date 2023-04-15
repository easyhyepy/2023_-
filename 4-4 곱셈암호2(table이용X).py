#암호디스크(table) 없이 바로 구현

#유클리드 호제법 (ft.재귀) -> x*k mod 26에서 복호화키 구하기
#a,b의 최대공약수 g 구함. 2,3번째 인자는 a,b이용한 식의 계수들.
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g,y,x = egcd(b%a, a) #재귀 -> 몰라도됨
        return (g, x-(b//a)*y, y)

#modinv(3,26) -> 3*x mode 26=1인 x를 반환해주는 함수.
def modinv(a,m):
    g, x, y = egcd(a,m)
    if g != 1:
        raise Exception ('modular inverse does not exist')
    else: 
        return x%m
        
#한글자(씩) 암호화. char->int / 곱셈 암호화 후, +65로 아스키문자로 돌려둠.
def encMult(msg, key):
    cid = ord(msg)
    if cid in range(65,91):
        #암호화
        cid = ((cid-65)*key) % 26 + 65      #아스키코드(str)->숫자로 계산->아스키 
        c = chr(cid)
    else:
        c=""
    return c

def decMult(msg,key):
    cid = ord(msg)
    key = modinv(key,26)
    if cid in range(65,91):
        #복호화
        cid = ((cid-65)*key) % 26 + 65
        c = chr(cid)
    else:
        c=""
    return c

def multCipher2(msg, key, mode='encrypt'):
    #key가 1개고, str이나 int일 때可
    #key를 0~25사이 정수로 변환환
    if ( type(key) == str ) and ( len(key) == 1):
        #key는 정수라 ord(char->int), 대문자로 통일 
        key = ord(key.upper()) - 65
        assert key in [1,3,5,7,9,11,15,17,19,21,23,25], "26과 서로소가 아니여서, 키 부적절."
    elif type(key) == int:
        key = key % 26
    else:
        print("키 부적절 ")
    
    #한번더 test (0~25)
    g, _, _ = egcd(key, 26)
    if g != 1:  #서로소 아니면 
        raise Exception('키부적절절')
    
    #대문자로 변환 -> 한글자씩 암호화 or 복호화
    msg_upper = msg.upper()
    result=""
    
    if mode == "encrypt" :
        print("Encrypting...")
        for m in msg_upper:
            result += encMult(m,key)     #위에서 만든거 호출
    
    elif mode == "decrypt" :
        print("Decrypting...")
        for m in msg_upper:
            result += decMult(m,key)     #위에서 만든거 호출
    
    return result

#평문
msg = "crytography"
#암호문
ctxt = multCipher2(msg, 'D', 'encrypt')
print(ctxt)
#되돌리기
print(multCipher2(ctxt, 'D', 'decrypt'))
