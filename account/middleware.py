from django.http import HttpResponseForbidden
from django.urls import reverse


class ApprovalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        admin_url = reverse('admin:index')
        if request.path.startswith(admin_url):
            return self.get_response(request)

        # Check if user is authenticated and if they are not approved
        if request.user.is_authenticated:
            if not getattr(request.user, 'is_approved', False):
                # Deny access to certain URLs if user is not approved
                restricted_urls = ['/employee/']  
                if request.path in restricted_urls:
                    return HttpResponseForbidden("Your account is not approved yet.")

            # Role-based access control for admin and employee views
            if request.path.startswith('/admin/'):
                if not request.user.is_admin :
                    return HttpResponseForbidden("Access restricted. Admins only.")
            elif request.path.startswith('/employee/'):
                if not  request.user.is_employee:
                    return HttpResponseForbidden("Access restricted. Employees only.")
                else:
                    pass

        return self.get_response(request)
