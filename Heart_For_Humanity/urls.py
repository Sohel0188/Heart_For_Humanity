
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blogs.urls')),
    path('events/', include('events.urls')),
    path('campain/', include('campain.urls')),
    path('account/', include('account.urls')),
    path('volunteer/', include('volunteer.urls')),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)