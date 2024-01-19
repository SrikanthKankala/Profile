from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact,Experience,Skill, Education, Achievement , About, WorkPortfolio, PlaceLived, Relationship
# Register your models here.
admin.site.register(Contact)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register (Achievement )
admin.site.register(About)
admin.site.register(WorkPortfolio)
admin.site.register(PlaceLived)
admin.site.register(Relationship)