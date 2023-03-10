from django.contrib import admin

from .models import Disease
from .models import Medtype
from .models import Medicine

admin.site.register(Disease)
admin.site.register(Medtype)
admin.site.register(Medicine)
