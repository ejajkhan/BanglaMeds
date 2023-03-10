from django.urls import path
from . import views

urlpatterns = [
     path("",views.home,name="ShopeHome"),
     path("home",views.home,name="ShopeHome"),
     path("about",views.about,name="AboutUs"),
     path("contact",views.contact,name="ContactUs"),
     path("search",views.search,name="Search"),
     path("addcart",views.addcart,name='Add Cart'),
     path("medicineView",views.medicineView,name='medicineView'),
     path("error",views.error,name='Error'),
     path("confirmBuying",views.confirmBuying,name='confirmBuying'),

     path("typeView",views.typeView,name='typeView'),
     path("diseaseView",views.diseaseView,name='diseaseView'),

]
