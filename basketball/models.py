from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Activity(models.Model):
    slug = models.SlugField('活动标题', unique=True, help_text='用于URL地址，请勿填写中文')
    title = models.CharField('活动名称', max_length=200)
    image = ProcessedImageField(verbose_name='活动图片',
                                upload_to='activity',
                                processors=[ResizeToFill(640, 379)],
                                format='JPEG',
                                options={'quality': 60})
    start_time = models.DateTimeField('开始时间')
    end_time = models.DateTimeField('结束时间')
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        verbose_name = '活动名'
        verbose_name_plural = '活动名'


class Candidate(models.Model):
    name = models.CharField('姓名', max_length=20)
    mobile = models.CharField('手机号', max_length=11, blank=True)
    description = models.TextField('自我简介', max_length=200)
    avatar = ProcessedImageField(verbose_name='头像',
                                 upload_to='basketball_avatar',
                                 processors=[ResizeToFill(350, 350)],
                                 format='JPEG',
                                 options={'quality': 60})
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(150, 150)],
                                      format='JPEG',
                                      options={'quality': 60})
    votes = models.PositiveIntegerField('票数', default=0)
    # activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='所属活动')

    def __str__(self):
        return self.name

    def increase_votes(self):
        self.votes += 1
        self.save(update_fields=['votes'])

    class Meta:
        verbose_name = '参赛选手'
        verbose_name_plural = '参赛选手'


class VoteRecord(models.Model):
    mobile = models.CharField('手机号', max_length=11)
    created_time = models.DateTimeField('投票时间', auto_now_add=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, verbose_name='选择的投票对象')

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name = '投票记录'
        verbose_name_plural = '投票记录'
