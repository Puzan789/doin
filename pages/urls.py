from django.urls import path
from .views import blog, blogdetail, contact, index,blog

urlpatterns = [
    path("", index, name="index"),
    path("blogs/", blog, name="blogs"),
    path("blogdetail/<int:id>",blogdetail,name='blogdetail'),
    path("contact/",contact,name='contact'),
]