from django.shortcuts import render
import json

# Create your views here.

def read_data(location):
    with open(location, "r") as file:
        data = json.load(file)

    return data

def find_instance(data_list, id):
    for instance in data_list:
        if instance['id'] == id:
            return instance
    return None

def all_people(request):
    data = read_data('data.json')
    sorted_data = sorted(data, key=lambda x: x['age'])
    context = {"people": sorted_data}
    return render(request, 'people.html', context)

def specific_person(request, id):
    data = read_data('data.json')
    instance = find_instance(data, id)
    context = {"people": instance}
    return render(request, 'specific_person.html', context)