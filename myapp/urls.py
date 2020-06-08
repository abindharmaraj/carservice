from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.fn_index),
    path('prohome',views.prohome),
    path('proser',views.proser),
    path('adm',views.adm),
    path('admn',views.admn),
    path('log',views.lo),
    path('tab',views.tab,name='tab'),
    path('text1/<int:id>',views.textdel),
    path('text2/<int:id>',views.textup),
    path('updateform/<int:id>',views.updateform),
    path('user',views.user),
    path('home',views.home,name='home'),
    path('lout',views.lout,name='lout'),
    path('file',views.file),
    path('fileup',views.fileup),
    path('save',views.save),
    path('ajform',views.ajform),
    path('ajf',views.ajf),
    path('ajtab',views.ajtab),
    path('displaydata',views.displaydata),
    path('delaj',views.delaj,name='delaj'),
    path('apiins',views.apiins,name='apiins'),
    path('apiget',views.apiget,name='apiget'),
    path('apidel',views.apidel,name='apidel'),
]