import random
import csv
from datetime import datetime
# rent_fee: int
# starttime: datetime
# endtime: datetime
# contact_info: string
# requirement: string
# user_id: int
def RentRequestSave(DicRent):
    writefile = open('rent_request.csv','a+', newline ='')
    writer = csv.writer(writefile)
    try:
        s = random.randint(0, 10000)
        s = str(s)
        requestID = s.zfill(5)
        # check id
        with open('rent_request.csv') as csvfile:
            i = 0
            reader = csv.reader(csvfile)
            try:
                column6 = [row[5] for row in reader]
            except IndexError:
                requestID = requestID
            else:
                leng = len(column6)
                for i in range(0,leng):
                    if requestID == column6[i]:
                        s = random.randint(0, 10000)
                        s = str(s)
                        requestID = s.zfill(5)
                        i = 0
                    else:
                        break
        requestID = int(requestID)
        c = open('rent_request.csv','a+', newline ='')
        writer = csv.writer(c)
        writer.writerow([DicRent['rent_fee'], DicRent['starttime'], DicRent['endtime'], DicRent['contact_info'], DicRent['requirement'], requestID])
    except BaseException:
        return(False)
    else:
        return(True)