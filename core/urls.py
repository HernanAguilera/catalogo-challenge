from django.conf.urls import url
from . import views

urlpatterns = [
    # Catalogos
    url(regex=r'^catalogos/$',
        view=views.CatalogoList.as_view(),
        name='core.catalogo.list'),
    url(regex=r'^catalogos/(?P<pk>[0-9]+)/$',
        view=views.CatalogoDetail.as_view(),
        name='core.catalogo.detail'),
    # Areas
    url(regex=r'^areas/$',
        view=views.AreaList.as_view(),
        name='core.area.list'),
    url(regex=r'^areas/(?P<pk>[0-9]+)/$',
        view=views.AreaDetail.as_view(),
        name='core.area.detail'),
    # Items
    url(regex=r'^items/$',
        view=views.ItemList.as_view(),
        name='core.item.list'),
    url(regex=r'^items/(?P<pk>[0-9]+)/$',
        view=views.ItemDetail.as_view(),
        name='core.item.detail'),
]