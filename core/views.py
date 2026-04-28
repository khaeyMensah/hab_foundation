from django.shortcuts import render

from programs.services import get_programs

CORE_VALUES = [
    "Compassion in action",
    "Integrity and accountability",
    "Community-centered service",
    "Dignity for every life",
]

IMPACT_HIGHLIGHTS = [
    {
        "title": "Education support",
        "description": "Helping children and families access learning opportunities and school essentials.",
    },
    {
        "title": "Community outreach",
        "description": "Providing practical care through local support drives and compassionate engagement.",
    },
    {
        "title": "Hope restoration",
        "description": "Creating safe spaces where vulnerable people can find encouragement and direction.",
    },
    {
        "title": "Volunteer partnerships",
        "description": "Mobilizing people who want to serve and make a measurable difference together.",
    },
]


def home(request):
    featured_programs = get_programs(ordering="-created_at", limit=3)
    context = {
        "featured_programs": featured_programs,
        "impact_highlights": IMPACT_HIGHLIGHTS[:3],
    }
    return render(request, "core/home.html", context)


def about(request):
    context = {"core_values": CORE_VALUES}
    return render(request, "core/about.html", context)


def impact(request):
    context = {"impact_highlights": IMPACT_HIGHLIGHTS}
    return render(request, "core/impact.html", context)


def contact(request):
    return render(request, "core/contact.html")
