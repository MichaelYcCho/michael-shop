from django.contrib import admin
from accounts.models import User

# Read User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff')

    filter_horizontal = ()
