from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class slideImage(models.Model):
    title = models.CharField('图片标题',max_length=255,default='')
    slidepic = models.ImageField('首页轮播图片1360*250',upload_to='uploads/top_images/',default='uploads/top_images/slide.jpg')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '首页轮播图片'


class Categary(models.Model):
    categary = models.CharField('分类', max_length=255, default= "安全热点")
    url = models.CharField("URL", max_length=255, default="")
    num = models.IntegerField()

    def __str__(self):
        return self.categary

    class Meta:
        ordering = ['num']
        verbose_name = '首页类别'

class Article(models.Model):
    toutiao = models.BooleanField('设为头条', default=False)
    categary = models.ForeignKey(Categary)
    pic = models.ImageField('头条图片436*200',upload_to='uploads/top_images/', default='uploads/top_images/default.jpg')
    title = models.CharField('标题',max_length=255)
    abstract = models.TextField('摘要', default='', blank=True)
    content = UEditorField('内容', height=500, width=1200,
        default='', blank=True, imagePath="uploads/images/%(basename)s_%(datetime)s.%(extname)s",
        toolbars='full', filePath='uploads/files/%(basename)s_%(datetime)s.%(extname)s')
    published = models.BooleanField('正式发布',default=True)
    pub_date = models.DateTimeField('发表日期')
    author = models.CharField('作者',default='清朗安全',max_length=255)
    sourcefrom = models.CharField('来源',default='清朗安全',max_length=255)
    slug_url = models.CharField('默认网址勿改',default='focus_detail',max_length=255)
    slug_name = models.CharField('默认栏目名勿改', default='安全热点',max_length=255)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '文章'


