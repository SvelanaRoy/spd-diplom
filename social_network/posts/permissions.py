from rest_framework import permissions

class IsOwnerOrReadOnlyPost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return request.method in permissions.SAFE_METHODS
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
           return True
        
        return obj.user == request.user
    
class IsAuthenticatedOrReadOnlyComment(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return request.method in permissions.SAFE_METHODS
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_authenticated:
            return True
        
class IsAuthenticatedOrReadOnlyLike(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return request.method in permissions.SAFE_METHODS
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_authenticated:
            return True         