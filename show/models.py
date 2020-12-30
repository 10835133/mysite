from django.db import models

# Create your models here.
#借閱人
class Borrower(Model):
    realname = CharField('姓名', max_length=32)
    position = CharField('身分', max_length=255)
    job = CharField('職稱')
    tel= CharField('聯絡電話')
    email= EmailField

    def __str__(self):
        return "{} / {} / {}".format(
            self.realname, 
            self.position, 
            self.tel
        )