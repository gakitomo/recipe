from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from lib.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/', include("recipe.urls", namespace = "recipe")),
    path('comment/', include("comment.urls", namespace = "comment")),
    path('userpage/',include("userpage.urls", namespace = "userpage")),
    path('login', LoginView.as_view(template_name = "login.html"), name = "login"),

    path('', IndexTemplateView.as_view(), name = "index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)