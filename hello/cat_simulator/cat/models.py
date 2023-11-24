from django.db import models
from random import randint


class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = 1
    happiness = models.IntegerField(default=50)
    hunger = models.IntegerField(default=50)
    is_sleeping = models.BooleanField(default=False)

    def mood(self):
        if self.hunger < 0:
            self.hunger = 0
        if self.hunger > 100:
            self.hunger = 100
        if self.happiness < 0:
            self.happiness = 0
        if self.happiness > 100:
            self.happiness = 100

    def feed(self):
        if not self.is_sleeping:
            self.hunger += 15
            self.happiness += 5
            self.happiness -= 30
            self.mood()
        else:
            pass
        self.save()

    def play(self):
        if not self.is_sleeping:
            self.happiness += 15
            self.hunger -= 10
            if randint(1, 3) == 1:
                self.happiness = 0
            self.mood()
        else:
            self.happiness -= 5
            self.is_sleeping = False
        self.save()
        self.mood()

    def sleep(self):
        self.is_sleeping = True
        self.save()

    class Meta:
        app_label = 'cat'