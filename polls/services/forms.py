"""
# view decorators

The decorators in django.views.decorators.http can be used to restrict access to views based on the request
method. These decorators will return a django.http.HttpResponseNotAllowed if the conditions are not
met.

"""

from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe


@require_http_methods(["GET", "POST"])
def view_decorators(request):
    # only accept methods GET OR POST
    pass


@require_GET
def get_only(request):
    pass


@require_POST
def post_only(request):
    pass


@require_safe
def safe_view(request):
    """
    require_safe()
Decorator to require that a view only accepts the GET and HEAD methods. These methods are commonly
considered “safe” because they should not have the significance of taking an action other than retrieving the
requested resource.
    :param request:
    :return:
    """
    pass


# File uploads

from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def handle_uploaded_file(f):
    with open('', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
