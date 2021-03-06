from django.conf.urls import url, include

from media import views

urlpatterns = [
  url(r'^photo/search/$',views.photo_search,name='photo_search'),
  url(r'^photo/tag/$',views.tag_photo,name='tag_photo'),
  url(r'^photo/insert/$',views.insert_photo,name='insert_photo'),
  url(r'^photo/add/$',views.add_photo,name='add_photo'),
  url(r'^photo/bulk_tag/$',views.bulk_tag_index,name='bulk_tag_index'),
  url(r'^photo/bulk_tag/(\d+)/$',views.bulk_tag_detail,name='bulk_tag_detail'),
  url(r'^photo/bulk_upload/$',views.bulk_photo_upload,name='bulk_photo_upload'),
  url(r'^photo/untag/$',views.untag_photo,name='untag_photo'),
  url(r'^photo/delete/(\d+)/$',views.delete_photo,name='delete_photo'),
  url(r'^photo/edit/(\d+)/$',views.edit_photo,name='edit_photo'),
  url(r'^private/$',views.post_file,name="post_private_file"),
  url(r'^private/(.*)',views.private_file,name='private_file'),
]
