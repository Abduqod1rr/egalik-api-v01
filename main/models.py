from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    HOLAT_CHOICES=[('sotiladi','Sotiladi'),
                   ('ijaraga','Ijaraga')]
    holat=models.CharField(max_length=50,choices=HOLAT_CHOICES,default='sotiladi')
    title=models.CharField(max_length=60,default='empty')
    KATEGORIYA_CHOICES=[('texnika','Texnika'),
                        ('transport','Transport'),
                        ('uskunalar','Uskunalar'),
                        ('kochmas-mulk','Kochmas-mulk')]
    kategoriya=models.CharField(max_length=60,choices=KATEGORIYA_CHOICES,default='texnika')
    tavsilot=models.TextField(default='mahsulot:')
    narx=models.DecimalField(max_digits=10,decimal_places=2)
    rasm=models.FileField(upload_to='products/',null=True)
    number=models.CharField(max_length=13,default='+998000000000')
    telegram=models.CharField(max_length=60,default='@username')

    class Meta:
        ordering=['-id']



    def __str__(self):
        return self.title

