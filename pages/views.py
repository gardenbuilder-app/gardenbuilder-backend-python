from django.http import HttpResponse


def homePageView(request):
    html = """
        <html>
            <body>
                <h1>Gardenbuilder Backend</h1>
                <h3>API for the Guardenbuilder application</h3>
                <p>You probably want to connect to <a href="https://gardenbuilder-backend.uc.r.appspot.com/graphql">https://gardenbuilder-backend.uc.r.appspot.com/graphql</a></p>
            </body>
        </html>
    """

    return HttpResponse(html)
