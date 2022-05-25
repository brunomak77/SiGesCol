from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class UserComplete(models.Model):
    Choices_sexo = (('F', 'Feminino'), ('M', 'Masculino'), ('+', 'LGBTQIA+'), ('N', 'Nenhuma das opções'))
    Choices_cargo = (('1','Designer'), ('2','Redator'), ('3','Analista de Dados'), ('3', 'Gerente de Comunidade'),
                     ('4','Planner'), ('5','Arte Finalista'), ('6','Designer 3D'), ('7','Atendimento'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=11, blank=False, null=False)
    dob = models.DateTimeField(verbose_name='data de nascimento', blank=False, null=True)
    phone = models.CharField('telefone', max_length=11, blank=False, null=False)
    address = models.CharField('endereço', max_length=100, blank=False, null=False, default='')
    cargo = models.CharField('cargo', max_length=30, choices=Choices_cargo, null=False, blank=False, default='1')
    sexo = models.CharField('sexo', max_length=1, choices=Choices_sexo, null=False, blank=False, default='N')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def save(self, *args, **kwargs):
        super(UserComplete, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Dados Complementares'
        verbose_name = 'Dado Complementar'