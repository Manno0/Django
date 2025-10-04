import datetime

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

    


def home(request):
    return HttpResponse("Welcome to the Home Page!")

def not_found(request):
    return HttpResponse("Not found")

def current_datetime(request):
    now = datetime.datetime.now().strftime("%A, %d %B %Y, %H:%M:%S")
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Current Date & Time</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #6dd5ed, #2193b0);
                color: #fff;
                text-align: center;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
            }}
            .card {{
                background: rgba(0, 0, 0, 0.3);
                padding: 30px 50px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }}
            h1 {{
                font-size: 2.2rem;
                margin: 0;
            }}
            p {{
                font-size: 1.2rem;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>⏰ Current Date & Time</h1>
            <p>{now}</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")

class NotFoundView(View):
    def get(self, request):
        return HttpResponse("404 Not Found")