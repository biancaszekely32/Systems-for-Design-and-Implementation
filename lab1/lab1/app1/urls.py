from django.urls import path
from .views import EmployeeDetail, EmployeeInfo, EmployeeWithSalaryAtLeastN
from .views import ProductDetail,ProductInfo
from .views import ShoppingCenterDetail,ShoppingCenterInfo

urlpatterns=[
    path("ShoppingCenter/",ShoppingCenterDetail.as_view(),name="ShoppingCenter"),
    path("ShoppingCenter/<int:id>/",ShoppingCenterInfo.as_view()),
    path("Employee/",EmployeeDetail.as_view(),name="Employee"),
    path("Product/",ProductDetail.as_view(),name="Product"),
    path("Employee/<int:id>/",EmployeeInfo.as_view()),
    path("Salary/<int:sal>/",EmployeeWithSalaryAtLeastN.as_view(),name="sal")

]