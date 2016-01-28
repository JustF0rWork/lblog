from django.conf.urls import url,include
from django.contrib import admin
from views import ArticleListView,ArticlePublishView,ArticleDetailView,ArticleEditView

urlpatterns=[
    url(r'^$', ArticleListView.as_view(), name='blog_index'),
    url(r'^article/publish$',ArticlePublishView.as_view(),name='article_publish'),
    url(r'^article/(?P<title>[^\/])$',ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/(?P<title>\w+)/edit$',ArticleEditView.as_view(), name='article_edit'),

]