from django.contrib import admin
from .models import Author, JobPost, Location, Skills
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display= ('title','date','salary')
    list_filter=('date','salary')
    search_fields = ('title','salary')
    search_help_text = "Write in your query"
    # exclude = ('title', )
    # fields = (('title', 'description'), 'expiry')
    fieldsets = (
        ('Basic Information', {
            'fields':('title', 'description')
        }),
    )


admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)