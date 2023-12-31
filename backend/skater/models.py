from django.db import models


COUNTRIES = (
    ('NL', 'Netherlands'),
)

GENDERS = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Skater(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    birthday = models.DateField()

    def __str__(self):
        return f'<Skater {self.first_name} {self.last_name}>'


class Track(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'<Track {self.name} {self.city} {self.country}>'


class Competition(models.Model):
    name = models.CharField(max_length=50)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f'<Competition {self.name}>'


class Race(models.Model):
    name = models.CharField(max_length=50)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'<Race {self.name} {self.track} {self.date}>'


class Distance(models.Model):
    distance = models.IntegerField()

    def __str__(self):
        return f'<Distance {self.distance}>'


class RaceResult(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    skater = models.ForeignKey(Skater, on_delete=models.CASCADE)
    distance = models.ForeignKey(Distance, on_delete=models.CASCADE)
    time = models.FloatField()
    result = models.IntegerField()
    source = models.CharField(max_length=50)
    link = models.CharField(max_length=200)

    def __str__(self):
        return f'<RaceResult {self.skater.first_name} {self.skater.last_name} {self.race.name} {self.distance.distance} {self.result}>'
