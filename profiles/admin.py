from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserInlines(admin.StackedInline):
    model = UserProfile
    can_delete = False
    fields = ('patronymic', 'avatar', 'information')
    verbose_name_plural = "Дополнительная информация"


class UserProfileAdmin(UserAdmin):
    inlines = (UserInlines, )


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
