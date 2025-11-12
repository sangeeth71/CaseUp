from django.urls import path
from capp import views
urlpatterns=[
    path('dashboard/',views.dashboard,name="dashboard"),
    # ================================================
    path('add_category/',views.add_category,name="add_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:cat_id>',views.edit_category,name="edit_category"),
    path('save_cat_edit/<int:cat_id>',views.save_cat_edit,name="save_cat_edit"),
    path('delete_category/<int:cat_id>',views.delete_category,name="delete_category"),
    # ================================================
    path('add_case/',views.add_case,name="add_case"),
    path('save_case/',views.save_case,name="save_case"),
    path('display_cases/',views.display_cases,name="display_cases"),
    path('edit_cases/<int:case_id>',views.edit_cases,name="edit_cases"),
    path('save_case_edit/<int:case_id>',views.save_case_edit,name="save_case_edit"),
    path('delete_cases/<int:case_id>',views.delete_cases,name="delete_cases"),
#
    path('admin_login/', views.admin_login, name="admin_login"),
    path('login_fn/', views.login_fn, name="login_fn"),
    path('logout_fn/', views.logout_fn, name="logout_fn"),
    path('display_messages/', views.display_messages, name="display_messages"),
    path('del_message/<int:m_id>', views.del_message, name="del_message"),

]