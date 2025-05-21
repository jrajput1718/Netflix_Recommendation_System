from django.shortcuts import render
from .recommender_engine import get_recommendations

def index(request):
    recommendations = []
    query = ""
    if request.method == 'POST':
        query = request.POST.get('movie')
        recommendations = get_recommendations(query)
    return render(request, 'index.html', {'recommendations': recommendations, 'query': query})
