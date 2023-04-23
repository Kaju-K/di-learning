from django.shortcuts import render

data = {
    "animals": [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        }
    ],
    "families": [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        }
    ]
}

def caninae(request):
    context = data
    return render(request, 'family/caninae.html', context)

def felidae(request):
    context = data
    return render(request, 'family/felidae.html', context)

def dog(request):
    context = data
    return render(request, 'animal/dog.html', context)

def domestic_cat(request):
    context = data
    return render(request, 'animal/domestic_cat.html', context)

def panther(request):
    context = data
    return render(request, 'animal/panther.html', context)
