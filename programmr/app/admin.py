from django.contrib import admin

# Register your models here.
from app.models import Users
from app.models import Questions
from app.models import Submission


admin.site.register(Users)
admin.site.register(Questions)
admin.site.register(Submission)

