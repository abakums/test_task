from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    # в данной модели определены поля first_name и last_name, так как в модели User они не обязательные
    # необходимо, чтобы в форме после регистрации они были обязательными
    # кроме того, они не отображаются в админ панеле, так как после заполнения они передают свое значение в модель User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    avatar = models.ImageField(upload_to="users/", verbose_name="Аватар")
    information = models.TextField(verbose_name="Информация")

    def __str__(self):
        return self.first_name + " (id: " + str(self.id) + ")"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        default_related_name = "profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
