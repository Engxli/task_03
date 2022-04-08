from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list":[ 
            {"res1":"food_type1"},
            {"res2":"food_type2"},
            {"res3":"food_type3"}
         ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object":{"res1":"food_type1"}
    }
    return render(request, 'detail.html', context)
