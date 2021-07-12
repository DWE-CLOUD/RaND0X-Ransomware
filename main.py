import time
import os
import hashlib
from tkinter import *
print("what do you wanna create ? (payload : 1 or execute : 2 ):  ",end='')
input_1=int(input(""))
if input_1==1:
    print("do you want payload in direct version or want to hide it behind a software or a file ? ( direct : 1 or "
          "hide : 2 ) > ",end='')
    input_2=int(input(""))
    if input_2==1:
        print("Educational Purpose Only ! ")
        print("Amount of Ransom in dollars : ",end='')
        ran_amt=int(input(""))
        print("[1] Own Crypto Address or [2] Temp Crypto Address : ",end='')
        t_o=int(input(""))
        if t_o==2:
            def sha256(data):
                digest = hashlib.new("sha256")
                digest.update(data)
                return digest.digest()


            def ripemd160(x):
                d = hashlib.new("ripemd160")
                d.update(x)
                return d.digest()


            def b58(data):
                B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

                if data[0] == 0:
                    return "1" + b58(data[1:])

                x = sum([v * (256 ** i) for i, v in enumerate(data[::-1])])
                ret = ""
                while x > 0:
                    ret = B58[x % 58] + ret
                    x = x // 58

                return ret


            class Point:
                def __init__(self,
                             x=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
                             y=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
                             p=2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1):
                    self.x = x
                    self.y = y
                    self.p = p

                def __add__(self, other):
                    return self.__radd__(other)

                def __mul__(self, other):
                    return self.__rmul__(other)

                def __rmul__(self, other):
                    n = self
                    q = None

                    for i in range(256):
                        if other & (1 << i):
                            q = q + n
                        n = n + n

                    return q

                def __radd__(self, other):
                    if other is None:
                        return self
                    x1 = other.x
                    y1 = other.y
                    x2 = self.x
                    y2 = self.y
                    p = self.p

                    if self == other:
                        l = pow(2 * y2 % p, p - 2, p) * (3 * x2 * x2) % p
                    else:
                        l = pow(x1 - x2, p - 2, p) * (y1 - y2) % p

                    newX = (l ** 2 - x2 - x1) % p
                    newY = (l * x2 - l * newX - y2) % p

                    return Point(newX, newY)

                def toBytes(self):
                    x = self.x.to_bytes(32, "big")
                    y = self.y.to_bytes(32, "big")
                    return b"\x04" + x + y


            def getPublicKey(privkey):
                SPEC256k1 = Point()
                pk = int.from_bytes(privkey, "big")
                hash160 = ripemd160(sha256((SPEC256k1 * pk).toBytes()))
                address = b"\x00" + hash160

                address = b58(address + sha256(sha256(address))[:4])
                return address


            def getWif(privkey):
                wif = b"\x80" + privkey
                wif = b58(wif + sha256(sha256(wif))[:4])
                return wif


            if __name__ == "__main__":
                randomBytes = os.urandom(32)
                print("")
                print('*' * 100)
                print("")
                print("Address: " + getPublicKey(randomBytes))
                print("Privkey: " + getWif(randomBytes))
                print("")
                print('*'*100)
                t_o_1 = getPublicKey(randomBytes)
        elif t_o==1:
            t_o_1=input("Please enter your own BTC address : ")
            print("Is this right [1 : TO CONFIRM] [2: To Re-enter]: ",t_o_1,end='')
            input_t_o=int(input(""))
            if input_t_o==1:
                print("Thanks !")
            elif input_t_o==2:
                t_o_1=input("Re-enter now : ")
                print(t_o_1)
            else:
                print("bye")
        else:
            print("bye !")
        print("[1] Normal Ransomware / [2] Deadly Ransomware : ",end='')
        n_d=int(input(""))
        if n_d==2:
            print('THIS IS A PUBLIC VERSION , THE DEADLY RANSOMWARE IS WITH OWNER')
            print("email to : dwecloud@gmail.com to get the full  version")
        elif n_d==1:
            print("Please wait while we create your own ransomware")
            window = Tk()
            btn = Button(window, text="Click to download file", fg='blue')
            btn.place(x=80, y=100)
            lbl = Label(window, text="Hey , Your ransomware is made ... This ransomware is made using python and the creator of this project is Team DWE CLOUD", fg='red', font=("Helvetica", 14))
            lbl.place(x=60, y=50)
            window.title('Ransomware Creation')
            window.geometry("300x200+10+10")
            window.mainloop()
else:
    print("bye")