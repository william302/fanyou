from django.contrib import admin

# Register your models here.
from .models import Candidate, VoteRecord, Activity


admin.site.register(Candidate)
admin.site.register(VoteRecord)
admin.site.register(Activity)
