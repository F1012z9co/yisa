from django.db import models

# Create your models here.
class Daoju(models.Model):
    id = models.AutoField(primary_key=True)
    englishName = models.TextField()
    daojuUrl  = models.TextField()
    chineseName = models.TextField()
    imageName = models.TextField()
    imageUrl = models.TextField()
    daojuID = models.TextField()
    daojuChongneng = models.TextField()
    daojuXiaoguo = models.TextField()


class Shipin(models.Model):
    id = models.AutoField(primary_key=True)
    shipinUrl = models.TextField()
    chineseName = models.TextField()
    imageName = models.TextField()
    imageUrl = models.TextField()
    shipinID = models.TextField()
    shipinXiaoguo = models.TextField()


class Wupin(models.Model):
    id = models.AutoField(primary_key=True)
    wupinUrl = models.TextField()
    chineseName = models.TextField()
    imageName = models.TextField()
    imageUrl = models.TextField()
    wupinID = models.TextField()
    wupinXiaoguo = models.TextField()


class Yaowan(models.Model):
    id = models.AutoField(primary_key=True)
    englishName = models.TextField()
    yaowanUrl = models.TextField()
    chineseName = models.TextField()
    yaowanID = models.TextField()
    yaowanXiaoguo = models.TextField()


class Chengjiu(models.Model):
    id = models.AutoField(primary_key=True)
    chengjiuID = models.TextField()
    chengjiuUrl = models.TextField()
    chineseName = models.TextField()
    englishName = models.TextField()
    imageName = models.TextField()
    imageUrl = models.TextField()