from django.urls import re_path
from catalog import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user-all-crud", views.UserViewset)
router.register(r"blog-all-crud", views.BlogViewset)
router.register(r"like-all-crud", views.LikeViewset)

urlpatterns = (
    [
        re_path(r"get-number-like/$", views.NumberOfLikeAPIView.as_view()),
        re_path(r"blog-with-like/$", views.BlogwithLikeAPIView.as_view()),
        re_path(r"userget/$", views.Userpermission.as_view()),
        re_path(r"create-group/$", views.Creategroup.as_view()),
        re_path(r"permission/$", views.AssigenPermission.as_view()),
        re_path(r"Html-pdf/$", views.HtmlPdf.as_view()),
        re_path(r"Url-pdf/$", views.UrlPdf.as_view()),
        re_path(r"html-file-pdf/$", views.HtmlfilePdf.as_view()),
        re_path(r"dynamic-html-from/$", views.DynamicHtml.as_view()),
        re_path(r"fill-html-from/$", views.FillHtmlfile.as_view()),
    ]
) + router.urls
