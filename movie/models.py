from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="分类名称")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


Region = (
    (1, "中国"),
    (2, "美国"),
    (3, "日本"),
    (4, "韩国"),
    (5, "英国"),
    (6, "法国"),
    (7, "德国"),
    (8, "其他"),
)

IsHot = (
    (True, "是"),
    (False, "否"),
)

IsTop = (
    (True, "是"),
    (False, "否"),
)

Quality = (
    (1, "高清"),
    (2, "超清"),
    (3, "蓝光"),
)

IsShow = (
    (True, "是"),
    (False, "否"),
)

IsFree = (
    (True, "是"),
    (False, "否"),
)


class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name="电影名称")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="电影分类")
    release_year = models.IntegerField(verbose_name="上映年份")
    director = models.CharField(max_length=100, verbose_name="导演")
    scriptwriter = models.CharField(max_length=100, verbose_name="编剧")
    actors = models.CharField(max_length=100, verbose_name="主演")
    region = models.SmallIntegerField(choices=Region, verbose_name="地区")
    types = models.CharField(max_length=100, verbose_name="类型")
    language = models.CharField(max_length=100, verbose_name="语言")
    release_date = models.DateField(verbose_name="上映日期")
    duration = models.CharField(max_length=100, verbose_name="片长")
    alternate_name = models.CharField(max_length=100, verbose_name="又名")
    image_url = models.URLField(verbose_name="海报链接")
    rate = models.FloatField(verbose_name="评分")
    review = models.TextField(verbose_name="简介")
    is_hot = models.BooleanField(choices=IsHot, default=False, verbose_name="是否热门")
    is_top = models.BooleanField(choices=IsTop, default=False, verbose_name="是否置顶")
    quality = models.SmallIntegerField(choices=Quality, verbose_name="画质")
    subtitle = models.CharField(max_length=100, verbose_name="字幕")
    update_info = models.CharField(max_length=100, verbose_name="更新信息")
    update_progress = models.CharField(max_length=100, verbose_name="更新进度")
    download_info = models.CharField(max_length=500, verbose_name="网盘链接", help_text="格式：链接+密码")
    is_show = models.BooleanField(choices=IsShow, default=True, verbose_name="是否显示")
    is_free = models.BooleanField(choices=IsFree, default=True, verbose_name="是否免费")

    class Meta:
        verbose_name = "电影"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
