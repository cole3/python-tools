#!python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "w1c2g3@163.com"  # 用户名
mail_pass = "dagang123$%^"  # 口令

sender = 'w1c2g3@163.com'
receivers = ['w1c2g3@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python send mail test...', 'plain', 'utf-8')
message['From'] = "w1c2g3@163.com"
message['To'] = "w1c2g3@163.com"

subject = 'Python SMTP mail test'
message['Subject'] = Header(subject, 'utf-8')

try:
	print 1
	smtpObj = smtplib.SMTP()
	print 2
	smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
	print 3
	smtpObj.login(mail_user, mail_pass)
	print 4
	smtpObj.sendmail(sender, receivers, message.as_string())
	print "mail success"
except smtplib.SMTPException:
    print "Error: fail"