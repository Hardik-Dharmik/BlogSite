from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="BlogHome"),
    path("<str:slug>",views.viewblog,name="viewblog"),
    path("writeblog/",views.write,name="writeBlog"),
    path("showmyblog/",views.showmyblog,name="showmyblog"),
    path("write_comment/",views.write_comment,name="writecomm"),
    path("edit/",views.edit,name="edit"),
    path("delete/",views.delete,name="delete"),
    path("editblog/",views.editblog,name="edit"),
    path("deleteblog/",views.deleteblog,name="deleteblog"),
]
