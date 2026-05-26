from django.shortcuts import render, redirect

def home(request):
    """
    Render the public home page or redirect authenticated users.

    Unauthenticated users are shown the home page. Authenticated users
    are redirected directly to their profile page.

    Parameters:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: A redirect to the profile page for authenticated users,
        or the rendered home page for unauthenticated users.
    """

    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'core/home.html')


def handler404(request, exception):
    """
    Render the custom 404 error page.

    Called automatically by Django when a requested resource cannot be found.

    Parameters:
        request (HttpRequest): The incoming HTTP request.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: The rendered 404 error page with a 404 status code.
    """
    return render(request, '404.html', status=404)


def handler500(request):
    """
    Render the custom 500 error page.

    Called automatically by Django when an unhandled server error occurs.

    Parameters:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered 500 error page with a 500 status code.
    """
    return render(request, '500.html', status=500)