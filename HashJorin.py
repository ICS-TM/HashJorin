
import hashlib
import os
os.system("cls"or"clear")
print ("""
            
""")
print ("----------------------------------------------------")
print ("| CODED BY CHQ & Me3T4r_IP </>   <<--*ICSTEAM*-->> |")
print ("----------------------------------------------------")

print ("""
-------------------------
| SELECT THE HASH TYPE: |
-------------------------
[+] MD 5  = -m
[+] SHA 1 = -s1
[+] SHA 224 = -s224
[+] SHA 256 = -s256
[+] SHA 384 = -s384
[+] SHA 512 = -s384
[+] ALL
""")

hash_type = raw_input(">>> ")
print ("INTER YOUR TEXT")
text = raw_input(">>> ")

if hash_type=="-m" :
    md5 = hashlib.md5()
    md5.update(text)
    print ("YOUR MD5 HASH IS : ", md5.hexdigest())

elif hash_type=="-s1" :
    sha1 = hashlib.sha1()
    sha1.update(text)
    print ("YOUR SHA 1 HASH IS : ", sha1.hexdigest())

elif hash_type=="-s224" :
    sha224 = hashlib.sha224()
    sha224.update(text)
    print ("YOUR SHA 224 HASH IS : ", sha224.hexdigest())

elif hash_type=="-s256" : 
    sha256 = hashlib.sha256()
    sha256.update(text)
    print ("YOUR SHA 256 HASH IS : ", sha256.hexdigest())

elif hash_type=="-s384" :
    sha384 = hashlib.sha384()
    sha384.update(text)
    print ("YOUR SHA 384 HASH IS : ", sha384.hexdigest())

elif hash_type=="-s512":
    sha512 = hashlib.sha512()
    sha512.update(text)
    print ("YOUR SHA 512 HASH IS : ", sha512.hexdigest())

elif hash_type=="all" or hash_type=="ALL" :
    x1 = text
    x2 = x1
    x3 = x2
    x4 = x3
    x5 = x4
    x6 = x5
    md5 = hashlib.md5()
    md5.update(x1)
    print ("YOUR MD5 HASH IS : ", md5.hexdigest())
    sha1 = hashlib.sha1()
    sha1.update(x2)
    print ("YOUR SHA 1 HASH IS : ", sha1.hexdigest())
    sha224 = hashlib.sha224()
    sha224.update(x3)
    print ("YOUR SHA 224 HASH IS : ", sha224.hexdigest())
    sha256 = hashlib.sha256()
    sha256.update(x4)
    print ("YOUR SHA 256 HASH IS : ", sha256.hexdigest())
    sha384 = hashlib.sha384()
    sha384.update(x5)
    print ("YOUR SHA 384 HASH IS : ", sha384.hexdigest())
    sha512 = hashlib.sha512()
    sha512.update(x6)
    print ("YOUR SHA 512 HASH IS : ", sha512.hexdigest())
else:
    print ("OBJECT NOT FOUND !!!")
    exit()


