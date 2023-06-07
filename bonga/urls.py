from django.contrib import admin
from django.urls import path, include
from dal import autocomplete

from school.models import School

api_version = 'api/v1/'

api_patterns = [
    path(api_version + 'users/', include('appuser.api.urls')),
    path(api_version + 'payments/', include('payments.api.urls')),
    path(api_version + 'students/', include('student.api.urls')),
    path(api_version + 'schools/', include('school.api.urls')),
    path(api_version + 'contacts/', include('contact.api.urls')),
    path(api_version + 'mobiles/', include('mobile.api.urls')),
    path(api_version + 'constants/', include('constants.api.urls')),
    path(api_version + 'calls/', include('calls.api.urls')),
    path(api_version + 'tokens/', include('tokens.api.urls')),

    path('', include('web.urls')),

    path(
        'school-autocomplete/',
        autocomplete.Select2QuerySetView.as_view(model=School),
        name="school-autocomplete"
    )

]

urlpatterns = api_patterns + [
    path('admin/', admin.site.urls),
]
