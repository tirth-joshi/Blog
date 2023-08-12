from rest_framework.permissions import BasePermission
from .models import Blog

class OnlyBlogOwner(BasePermission):
    # Only owner access of Upadte and delete oprations.
    def has_permission(self, request, view):
        user = request.user
        object_id = view.kwargs.get("pk")
        if request.method in ["PUT", "DELETE", "PATCH"]:
            if Blog.objects.filter(user=user.id, id=object_id).exists():
                return True
            else:
                return False
        return True
