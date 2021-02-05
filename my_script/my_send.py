#处理Excel的方法
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.mime.base import MIMEBase
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import datetime
from openpyxl import load_workbook
import os
from email.mime.image import MIMEImage
import random
import time

from my_script.hand_excel import handle_excel
from my_script.hand_txt import handle_txt,get_gaokao_time,get_mark_str
def send_email(msg_to,file_path,my_str,msg_from,password,nick_name,gaokao_time,mark_str):
    '''
    :param msg_to: 收件人邮箱
    :param file_path: 图片路径
    :param my_str: 语录
    ：msg_from:发件人
    ：password:密码
    nick_name:用户昵称
    gaokao_time：高考剩余时间
    :return:
    '''
    now_time = datetime.datetime.now()
    year = now_time.year
    month = now_time.month
    day = now_time.day
    hour=now_time.hour
    mint=now_time.minute
    mytime = str(year) + " 年 " + str(month) + " 月 " + str(day) + " 日 " +str(hour) + " 时 " +str(mint)+" 分 "

    msg_from=msg_from
    passwd=password

    subject = '会议纪要'

    #message = MIMEMultipart('mixed')
    message=MIMEMultipart('alternative')

    # #添加正文内容
    # text=my_str
    # message.attach(MIMEText(text,'html','utf-8'))

    # att2=MIMEImage(open(file_path,'rb').read(),_subtype='octet-stream')
    # att2.add_header('Content-ID', '<image1>')
    #
    # message.attach(att2)

    fp=open(file_path,'rb')
    msgImage=MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID','<image1>')
    message.attach(msgImage)
    html="""
    <html>
        <body>
            <h1 align="center">高考助力</h1>
            <p><strong>您好：{nick_name}</strong></p>
            <p><strong>距离2021年高考还有：{gaokao_time} </strong></p>
            <p><strong>{mark_str}</strong></p>
            <p>{yulu}</p>
            <p>
                <br><img src="cid:image1"></br>
            </p>
            
            <p align="right">{mytime}</p>
        </body>
    </html>
    """.format(nick_name=nick_name,gaokao_time=gaokao_time,mark_str=mark_str,yulu=my_str,mytime=mytime)

    htm=MIMEText(html,'html',_charset='utf-8')
    message.attach(htm)


    att1=MIMEText(open(file_path,'rb').read(),'base64','utf-8')
    att1["Content-Type"]='application/octet-stream'
    #att1['Content-Disposition']='attachment;filename='+file_path
    excel_base_path=os.path.dirname(file_path)  #获取的是路径
    excel_base_name=os.path.basename(file_path)  #获取到的是文件名称
    #excel_base_name="院校专业介绍.png"
    att1['Content-Disposition'] = 'attachment;filename=' + excel_base_name
    message.attach(att1)



    # 放入邮件主题
    message['Subject'] = subject

    # 放入发件人,这是展示在邮件里面的，和时间的发件人没有关系
    message['From'] = msg_from
    try:
        # 通过ssl方式发送，服务器地址，端口
        #s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s = smtplib.SMTP_SSL("smtp.yeah.net", 465)
        #登录邮箱
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, message.as_string())
        print("邮件发送成功")

    except Exception as e:
        print(e)
        print("出现了失败")
        return None


    finally:
        s.quit()



def main_send():
    file_path = '1.png'

    my_email=[
        ['gaokao2021@yeah.net','NVXUBJRDTRIBIVIO'],
        ['gaokao2022@yeah.net','HMDUAZPYSBIXMRJN'],
        ['gaokao2023@yeah.net','DEMZQYYBUYWRDNGT'],
        ['gaokao2024@yeah.net','LCQIUVGLRBDACSGU'],
        ['gaokao2025@yeah.net','URVTSNUNYPFLICHC'],
        ['gaokao2020@yeah.net','ALWHVMMTIBKXMYCP'],
        ['gaokao2026@yeah.net','OTXGEHIZNVLZBLVZ'],
        ['gaokao2027@yeah.net','MCXEVNRWIOTQHCWA'],
        ['gaokao2028@yeah.net','JFZPZSUFHECWVDNG'],
        ['gaokao2029@yeah.net','ASZTWFAZEPXRMXHH'],
        ['gaokao2030@yeah.net','EUGEXGNGGTGBZUSQ'],
        ['gaokao2031@yeah.net','LVIDJMYYKEPWHWFN'],
        ['university2020@yeah.net','VRYZNCYTGPWSYWJW'],
        ['university2021@yeah.net','DYSCZVGTLRWODOLA'],
        ['university2022@yeah.net','FYLGHIKOZQJWUYSV'],
        ['university2023@yeah.net','LMGVSVSJDEKQKMZO']
    ]
    values=handle_excel()
    # my_strs=handle_txt()
    # len_mystr=len(my_strs)
    len_myemail=len(my_email)
    # print(len_mystr)
    #j=0
    for i in range(len(values)):
        print("========"+str(i)+"=========")
        print(values[i])

        my_strs = handle_txt()
        len_mystr = len(my_strs)
        print("len_mystr ",len_mystr)
        random_mystr=random.randint(0,len_mystr-1)
        random_myemail=random.randint(0,len_myemail-1)
        msg_to=values[i][1]


        my_str=my_strs[random_mystr]
        msg_from=my_email[random_myemail][0]
        print(msg_to)
        print(msg_from)

        password=my_email[random_myemail][1]
        nick_name=values[i][0]
        gaokao_time=get_gaokao_time()
        mark_lines=get_mark_str()
        len_mark=len(mark_lines)
        print("len_mark: ",len_mark)
        random_mark = random.randint(0, len_mark - 1)
        mark_str=mark_lines[random_mark]

        print(nick_name)
        print(gaokao_time)
        print(my_str)
        print(mark_str)

        res=send_email(msg_to, file_path, my_str, msg_from, password, nick_name, gaokao_time,mark_str)
        # if res==None:
        #     print("发送邮件失败，退出")
        #     break
        time.sleep(60)







if __name__=="__main__":
    #2021甘肃高考群家长群(866972667)

    main_send()

    # my_email=[
    #     ['gaokao2021@yeah.net','NVXUBJRDTRIBIVIO'],
    #     ['gaokao2022@yeah.net','HMDUAZPYSBIXMRJN'],
    #     ['gaokao2023@yeah.net','DEMZQYYBUYWRDNGT'],
    #     ['gaokao2024@yeah.net','LCQIUVGLRBDACSGU'],
    #     ['gaokao2025@yeah.net','URVTSNUNYPFLICHC'],
    #     ['gaokao2020@yeah.net','ALWHVMMTIBKXMYCP']
    # ]
    my_email=[

        ['gaokao2025@yeah.net', 'URVTSNUNYPFLICHC']
    ]

    #send_email(msg_to, file_path, my_str, msg_from, password, nick_name, gaokao_time):

    # for i in range(len(my_email)):
    #     print("========="+str(i)+"===========")
    #     print(my_email[i])
    #     msg_to = '1508691067@qq.com'
    #     file_path='1.png'
    #     my_str="除了自己，任何人都无法给你力量。没有口水与汗水，就没有成功的泪水。"
    #     # msg_from="wei_wei1992@yeah.net"
    #     # password="TTYKQLURURNBDZWY"
    #     msg_from=my_email[i][0]
    #     password=my_email[i][1]
    #     #send_email(msg_to, file_path, my_str, msg_from, password, nick_name, gaokao_time)
    #     nick_name='两书卷'
    #     gaokao_time='224'
    #     send_email(msg_to, file_path, my_str, msg_from, password,nick_name,gaokao_time)
    #     time.sleep(10)








    #
    # now_time = datetime.datetime.now()
    # year = now_time.year
    # month = now_time.month
    # day = now_time.day
    # hour=now_time.hour
    # mint=now_time.minute
    # mytime = str(year) + " 年 " + str(month) + " 月 " + str(day) + " 日 " +str(hour) + " 时 " +str(mint)+" 分 "
    # print(mytime)


    # my_send()
    #my_send(excel_path,msg_to)