from gmail import GMail, Message
from random import randint
from datetime import datetime

now = datetime.now()

sickness_list = ["Tiêu chảy","Táo bón","Viêm dạ dày","Sỏi mật"]

i = randint(0,len(sickness_list)-1)

sickness = sickness_list[i]

html_templace = ''' <p><strong>Ch&agrave;o sếp&nbsp;</strong></p>
<p><strong>Dạo n&agrave;y em sống v&ocirc; tổ chức ăn uống linh tinh n&ecirc;n sinh ra bệnh</strong></p>
<p><strong>S&aacute;ng nay em c&oacute; đi kh&aacute;m bệnh b&aacute;c sỹ bảo em bị {{sickness}} nặng</strong></p>
<p><strong>Em xin nghỉ buổi l&agrave;m ng&agrave;y h&ocirc;m nay để điều trị bệnh</strong></p>
<p><strong><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-innocent.gif" alt="innocent" />Em cảm ơn sếp !!!</strong></p>

'''

html_templace.replace("{{sickness}}",sickness)

gmail = GMail('cuongnguyendtvt6108@gmail.com','cuonglung2809')
msg = Message('Đơn xin nghỉ làm ',to='nguyencuong.hust6108@gmail.com',text='Chào sếp',html=html_templace)


if now.hour >= 7:
    gmail.send(msg)
    
else:
    print("Tôi không nhận đơn trước 7h sáng")

