from django.conf.urls import url
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'coupons'
urlpatterns = [
    url(_(r'^apply/$'), views.coupon_apply, name='apply'),
]