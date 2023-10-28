from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django import forms

class Post_1(models.Model):
    titel=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    is_enebel=models.BooleanField(default=False)
    publish_date=models.DateField(null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='./static/image', default='avatar.png')
    def __str__(self):
        # return self.titel
        return '{} -{}'.format(self.pk ,self.titel)
class Comment_1(models.Model):
    post =models.ForeignKey(Post_1,related_name='comments',on_delete=models.CASCADE)
    text = models.TextField()
    reated_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
class Post_2(models.Model):
    titel=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    is_enebel=models.BooleanField(default=False)
    publish_date=models.DateField(null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        # return self.titel
        return '{} -{}'.format(self.pk ,self.titel)
class Comment_2(models.Model):
    post =models.ForeignKey(Post_2,related_name='comments_2',on_delete=models.CASCADE)
    text = models.TextField()
    reated_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Post_3(models.Model):
    titel=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    is_enebel=models.BooleanField(default=False)
    publish_date=models.DateField(null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        # return self.titel
        return '{} -{}'.format(self.pk ,self.titel)
class Comment_3(models.Model):
    post =models.ForeignKey(Post_3,on_delete=models.CASCADE)
    text = models.TextField()
    reated_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Post_4(models.Model):
    titel=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    is_enebel=models.BooleanField(default=False)
    publish_date=models.DateField(null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        # return self.titel
        return '{} -{}'.format(self.pk ,self.titel)
class Comment_4(models.Model):
    post =models.ForeignKey(Post_4,on_delete=models.CASCADE)
    text = models.TextField()
    reated_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class Post_5(models.Model):
    titel=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    is_enebel=models.BooleanField(default=False)
    publish_date=models.DateField(null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    image_5 = models.ImageField(upload_to='./static/image', default='avatar.png')
    def __str__(self):
        # return self.titel
        return '{} -{}'.format(self.pk ,self.titel)
class Comment_5(models.Model):
    post =models.ForeignKey(Post_5,on_delete=models.CASCADE)
    text = models.TextField()
    reated_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class Post_6(models.Model):
    titel=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    is_enebel=models.BooleanField(default=False)
    publish_date=models.DateField(null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    image_6_1=models.ImageField(upload_to='./static/gallery', default='avatar.png')
    image_6_2 = models.ImageField(upload_to='./static/gallery', default='avatar.png')
    image_6_3 = models.ImageField(upload_to='./static/gallery', default='avatar.png')
    def __str__(self):
        # return self.titel
        return '{} -{}'.format(self.pk ,self.titel)
class Comment_6(models.Model):
    post =models.ForeignKey(Post_6,on_delete=models.CASCADE)
    text = models.TextField()
    reated_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Post_7(models.Model):
    titel=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    is_enebel=models.BooleanField(default=False)
    publish_date=models.DateField(null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        # return self.titel
        return '{} -{}'.format(self.pk ,self.titel)
class Comment_7(models.Model):
    post =models.ForeignKey(Post_7,on_delete=models.CASCADE)
    text = models.TextField()
    reated_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class Post_8(models.Model):
    titel=models.CharField(max_length=50)
    text=models.TextField(blank=True)
    is_enebel=models.BooleanField(default=False)
    publish_date=models.DateField(null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        # return self.titel
        return '{} -{}'.format(self.pk ,self.titel)
class Comment_8(models.Model):
    post =models.ForeignKey(Post_8,on_delete=models.CASCADE)
    text = models.TextField()
    reated_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

