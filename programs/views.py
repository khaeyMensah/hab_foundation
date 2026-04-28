from django.shortcuts import render

from .services import get_programs


def program_list(request):
    programs = get_programs()
    return render(request, "programs/list.html", {"programs": programs})
