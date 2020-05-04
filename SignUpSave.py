import random
import csv

def SignUpSave(userName, email, encoded_password):
    writefile = open('user_info.csv','a+', newline ='')
    writer = csv.writer(writefile)
    try:
        s = random.randint(0, 10000)
        s = str(s)
        userID = s.zfill(5)
        # check id
        with open('user_info.csv') as csvfile:
            i = 0
            reader = csv.reader(csvfile)
            try:
                column3 = [row[3] for row in reader]
            except IndexError:
                userID = userID
            else:
                leng = len(column3)
                for i in range(0,leng):
                    if userID == column3[i]:
                        s = random.randint(0, 10000)
                        s = str(s)
                        userID = s.zfill(5)
                        i = 0
                    else:
                        break
        c = open('user_info.csv','a+', newline ='')
        writer = csv.writer(c)
        writer.writerow([userName, email, encoded_password, userID])
    except BaseException:
        return(False)
    else:
        return userID
        #return(True)