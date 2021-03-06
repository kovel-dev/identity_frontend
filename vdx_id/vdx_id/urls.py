"""vdx_id
vdx_id URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
import notifications.urls

app_name = 'vdx_id'


iam_urls = [
    path('identities/', include('id_identities.urls')),
    path('accounts/', include('id_accounts.urls')),
    path('access/', include('id_access.urls')),
]

system_urls = [
    path('platforms/', include('id_platforms.urls')),
    path('servers/', include('id_servers.urls')),
    path('agents/', include('id_work_agent.urls')),
]

api_urls = [
    path('iam/', include((iam_urls, 'iam'), namespace='iam')),
    path('sys/', include((system_urls, 'sys'), namespace='sys')),
]

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('accounts/', include('django.contrib.auth.urls')),
    path('allauth_accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),  # admin site
    path('admin_tools/', include('admin_tools.urls')),  # admin site
    # Todo: https://django-admin-tools.readthedocs.io/en/latest/customization.html

    path('', include(('web_interface.urls', 'web'),
        namespace='web')),  # admin site
    path('api/', include((api_urls, 'api'),
        namespace='api')),  # admin site

    path('inbox/notifications/', include(
        (notifications.urls, 'notifications'), namespace='notifications')),

    path('docs_api/', get_swagger_view(title="Vdx Iam API")),
    path('explorer/', include('explorer.urls')),
    path('report_builder/', include('report_builder.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
