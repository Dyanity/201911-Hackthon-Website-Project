import pandas as pd

def LogIn(email,password):
    dataUser = pd.read_csv("user_info.csv")
    dfu = pd.DataFrame(data = dataUser)
    rowu = len(dfu)
    for i in range(0,rowu):
        if dfu.iloc[i][1] == email:
            if dfu.iloc[i][2] == password:
                return(True,dfu.iloc[i][3])
    return(False,'')

def queryUser(userid):
    dataUser = pd.read_csv("user_info.csv")
    dfu = pd.DataFrame(data = dataUser)
    rowu = len(dfu)
    for i in range(0,rowu):
        if dfu.iloc[i][1] == userid:
            return(True)
    return(False)