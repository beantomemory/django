from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^upimg", Upimg, name="upimg")
]