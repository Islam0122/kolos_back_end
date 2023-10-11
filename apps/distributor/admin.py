from django.contrib import admin
from .models import Distributor, ArchiveDistributor

# from apps.distributor import models


# Register your models here.
admin.site.register(Distributor)
admin.site.register(ArchiveDistributor)

