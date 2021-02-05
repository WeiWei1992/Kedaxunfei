import os

from datetime import datetime
def handle_txt(file=None):
    if file==None:
        file='语录1'
    mylines=[]
    with open(file,encoding='utf-8') as f:
        lines=f.readlines()
        mylines=lines
    return mylines

def get_mark_str(file=None):
    if file==None:
        file='mark.txt'
    mylines=[]
    with open(file,encoding='utf-8') as f:
        lines=f.readlines()
        mylines=lines
    return mylines

def get_gaokao_time():

    # 构造一个将来的时间
    future=datetime.strptime('2021-6-7 9:00:00', '%Y-%m-%d %H:%M:%S')
    # 当前时间
    now=datetime.now()
    # 求时间差bai
    delta=future-now
    days=delta.days


    hour=delta.seconds / 60 / 60
    #minute=(delta.seconds-hour * 60 * 60) / 60
    #print(minute)
    r_str=str(days)+" 天 "+str(int(hour))+" 小时 "
    print(r_str)
    return r_str
    #return r_str
    # print(delta)


if __name__=="__main__":
    mylines=handle_txt()
    print(mylines)
    print(len(mylines))
    print(mylines[0])
    get_gaokao_time()