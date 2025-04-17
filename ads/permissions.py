from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only allow owners of an Ad to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsReceiverForStatusChange(permissions.BasePermission):
    """
    Only the ad_receiver on an ExchangeProposal can change its .status.
    """
    def has_object_permission(self, request, view, obj):
        # Any user can list or create; only PATCH/PUT on an existing object
        # must come from obj.ad_receiver.user
        if request.method in ('PATCH', 'PUT'):
            return obj.ad_receiver.user == request.user
        return True
