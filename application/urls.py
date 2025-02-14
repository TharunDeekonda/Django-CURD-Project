from django.urls import path
from . import views
urlpatterns = [
    path('',views.add_form,name='Home'),
    path('update/<int:pk>',views.Update_Form.as_view(),name='Update'),
    path('delete/<int:pk>',views.delete_form,name='Delete')
]
