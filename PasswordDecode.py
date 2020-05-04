import base64

def PasswordDecode(afterpassword):
    var = afterpassword.encode()
    ori = base64.b64decode(var).decode()
    return(ori)

#afterpassword = 'Y2VzaGk='
afterEncode = PasswordDecode(afterpassword)
print(afterEncode)

#after = b64_password.decode()


#b'Y2VzaGk='
#Y2VzaGk=