from django.shortcuts import render

from programs.services import get_programs

MAIN_OBJECTIVE = (
    "HAB Beacon of Hope Foundation is focused on promoting holistic health, social welfare, and inclusive community development by providing education, care, and support to vulnerable groups including women, youth, children, the elderly, and underserved populations."
)

CORE_VALUES = [
    "Compassion",
    "Integrity",
    "Inclusiveness",
    "Accountability",
    "Respect for Human Dignity",
    "Service to Humanity",
    "Empowerment",
    "Transparency",
]

WHO_WE_SERVE = [
    "Women and adolescent mothers",
    "Children and orphans",
    "Youth and school dropouts",
    "Persons with disabilities",
    "The elderly",
    "Underserved communities",
]

KEY_PROGRAMMES = [
    "Women's Health and Wellness",
    "Community Health Screening and Education",
    "Adolescent Mothers Support and Reintegration",
    "Prison Outreach and Rehabilitation",
    "Orphans Care and Support Services",
    "Elderly Care and Wellness Programs",
    "Social Support and Empowerment for Underprivileged Groups",
]

IMPACT_HIGHLIGHTS = [
    {
        "title": "Breast cancer awareness and screening",
        "description": (
            "On 19 October 2025, the foundation held a major outreach at Holy Spirit Catholic "
            "Church, Sunyani, screening 30 women and referring 7 for further medical care."
        ),
    },
    {
        "title": "Adolescent mothers back to school",
        "description": (
            "From March to July 2025, vulnerable adolescent mothers across the Bono Region "
            "received reintegration support to return to school and rebuild confidence."
        ),
    },
    {
        "title": "Prison outreach and health education",
        "description": (
            "On 17 October 2025, breast cancer education and free breast examinations reached "
            "female inmates and staff at Sunyani Central Prison."
        ),
    },
    {
        "title": "Orphanage care and health support",
        "description": (
            "Between December 2024 and January 2025, the foundation supported four orphanages "
            "in Sunyani with hygiene education, sanitary pads, and health screenings."
        ),
    },
    {
        "title": "Elderly home visits and wellness support",
        "description": (
            "Through continuous home visits in Sunyani and Fiapre during 2024 and 2025, "
            "elderly adults received health education, emotional support, and wellness checks."
        ),
    },
]

FUTURE_PRIORITIES = [
    {
        "title": "Expand health screening and education",
        "description": (
            "Organize quarterly breast cancer, hypertension, diabetes, and wellness screenings "
            "while strengthening referrals through hospitals and clinics."
        ),
    },
    {
        "title": "Build a formal support pathway for adolescent mothers",
        "description": (
            "Establish mentorship, counselling, educational support, and vocational training "
            "for adolescent mothers returning to school and work."
        ),
    },
    {
        "title": "Scale prison rehabilitation and reintegration outreach",
        "description": (
            "Introduce literacy support, skills training, counselling, and preparation for "
            "life after release."
        ),
    },
    {
        "title": "Strengthen orphanage and child development programmes",
        "description": (
            "Provide regular medical screening, hygiene packs, educational materials, and "
            "psychosocial support for children and caregivers."
        ),
    },
    {
        "title": "Grow elderly wellness and homecare services",
        "description": (
            "Train volunteers in companionship and homecare while building a mobile wellness "
            "team for regular visits and emergency assessments."
        ),
    },
    {
        "title": "Expand empowerment, jobs, and sustainability initiatives",
        "description": (
            "Launch vocational training, internships, micro-loans, and social enterprise ideas "
            "to strengthen long-term self-reliance."
        ),
    },
]

FOUNDER_STORY = [
    (
        "Esther Kwahene Nsiah, founder of HAB Beacon of Hope Foundation, has always had a strong "
        "passion for helping people through health and social outreach both at work and in her community."
    ),
    (
        "Over the years, she supported vulnerable children, youth, widows, single mothers, school "
        "dropouts, persons with disabilities, the elderly, and people struggling with addiction. "
        "She learned that meaningful service does not depend on having much, but on having a willing and caring heart."
    ),
    (
        "A turning point came in April 2024 during a Bible study session when friends and leaders "
        "encouraged her to formalize her good works. After prayer and with the full support of her husband, "
        "she took the bold step of establishing the foundation."
    ),
    (
        "Today, Esther leads the foundation with a commitment to restore dignity, expand opportunity, "
        "and build stronger, self-reliant communities through transparency, accountability, and sustainable development."
    ),
]


def home(request):
    featured_programs = get_programs(ordering="-created_at", limit=3)
    context = {
        "featured_programs": featured_programs,
        "impact_highlights": IMPACT_HIGHLIGHTS[:3],
        "main_objective": MAIN_OBJECTIVE,
        "who_we_serve": WHO_WE_SERVE,
    }
    return render(request, "core/home.html", context)


def about(request):
    context = {
        "core_values": CORE_VALUES,
        "main_objective": MAIN_OBJECTIVE,
        "founder_story": FOUNDER_STORY,
        "key_programmes": KEY_PROGRAMMES,
    }
    return render(request, "core/about.html", context)


def impact(request):
    context = {
        "impact_highlights": IMPACT_HIGHLIGHTS,
        "future_priorities": FUTURE_PRIORITIES,
    }
    return render(request, "core/impact.html", context)


def contact(request):
    return render(request, "core/contact.html")
