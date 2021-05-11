from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Typ(models.Model):
    oznaceni_typu = models.CharField(max_length=50, unique=True, verbose_name="Označení typu desky",
                                      help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    TYP = (
        ('vintage', 'Vintage'),
        ('newschool', 'Newschool'),
        ('pop', 'Pop'),
        ('underground', 'Underground'),
        ('rap', 'Rap'),
    )
    oblast = models.CharField(max_length=20, choices=TYP, blank=True, default='vintage', verbose_name="typ desky", help_text='Vyberte typ desky')

    class Meta:
        ordering = ["oznaceni_typu"]
        verbose_name = 'Typ desky'
        verbose_name_plural = 'Typ desky'

    def __str__(self):
        return f"{self.oznaceni_typu}, {self.oblast}"


class Deska(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název desky", help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis desky")
    cena = models.IntegerField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadejte nezáporné desetinné číslo", verbose_name="Cena")
    HODNOCENI = (
        (5, 'kvalitni'),
        (4, 'dobre'),
        (3, 'prumerne'),
        (2, 'nekvalitni'),
        (1, 'neoblibene'),

    )
    hodnoceni = models.IntegerField(choices=HODNOCENI, blank=True, default=3, verbose_name="hodnoceni desky", help_text='Vyberte hodnoceni')
    autor = models.IntegerField(validators=[MinValueValidator(0.0)], null=True, help_text="Zadej nazev autora", verbose_name="autor")
    cover = models.ImageField(upload_to='zbozi/%Y/%m/%d/', blank=True, null=True, verbose_name="Cover")

    class Meta:
        ordering = ["-cena", "nazev"]
        verbose_name = 'Deska'
        verbose_name_plural = 'Deska'

    def __str__(self):
        return f"{self.nazev}, {self.cena}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
