from django.contrib import admin
from .models import Post_1,Post_2,Post_3,Post_4,Post_5,Post_6,Post_7,Post_8,Comment_1,Comment_2,Comment_3,Comment_4,Comment_5,Comment_6,Comment_7,Comment_8

class CommentAdminInline_1(admin.TabularInline):
    model=Comment_1
    fields=['text',]
    extra=0

@admin.register(Post_1)
class PostAdmin_1(admin.ModelAdmin):
    list_display=['id','titel','is_enebel','publish_date']
    inlines=[CommentAdminInline_1]

class CommentAdminInline_2(admin.TabularInline):
    model=Comment_2
    fields=['text',]
    extra=0

@admin.register(Post_2)
class PostAdmin_2(admin.ModelAdmin):
    list_display=['id','titel','is_enebel','publish_date']
    inlines=[CommentAdminInline_2]

class CommentAdminInline_3(admin.TabularInline):
    model=Comment_3
    fields=['text',]
    extra=0

@admin.register(Post_3)
class PostAdmin_3(admin.ModelAdmin):
    list_display=['id','titel','is_enebel','publish_date']
    inlines=[CommentAdminInline_3]

class CommentAdminInline_4(admin.TabularInline):
    model=Comment_4
    fields=['text',]
    extra=0

@admin.register(Post_4)
class PostAdmin_4(admin.ModelAdmin):
    list_display=['id','titel','is_enebel','publish_date']
    inlines=[CommentAdminInline_4]

class CommentAdminInline_5(admin.TabularInline):
    model=Comment_5
    fields=['text',]
    extra=0

@admin.register(Post_5)
class PostAdmin_5(admin.ModelAdmin):
    list_display=['id','titel','is_enebel','publish_date']
    inlines=[CommentAdminInline_5]


class CommentAdminInline_6(admin.TabularInline):
    model = Comment_6
    fields = ['text', ]
    extra = 0


@admin.register(Post_6)
class PostAdmin_6(admin.ModelAdmin):
    list_display = ['id', 'titel', 'is_enebel', 'publish_date']
    inlines = [CommentAdminInline_6]

class CommentAdminInline_7(admin.TabularInline):
    model = Comment_7
    fields = ['text', ]
    extra = 0


@admin.register(Post_7)
class PostAdmin_7(admin.ModelAdmin):
    list_display = ['id', 'titel', 'is_enebel', 'publish_date']
    inlines = [CommentAdminInline_7]

class CommentAdminInline_8(admin.TabularInline):
    model = Comment_8
    fields = ['text', ]
    extra = 0


@admin.register(Post_8)
class PostAdmin_8(admin.ModelAdmin):
    list_display = ['id', 'titel', 'is_enebel', 'publish_date']
    inlines = [CommentAdminInline_8]


