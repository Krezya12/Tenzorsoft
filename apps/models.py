from django.db import models
from django.db.models import CharField, DateTimeField, Model, BooleanField, TextField, EmailField, ForeignKey, \
    ImageField, CASCADE
from parler.models import TranslatableModel, TranslatedFields


class ContactMessage(Model):
    name = CharField(max_length=120)
    phone = CharField(max_length=30)
    email = EmailField(blank=True)
    message = TextField()
    created_at = DateTimeField(auto_now_add=True)
    is_processed = BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Murojaat'
        verbose_name_plural = 'Murojaatlar'

    def __str__(self):
        return f'{self.name} — {self.phone}'


class Category(TranslatableModel):
    created_at = models.DateTimeField(auto_now_add=True)

    # Все переводимые поля уходят сюда
    translations = TranslatedFields(
        title = models.CharField(max_length=120)
    )

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        # Parler сам вернет title для текущего активного языка
        return self.title


class Project(TranslatableModel):
    # Непереводимые поля и связи остаются в основной модели
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    translations = TranslatedFields(
        title = models.CharField(max_length=120),
        description = models.TextField()
    )

    class Meta:
        verbose_name = "Proyekt"
        verbose_name_plural = "Proyektlar"

    def __str__(self):
        return self.title


class Image(Model):
    image = ImageField(upload_to='images/')
    project = ForeignKey('Project', on_delete=CASCADE, related_name='images')
    created_at = DateTimeField(auto_now_add=True)
