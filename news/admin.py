from django.contrib import admin

# Register your models here.
from .models import Article, Categary, slideImage
from django.utils.timezone import now

class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', "categary",'pub_date', 'toutiao', 'published', 'sourcefrom']
    actions = ['modify_to_now', 'make_published',
               'set_them_top', 'drop_published',
               'drop_them_top',
               "modify_to_3", "modify_to_8", "modify_to_9", "modify_to_10", "modify_to_11", "modify_to_12"]
    list_per_page = 20

    def make_published(self, request, queryset):
        queryset.update(published=True)

    make_published.short_description = "选定出版"

    def set_them_top(self, request, queryset):
        queryset.update(toutiao=True)

    set_them_top.short_description = "选定置顶"

    def drop_published(self, request, queryset):
        queryset.update(published=True)

    drop_published.short_description = "取消出版"

    def drop_them_top(self, request, queryset):
        queryset.update(toutiao=True)

    drop_them_top.short_description = "取消置顶"
    ### ==============================

    def modify_to_now(self, request, queryset):
        queryset.update(pub_date=now())

    modify_to_now.short_description = "选定时间为现在"

    def modify_to_3(self, request, queryset):
        queryset.update(categary_id=3)

    modify_to_3.short_description = "->南方安全"

    def modify_to_8(self, request, queryset):
        queryset.update(categary_id=8)

    modify_to_8.short_description = "->主题活动"

    def modify_to_9(self, request, queryset):
        queryset.update(categary_id=9)

    modify_to_9.short_description = "->热点专题"

    def modify_to_10(self, request, queryset):
        queryset.update(categary_id=10)

    modify_to_10.short_description = "->网络安全法"

    def modify_to_11(self, request, queryset):
        queryset.update(categary_id=11)

    modify_to_11.short_description = "->公民个人信息"

    def modify_to_12(self, request, queryset):
        queryset.update(categary_id=12)

    modify_to_12.short_description = "->NSA武器库"




class CategaryAdmin(admin.ModelAdmin):

    list_display = ['categary', 'url', 'num']

admin.site.register(Article, ArticleAdmin)

admin.site.register(Categary, CategaryAdmin)

admin.site.register(slideImage)

