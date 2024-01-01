from django.contrib import admin

from .models import (
    Skater,
    Track,
    Race,
    Distance,
    RaceResult,
)


admin.site.register(Skater)
admin.site.register(Track)
admin.site.register(Race)
admin.site.register(Distance)
admin.site.register(RaceResult)
