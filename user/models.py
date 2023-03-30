from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify
# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=100, verbose_name = 'İsim')
    surname = models.CharField(max_length=100, verbose_name = 'Soyisim')
    bio = models.TextField(max_length = 500, verbose_name = 'Hakkımda', default="Merhaba ben bir blog yazarıyım.")
    image = models.FileField(upload_to='profiles/', null=True, verbose_name='Profil Resmi', default='profiles/default.jpg')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Oluşturulma Tarihi')
    follow = models.ManyToManyField('self', related_name='takip', symmetrical=False, verbose_name = 'Takip', blank = True)
    followers = models.ManyToManyField('self', related_name='takipci', symmetrical=False, verbose_name='Takipçiler', blank = True)
    slug = models.SlugField(null=True, blank=True, editable=False)
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username.replace('ı', 'i'))
        super().save(*args, **kwargs)

#ckeditor
