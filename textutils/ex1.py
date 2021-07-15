# Self created file
# exercise 1
from django.http import HttpResponse


def links(request):
    return HttpResponse(
        '''<h1>Navigation bar</h2><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Code 
        with harry</a><br><a href="https://www.youtube.com/">YouTube</a><br><a 
        href="https://www.facebook.com/">Facebook</a><br><a href="https://www.flipkart.com/">Flipkart</a><br><a 
        href="https://www.myntra.com/">Myntra</a>''')

