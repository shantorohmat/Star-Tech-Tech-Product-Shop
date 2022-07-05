from django.contrib import admin
from .models import Project, Tag

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    search_fields = ['title', 'description', 'tags__name', 'price', 'brand']
    list_editbale = ['project_priority_sl', 'title', 'price', 'brand', 'key_feature']
    list_display_links = ['title']
    list_display = ('title', 'search_tags', 'project_priority_sl', 'brand', 'price', 'key_feature')
    def search_tags(self,obj):
        return ", ".join([t.name for t in obj.tags.all()])


class TagAdmin(admin.ModelAdmin):
    # fields = ('title', 'tags', 'created')
    date_hierarchy = 'created'
    search_fields = ['name']
    # list_display = ('name')
# class registerAdmin(admin.ModelAdmin):
#     list_display = ('username','email')

# admin.site.register(register, registerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.site_header = 'ProjectHub Admin Dashboard'
admin.site.site_title = 'ProjectHub | All Projects in One Place!'
