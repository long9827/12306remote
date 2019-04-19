import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendmail():
    message = MIMEText('请尽快完成支付', 'plain', 'utf-8')
    message['from'] = '909919228@qq.com'
    message['to'] =  '360103381@qq.com'
    
    subject = '订购成功'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP() 
    smtpObj.connect("smtp.qq.com", 25)    # 25 为 SMTP 端口号
    smtpObj.login('909919228@qq.com', 'auxyztdjjntjbdda')
    smtpObj.sendmail('909919228@qq.com', '360103381@qq.com', message.as_string())

if __name__ == "__main__":
    sendmail()