from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('a_home.urls')),
    path('about/', include('a_home.urls')),
    path('portfolio/', include('a_portfolio.urls')),
    path('', include('a_portfolio.urls')),
    path('flower/', include('a_flower.urls')),
    path('', include('a_flower.urls')),
    path('service/', include('a_service.urls')),
    path('', include('a_service.urls')),
    path('blog', include('a_blog.urls')),

]



"""нам будут доступны все медиа файлы.В режиме debug мы сможем перейти 
 к ним прямо в браузере, когда вылез какой-нибудь трейсбек ошибки, 
 и вообще это упрощает отладку приложения"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#конфигурация надписи админ в админке джанго
admin.site.site_header = "Моя Админка Flower&Gifts"
admin.site.site_title = "Flowers & Gifts"
admin.site.index_title = "Добро Пожаловать в админку Flowers&Gifts"