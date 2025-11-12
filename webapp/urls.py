from django.urls import path
from webapp import views

urlpatterns=[
    path('home_page/',views.home_page,name="home_page"),
    path('all_products/',views.all_products,name="all_products"),
    path('all_materials/',views.all_materials,name="all_materials"),
    path('about_us/',views.about_us,name="about_us"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('cart_page/',views.cart_page,name="cart_page"),
    path('filtered_page/<model>',views.filtered_page,name="filtered_page"),
    path('material_filter_page/<mate>',views.material_filter_page,name="material_filter_page"),
    path('single_case/<case_name>',views.single_case,name="single_case"),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('log_in/',views.log_in,name="log_in"),
    path('add_user/',views.add_user,name="add_user"),
    path('user_login_fn/',views.user_login_fn,name="user_login_fn"),
    path('log_out/',views.log_out,name="log_out"),
    path('save_message/',views.save_message,name="save_message"),


]