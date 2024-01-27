from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shoesapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('allshoes/', views.allshoes, name='allshoes'),
    path('shoesdetails/<str:id>/', views.shoesdetails, name='shoesdetails'),
    path('shoessort/<str:id>/', views.shoessort, name='shoessort'),
    path('shoessize/<str:id>/', views.shoessize, name='shoessize'),
    path('shoescondition/<str:id>/', views.shoescondition, name='shoescondition'),
    path('shoesprice/', views.shoesprice, name='shoesprice'),
    path('videos/', views.videos, name='videos'),
    path('shoesreviews/', views.shoesreviews, name='shoesreviews'),
    path('gallery/', views.gallery, name='gallery'),
    path('query/', views.query, name='query'),
    path('returnpolicy/', views.returnpolicy, name='returnpolicy'),
    path('deals/', views.deals, name='deals'),
    path('dealsdetails/<str:id>/', views.dealsdetails, name='dealsdetails'),
    path('bestselling/', views.bestselling, name='bestselling'),
    path('bestsellingdetails/<str:id>/', views.bestsellingdetails, name='bestsellingdetails'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
