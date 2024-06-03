from django.contrib.auth.models import User
from django.db import models
from shortuuidfield import ShortUUIDField


class Profile(models.Model):
    uid = ShortUUIDField(primary_key=True, editable=False, verbose_name='用户ID', help_text='用户ID')
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name='手机号码',
                             help_text='手机号码')
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True, verbose_name='邮箱',
                              help_text='邮箱')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/', blank=True, null=True, verbose_name='头像',
                               help_text='头像')

    is_upgrade = models.BooleanField(default=False, verbose_name='是否升级为会员', help_text='是否升级为会员')
    upgrade_time = models.DateTimeField(blank=True, null=True, verbose_name='升级时间', help_text='升级时间')
    expire_time = models.DateTimeField(blank=True, null=True, verbose_name='到期时间', help_text='到期时间')
    upgrade_count = models.IntegerField(default=0, verbose_name='升级次数', help_text='升级次数')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='用户',
                                help_text='用户')
    movies = models.ManyToManyField('movie.Movie', related_name='profiles', blank=True, verbose_name='收藏电影',
                                    help_text='收藏电影')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
