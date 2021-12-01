"""i2dbackend URL Configuration
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

"""por cada aplicación nueva, se debe incluir la url aquí debajo"""
"""aquí se importan las urls de las aplicaciones locales que se usan en el proyecto"""
urlpatterns = [
    path('admin/', admin.site.urls),
    # se incluyen las urls de las apps
    re_path('',include('applications.dpto.urls')),
    re_path('',include('applications.mupio.urls')),
    re_path('',include('applications.mupiopolitico.urls')),
    re_path('',include('applications.gbif.urls')),
    re_path('',include('applications.user.urls')),
    re_path('',include('applications.cars.urls')),
]
