from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Avaliation(models.Model):

    notas = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),
             (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tee = models.IntegerField('trabalho em equipe', choices=notas, default='0', blank=False, null=False)
    pro = models.IntegerField('proatividade', choices=notas, default='0', blank=False, null=False)
    lid = models.IntegerField('liderança', choices=notas, default='0', blank=False, null=False)
    fle = models.IntegerField('flexibilidade', choices=notas, default='0', blank=False, null=False)
    ini = models.IntegerField('iniciativa', choices=notas, default='0', blank=False, null=False)
    pon = models.IntegerField('pontualidade', choices=notas, default='0', blank=False, null=False)
    com = models.IntegerField('comprometimento', choices=notas, default='0', blank=False, null=False)
    cup = models.IntegerField('cumprir prazos', choices=notas, default='0', blank=False, null=False)
    pst = models.IntegerField('proficiência em softwares e técnicas', choices=notas, default='0',
                              blank=False, null=False)
    err = models.IntegerField('erros', choices=notas, default='0', blank=False, null=False)
    org = models.IntegerField('organização', choices=notas, default='0', blank=False, null=False)
    cpi = models.IntegerField('cumprimento dos processos internos', choices=notas, default='0', blank=False, null=False)
    p_pos = models.TextField('percepções positivas', max_length=200, blank=True, null=False)
    p_neg = models.TextField('percepções negativas', max_length=200, blank=True, null=False)
    date_posted = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(User, self.user).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user-aval-list', kwargs={'username': self.user.username})

    class Meta:
        verbose_name_plural = 'Avaliações'
        verbose_name = 'Avaliação'
