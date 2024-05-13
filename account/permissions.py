from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.ADMIN

class IsManager(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.MANAGER

class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.EMPLOYEE

class IsDeliveryCrew(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.DELIVERY_CREW

class IsCustomer(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.CUSTOMER
