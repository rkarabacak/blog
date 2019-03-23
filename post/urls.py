from django.conf.urls import url
from .views import * # aynı dizinde bulunan views içindeki adresleri import ettik
from home.views import home_view # yeni sayfamızı once import ediyoruz

app_name = 'post'

urlpatterns = [

    url(r'^index/$', post_index, name='index'), # yeni bir sayfa oluşturduk
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'), # duzenli ifade kullanarak birden fazla değişken rakam almasını sağladık
    # " r' " = duzenli ifade olduğunu belirtir " ^ " = düzenli ifadenin başladığını " $ "= düzenli ifadenin bittiğini
    # " ?P<id> " = parametre taşımak için "id" adında bir arguman tanımladık " ?P " = parametre
    # " (\d+) " = \d bir rakam olduğunu " + " yanına başka rakam gelebileceğini belirttik
    url(r'^(?P<slug>[\w-]+)/update/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
    ]