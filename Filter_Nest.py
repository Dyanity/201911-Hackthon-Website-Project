import pandas as pd

def Filter(HomeType=None, RentFee=None, StartDate=None, EndDate=None, Latitude=None, Longitude=None):
    dataHome = pd.read_csv("home_info.csv")
    df = pd.DataFrame(data = dataHome)
    rows = len(df)
    a = [] # Define before
    res = [] #Return List
    for j in range(0,rows):
        i = rows-1-j
        if HomeType is None or (df.iloc[i][0] == HomeType or HomeType == 3 ): # 1 means Apt/ 2means House/ 3means both
            if RentFee is None or (df.iloc[i][1] == ' ' or df.iloc[i][1] <= RentFee):
                if (StartDate is None or df.iloc[i][2] <= StartDate) and (EndDate is None or df.iloc[i][3] >= EndDate): #' 'No Blank?
                    if (Latitude is None or abs( df.iloc[i][4] - Latitude ) <= 2)  and (Longitude is None or abs( df.iloc[i][5] - Longitude ) <= 1): #' ' No Blank
                        #a.append(df.iloc[i][6])   # Store ID
                        res.append({'roomType':int(df.iloc[i][0]), 'rentFee':int(df.iloc[i][1]), 'startDate':df.iloc[i][2], 'endDate':df.iloc[i][3], 'latitude':df.iloc[i][4], 'longitude':df.iloc[i][5], 'description':df.iloc[i][6], 'imgUrl':df.iloc[i][7],'contactInfo':str(df.iloc[i][8])})
    '''
    num = len(a)
    for i in range(0,num):
        res.append(df.iloc[[a[i]]])
    '''
    return res


















