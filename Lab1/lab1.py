from gmail import GMail, Message
from random import randint

sickness_list = ["thương hàn","kiết lị","tiêu chảy"]
i = randint(0,len(sickness_list)-1)
#1. Select a sickness_list
sickness = sickness_list[i]


html_template = '''<p>Ch&agrave;o sếp,</p>
<p>S&aacute;ng nay thức dậy,em thấy m&igrave;nh mệt mỏi, bụng đau quằn quại em bi {{sickness}}</p>
<p><strong>Sếp cho em nghỉ sớm&nbsp;</strong><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-innocent.gif" alt="innocent" /></p>
<p>Em cảm ơn sếp</p>
'''
#2. sickness + html_teamlate => html_content
# Hint : google: string replace
html_template.replace("{{sickness}}",sickness)


gmail = GMail('A.CuongNguyen<cuongnguyendtvt6108@gmail.com>','cuonglung2809')
msg = Message('Hello my name is Cuong',to='C4e.techkidsvn@gmail.com',text='Hello',html=html_template)
gmail.send(msg)



