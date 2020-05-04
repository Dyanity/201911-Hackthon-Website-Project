import random
import csv
from datetime import datetime
#location: tuple (latitude, longitude)
# type:inttype0:apartment and 1:house
# starttime: datetime
# endtime: datetime
# description: string
# rent_fee: int
# image: string
def HouseForRentSave(DicHouse):
    writefile = open('house_info.csv','a+', newline ='')
    writer = csv.writer(writefile)
    try:
        s = random.randint(0, 10000)
        s = str(s)
        HouseID = s.zfill(5)
        # check id
        with open('house_info.csv') as csvfile:
            i = 0
            reader = csv.reader(csvfile)
            try:
                column8 = [row[8] for row in reader]
            except IndexError:
                HouseID = HouseID
            else:
                leng = len(column8)
                for i in range(0,leng):
                    if HouseID == column8[i]:
                        s = random.randint(0, 10000)
                        s = str(s)
                        HouseID = s.zfill(5)
                        i = 0
                    else:
                        break
        HouseID = int(HouseID)
        c = open('home_info.csv','a+', newline ='')
        writer = csv.writer(c)
        print(DicHouse)
        writer.writerow([DicHouse['type'],DicHouse['rent_fee'],DicHouse['starttime'],DicHouse['endtime'],DicHouse['latitude'],DicHouse['longitude'],DicHouse['description'],DicHouse['image'], DicHouse['contact_info']])
    except BaseException:
        return(False)
    else:
        return(True)