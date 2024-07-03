from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profissional, Consulta
from django.urls import reverse

class ProfissionalModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profissional = Profissional.objects.create(user=self.user, especialidade='Fisioterapia')

    def test_profissional_creation(self):
        # Verifica se o profissional foi criado corretamente
        self.assertEqual(self.profissional.user.username, 'testuser')
        self.assertEqual(self.profissional.especialidade, 'Fisioterapia')



        

class ConsultaModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profissional = Profissional.objects.create(user=self.user, especialidade='Fisioterapia')
        self.consulta = Consulta.objects.create(profissional=self.profissional, data='2024-07-01', horario_inicial='08:00:00', horario_final='09:00:00')

    def test_consulta_creation(self):
        # Verifica se a consulta foi criada corretamente
        self.assertEqual(self.consulta.profissional.user.username, 'testuser')
        self.assertEqual(str(self.consulta.data), '2024-07-01')
        self.assertEqual(str(self.consulta.horario_inicial), '08:00:00')
        self.assertEqual(str(self.consulta.horario_final), '09:00:00')


