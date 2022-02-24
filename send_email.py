## 실행전 설치해야 할 라이브럴리~
## pip install snmtplib
## pip install MIMEText

## 20210930@easy on the eyes

import os
import smtplib
from email.encoders import encode_base64
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()      # say Hello
smtp.starttls()  # TLS 사용시 필요
smtp.login('mrgoharm', 'wpexswuhtsfcnswk')


msg = MIMEMultipart()


msg['To'] = input('전달받으실 이메일 입력 : ')


from email.header import Header
msg['Subject'] = Header(s='이지 온 아이즈 "대갈장군"이 왔습니다.', charset='utf-8')

from email.mime.text import MIMEText
body = MIMEText('이지 온 아이즈 "대갈장군"을 사용해 주셔서 감사합니다. team Easy on the eyes' , _charset='utf-8')
msg.attach(body)

files = list()
files.append('C:\python\\rapa\\opencv\\kakao_talk\\seoul.jpg')

import os
from email.mime.base import MIMEBase
from email.encoders import encode_base64
for f in files:
     part = MIMEBase('application', "octet-stream")
     part.set_payload(open(f,"rb").read())
     encode_base64(part)
     part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
     msg.attach(part)

smtp.sendmail('mrgoharm@gmail.com', msg['To'], msg.as_string())
 
smtp.quit()

print('발송했습니다.')