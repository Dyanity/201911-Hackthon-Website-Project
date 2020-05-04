import base64

def PasswordEncode( password ):
    b64_password = base64.b64encode(password.encode())
    afterpassword = b64_password.decode()
    return(afterpassword)