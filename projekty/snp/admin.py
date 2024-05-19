from django.contrib import admin

# Register your models here.

from .models import Species, Chromosome, Snp, Annotation

admin.site.register(Species)
admin.site.register(Chromosome)
admin.site.register(Snp)
admin.site.register(Annotation)