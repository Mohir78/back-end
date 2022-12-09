from django.urls import path, include

urlpatterns = [
    path('blog/', include('apps.blog.urls')),
    path('group/', include('apps.group.urls')),
    path('notifications/', include('apps.notifications.urls')),
]
