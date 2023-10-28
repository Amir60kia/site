from django.db.models import OuterRef
from django.shortcuts import render, redirect
from .models import Post_1,Post_2,Post_3,Post_4,Post_5,Post_6,Post_7,Post_8
def home(request):

    
    try:
        homes = Post_1.objects.latest("id")
        section_2 = Post_2.objects.latest("id")
        section_3 = Post_3.objects.all().order_by('-created_time')[:4]
        section_4 = Post_4.objects.latest("id")
        section_5 = Post_5.objects.all().order_by('-created_time')[:4]
        section_6 = Post_6.objects.latest("id")
        section_7 = Post_7.objects.latest("id")
        section_8 = Post_8.objects.latest("id")
        comments_1 = homes.comments.latest('id')
        image_filename = homes.image.name
        image_gallery_1=section_6.image_6_1.name
        image_gallery_2 = section_6.image_6_2.name
        image_gallery_3 = section_6.image_6_3.name


    except:
        comments=" "
        homes = ''
        section_2 =''
        section_3 = ''
        section_4 = ''
        section_5 = ''
        section_6 =''
        section_7 = ''
        section_8 = ''




    return render(request,'index.html', {'data': homes ,'comments_1': comments_1 ,
                                         'image_filename': image_filename ,'section_2':section_2,'section_3':section_3 ,
                                         'section_4':section_4 ,'section_5':section_5,'image_gallery_1':image_gallery_1,'image_gallery_2':image_gallery_2,'image_gallery_3':image_gallery_3,'section_6':section_6 ,'section_7':section_7,'section_8':section_8})

