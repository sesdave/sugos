from django.conf.urls import url
from django.views.generic import TemplateView
urlpatterns = [
    url(r"^process_payment/$", TemplateView.as_view(template_name="sample.html"), name="home"),
]