# ASCII 'a' = 97
# 'b' = 98
# 'z' = 122

def findPassword(password):
    for i in range (10):
        if(password.count(i)>0):
            for k in range(0,8):
                if(i==password[k]):
                    print(str(i)+" is "+str(k) +"th password")
      

    for i in range (97,123,1):
        if(password.count(chr(i))>0):
            #print(chr(i) +" is in password!!")
            for k in range(0,8):
                if(chr(i)==password[k]):
                    print(chr(i)+" is "+str(k) +"th password")


pw1 = ['a',5,'a','m',1,'o',4,'d']
pw2 = ['s','w','a','c',1,'o',3,'w']

print("pw1 을 해킹한다!!")
findPassword(pw1)

print("pw2를 해킹한다!! 성공할까??")
findPassword(pw2)



