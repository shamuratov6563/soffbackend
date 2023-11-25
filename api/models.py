from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from django.dispatch import receiver
import requests

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Advantage(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="poster/")
    tags = models.ManyToManyField(Tag)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title


class Course(models.Model):
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=200)
    body = RichTextUploadingField()
    order = models.IntegerField(default=1)

    def __str__(self):
        return  self.name

    class Meta:
        ordering = ("order",)


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="author_images/")
    position = models.CharField(max_length=50)

    def __str__(self):
        return  self.full_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="article_images/")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="gallery_images/")

    def __str__(self):
        return self.title


class Way2Job(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title


class ApplicationForm(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name} - {self.phone_number}"


@receiver(pre_save, sender=ApplicationForm)
def send_to_telegram_bot(sender, instance, **kwargs):
    TOKEN = "6489312836:AAH22vCCADPE-XeSPeJ9NybI-7X9jO0mPU4"
    CHAT_ID = 385419373

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    text = f"""
        Arizachiining ismi: {instance.full_name}\n
        Telefon raqami : {instance.phone_number}
    """    
    params = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url=url, params=params)


