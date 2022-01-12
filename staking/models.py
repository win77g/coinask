from django.db import models
from django.db.models.signals import  pre_save

# Create your models here.
class StakingCoin(models.Model):
    name = models.CharField(verbose_name='Название',max_length=120,blank=True, null=True )
    logo = models.CharField(verbose_name='Логотип',max_length=120,blank=True, null=True )
    dayplan = models.CharField(verbose_name='Дни',max_length=120,blank=True, null=True )
    procent = models.CharField(verbose_name='Процент',max_length=120,blank=True, null=True )
    mindeposit = models.CharField(verbose_name='Мин.депозит',max_length=120,blank=True, null=True )
    maxdeposit = models.CharField(verbose_name='Макс.депозит',max_length=120,blank=True, null=True )
    # image = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None,verbose_name='Фотка')
    slug = models.SlugField(blank=True, null=True, default=None,verbose_name='Транслит(Не трогать)')
    is_active = models.BooleanField(default=True,verbose_name='В наличии')
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name='Дата последнего обновления')
    # вывод одного поля
    def __str__(self):
        return " %s" % self.name
    class Meta:
        verbose_name = 'Монета Стекинга'
        verbose_name_plural = 'Монета Стекинга'
# автоматическое сохранение в слаг
def pre_save_brend_slug(sender,instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.name, reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_brend_slug, sender=StakingCoin)