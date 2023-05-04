from django.urls import path

import web.views as webviews

urlpatterns = [

    path('', webviews.loginhomepage, name='loginpage'),
    path('logout', webviews.logoutView, name='logout'),

    # AGENT
    path('agent/home', webviews.agenthomepage, name='agenthomepageminusid'),
    path('agent/home/<str:schoolid>/', webviews.agenthomepage, name='agenthomepage'),

    path('students', webviews.studentshomepage, name='studentshomepage'),
    path('students/add', webviews.addStudent, name='addStudent'),
    path('students/import', webviews.importStudent, name='importStudent'),
    path('students/edit/<str:studentid>', webviews.editStudent, name='editstudent'),
    path('students/delete/<str:studentid>', webviews.deletestudent, name='deletestudent'),
    path('students/activate/<str:studentid>', webviews.activateStudent, name='activateStudent'),

    path('parents', webviews.parentshomepage, name='parentshomepage'),
    path('parents/add', webviews.addparent, name='addparent'),
    path('parents/delete/<str:parentid>', webviews.deleteparent, name='deleteparent'),
    path('parents/edit/<str:parentid>', webviews.editparent, name='editparent'),
    path('parents/import', webviews.importParent, name='importParent'),

    path('transactions', webviews.transactionshomepage, name='transactions'),



    # ADMIN
    path('admin/home', webviews.adminhomepage, name='adminhomepage'),
    path('schools', webviews.adminschoolpage, name='adminschoolpage'),

    path('schools/add', webviews.addschool, name='addschool'),
    path('schools/edit/<str:schoolid>', webviews.editschool, name='editschool'),
    path('schools/delete/<str:schoolid>', webviews.deleteschool, name='deleteschool'),
    path('schools/view/<str:schoolid>', webviews.viewschool, name='viewschool'),

    path('devices', webviews.admindevicepage, name='admindevicepage'),
    path('devices/edit/<str:mobileid>', webviews.editdevice, name='editdevice'),

    path('tokens', webviews.admintokenspage, name='admintokenspage'),

    path('tokens/addtoken', webviews.addtoken, name='addtoken'),
    path('tokens/delete/<str:tokenid>', webviews.deletetoken, name='deletetoken'),
    path('tokens/list/<str:studentid>', webviews.tokenlist, name='tokenlist'),
    path('tokens/purchase/<str:studentid>/<str:amount>/', webviews.tokenbuy, name='tokenpurchase'),

    path('agents', webviews.adminagentspage, name='adminagentspage'),
    path('agents/add', webviews.addagent, name='addagent'),
    path('agents/edit/<str:agentid>', webviews.editagent, name='editagent'),
    path('agents/delete/<str:agentid>', webviews.deleteagent, name='deleteagent'),

    path('settings', webviews.adminsettingshomepage, name='adminsettingshomepage'),

]

