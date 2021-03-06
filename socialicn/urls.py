"""socialicn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from socialicn import views
from django.conf import settings
from dispatch import receiver
from paystack import signals


@receiver(signals.successful_payment_signal)
def on_successful_payment(sender, **kwargs):
    import pdb

    pdb.set_trace()
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^', include('user_registration.urls')),
    url(r'^', include('user_profile.urls')),
    url(r'^', include('home.urls')),
    #url(r'^', include('process_payment.urls')),
    url(r'^paystack/', include(('paystack.urls', 'paystack'), namespace="paystack")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
