from django.shortcuts import render
from .models import blogs,Index
from .forms import blogform

# Create your views here.


def contact(request):
    return render(request, 'blogs/contact.html')


def index(request):
    index_data = Index.objects.all()
    #homepage_data = HomePage.objects.get(id=1)
    context = {
        'head':index_data[0].head,
        'para':index_data[0].para,
        'para2':index_data[0].para2,
        'skills':index_data[0].skills,
        'softwares':index_data[0].softwares,
        'mail':index_data[0].mail,
        'image':index_data[0].image,
    }
    return render(request, "pages/Index.html",context)



def blog(request):
    blogs_list = blogs.objects.all()

    context = {
        'blogs_list':blogs_list,
    }
    
    return render(request, "blogs/blog.html",context)



def blogdetail(request, id):
    blog=blogs.objects.get(id=id)
    context = {
                'blog': blog,
            }
    return render(request, 'blogs/blogdetail.html', context)

def blogupdate(request):
    if request.method=='POST':
        form=blogform(request.POST)
        if form.is_valid():

            print("valid data")
            print('title',form.cleaned_data['title'])
            print('paragraph',form.cleaned_data['email'])
            print('password',form.cleaned_data['password'])
            form=blogform()
            return render(request,'blogs/happen.html',{'form':form})
    else:
        form=blogform()
    return render(request,'blogs/blog_update.html',{'form':form})