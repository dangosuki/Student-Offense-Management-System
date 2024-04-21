from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('homepage/', views.homePage, name='homepage'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('password/', auth_views.PasswordChangeView.as_view()),

    #anthony
    path('homepage/anthony/', views.anthony, name='anthony'),

    path('anthonyprofile/<str:pk_test>/', views.anthonyprofile, name='anthonyprofile'),

    path('anthonycreate_offense/<str:pk>/', views.anthonycreateOffense, name="anthonycreate_offense"),

    path('anthonyupdate_offense/<str:pk>/', views.anthonyupdateOffense, name='anthonyupdate_offense'),

    path('anthonydelete_offense/<str:pk>/', views.anthonydeleteOffense, name="anthonydelete_offense"),

    #charles
    path('homepage/charles/', views.charles, name='charles'),

    path('charlesprofile/<str:pk_test>/', views.charlesprofile, name='charlesprofile'),

    path('charlescreate_offense/<str:pk>/', views.charlescreateOffense, name="charlescreate_offense"),

    path('charlesupdate_offense/<str:pk>/', views.charlesupdateOffense, name='charlesupdate_offense'),

    path('charlesdelete_offense/<str:pk>/', views.charlesdeleteOffense, name="charlesdelete_offense"),

    #berchman
    path('homepage/berchman/', views.berchman, name='berchman'),

    path('berchmanprofile/<str:pk_test>/', views.berchmanprofile, name='berchmanprofile'),

    path('berchmancreate_offense/<str:pk>/', views.berchmancreateOffense, name="berchmancreate_offense"),

    path('berchmanupdate_offense/<str:pk>/', views.berchmanupdateOffense, name='berchmanupdate_offense'),

    path('berchmandelete_offense/<str:pk>/', views.berchmandeleteOffense, name="berchmandelete_offense"),

    #bosco
    path('homepage/bosco/', views.bosco, name='bosco'),

    path('boscoprofile/<str:pk_test>/', views.boscoprofile, name='boscoprofile'),

    path('boscocreate_offense/<str:pk>/', views.boscocreateOffense, name="boscocreate_offense"),

    path('boscoupdate_offense/<str:pk>/', views.boscoupdateOffense, name='boscoupdate_offense'),

    path('boscodelete_offense/<str:pk>/', views.boscodeleteOffense, name="boscodelete_offense"),

    #joseph
    path('homepage/joseph/', views.joseph, name='joseph'),

    path('josephprofile/<str:pk_test>/', views.josephprofile, name='josephprofile'),

    path('josephcreate_offense/<str:pk>/', views.josephcreateOffense, name="josephcreate_offense"),

    path('josephupdate_offense/<str:pk>/', views.josephupdateOffense, name='josephupdate_offense'),

    path('josephdelete_offense/<str:pk>/', views.josephdeleteOffense, name="josephdelete_offense"),
    
    #martin
    path('homepage/martin/', views.martin, name='martin'),

    path('martinprofile/<str:pk_test>/', views.martinprofile, name='martinprofile'),

    path('martincreate_offense/<str:pk>/', views.martincreateOffense, name="martincreate_offense"),

    path('martinupdate_offense/<str:pk>/', views.martinupdateOffense, name='martinupdate_offense'),

    path('martindelete_offense/<str:pk>/', views.martindeleteOffense, name="martindelete_offense"),

    #paul
    path('homepage/paul/', views.paul, name='paul'),

    path('paulprofile/<str:pk_test>/', views.paulprofile, name='paulprofile'),

    path('paulcreate_offense/<str:pk>/', views.paulcreateOffense, name="paulcreate_offense"),

    path('paulupdate_offense/<str:pk>/', views.paulupdateOffense, name='paulupdate_offense'),

    path('pauldelete_offense/<str:pk>/', views.pauldeleteOffense, name="pauldelete_offense"),

    #anne
    path('homepage/anne/', views.anne, name='anne'),

    path('anneprofile/<str:pk_test>/', views.anneprofile, name='anneprofile'),

    path('annecreate_offense/<str:pk>/', views.annecreateOffense, name="annecreate_offense"),

    path('anneupdate_offense/<str:pk>/', views.anneupdateOffense, name='anneupdate_offense'),

    path('annedelete_offense/<str:pk>/', views.annedeleteOffense, name="annedelete_offense"),

    #faustina
    path('homepage/faustina/', views.faustina, name='faustina'),

    path('faustinaprofile/<str:pk_test>/', views.faustinaprofile, name='faustinaprofile'),

    path('faustinacreate_offense/<str:pk>/', views.faustinacreateOffense, name="faustinacreate_offense"),

    path('faustinaupdate_offense/<str:pk>/', views.faustinaupdateOffense, name='faustinaupdate_offense'),

    path('faustinadelete_offense/<str:pk>/', views.faustinadeleteOffense, name="faustinadelete_offense"),

    #mary
    path('homepage/mary/', views.mary, name='mary'),

    path('maryprofile/<str:pk_test>/', views.maryprofile, name='maryprofile'),

    path('marycreate_offense/<str:pk>/', views.marycreateOffense, name="marycreate_offense"),

    path('maryupdate_offense/<str:pk>/', views.maryupdateOffense, name='maryupdate_offense'),

    path('marydelete_offense/<str:pk>/', views.marydeleteOffense, name="marydelete_offense"),

    #rita
    path('homepage/rita/', views.rita, name='rita'),

    path('ritaprofile/<str:pk_test>/', views.ritaprofile, name='ritaprofile'),

    path('ritacreate_offense/<str:pk>/', views.ritacreateOffense, name="ritacreate_offense"),

    path('ritaupdate_offense/<str:pk>/', views.ritaupdateOffense, name='ritaupdate_offense'),

    path('ritadelete_offense/<str:pk>/', views.ritadeleteOffense, name="ritadelete_offense"),

    #rose
    path('homepage/rose/', views.rose, name='rose'),

    path('roseprofile/<str:pk_test>/', views.roseprofile, name='roseprofile'),

    path('rosecreate_offense/<str:pk>/', views.rosecreateOffense, name="rosecreate_offense"),

    path('roseupdate_offense/<str:pk>/', views.roseupdateOffense, name='roseupdate_offense'),

    path('rosedelete_offense/<str:pk>/', views.rosedeleteOffense, name="rosedelete_offense"),


    #teresa
    path('', views.teresa, name='teresa'),
    path('homepage/teresa/', views.teresa, name='teresa'),

    path('teresaprofile/<str:pk_test>/', views.teresaprofile, name='teresaprofile'),

    path('teresacreate_offense/<str:pk>/', views.teresacreateOffense, name="teresacreate_offense"),

    path('teresaupdate_offense/<str:pk>/', views.teresaupdateOffense, name='teresaupdate_offense'),

    path('teresadelete_offense/<str:pk>/', views.teresadeleteOffense, name="teresadelete_offense"),



    #path('', views.home, name='home'),
    #path('homepage/home/', views.home, name='home'),

    path('products/', views.products, name='products'),
    #path('customer/<str:pk_test>/', views.customer, name='customer'),

    #path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    #path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    #path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),



    






]