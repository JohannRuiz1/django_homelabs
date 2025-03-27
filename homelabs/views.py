from django.shortcuts import render
from .models import featured_guide_info, featured_guide_content, guides_info, CategoryEnum, LabelEnum, guide_content


# Create your views here.
def home(request):
    # Pull from database
    return render(request, "homelabs/home.html", {"guide_info": featured_guide_info})

def guide_list(request):
    # Pull from database
    return render(request, "homelabs/guides/list.html",
                    {"guides": guides_info,
                            "categories": [(c.name, c.value) for c in CategoryEnum],
                            "labels": [(l.name, l.value) for l in LabelEnum] })

def guide_add(request):
    # Pull from database
    return render(request, "homelabs/guides/add.html",
                {"categories": [(c.name, c.value) for c in CategoryEnum],
                        "labels": [(l.name, l.value) for l in LabelEnum] })

# TODO: ADD EDIT PAGE
# def guide_edit(request):
#     # Pull from database
#     return render(request, "homelabs/guides/add.html")

def guide_view(request, id):
    # Pull from database
    return render(request, "homelabs/guides/view.html", {"guide_info": featured_guide_info, "guide_content": guide_content})


def guide_suggestion(request):
    # Pull from database
    return render(request, "homelabs/guides/suggestion.html", {"guide_info": featured_guide_info, "guide_content": guide_content} )

