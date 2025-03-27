from django.shortcuts import render, redirect
from .models import featured_guide_info, featured_guide_content, guides_info, CategoryEnum, LabelEnum, users, guide_content


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


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    if username in users and users[username]["password"] == password:
        request.session["username"] = username
        request.session["role"] = users[username]["role"]

    return redirect('homelabs:home')


def logout(request):
    del request.session["username"]
    del request.session["role"]
    return redirect('homelabs:home')


def profile(request):
    # Eventually will be a sql query
    if request.session.get("username"):
        # All Guides
        if request.session["role"] == "admin":
            users_guides = guides_info
        else:
            users_guides = list(filter(lambda guide: guide.author == request.session["username"], guides_info))
        return render(request, "homelabs/profile.html", {"guides": users_guides})
    else:
        return redirect("homelabs:home")
