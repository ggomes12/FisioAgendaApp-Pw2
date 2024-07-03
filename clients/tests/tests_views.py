from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Profissional, Consulta

class MarcarConsultaViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.profissional = Profissional.objects.create(user=self.user, especialidade='Fisioterapia')

    def test_marcar_consulta_view_get(self):
        response = self.client.get(reverse('marcar_consulta', args=[self.profissional.user.username, self.profissional.especialidade]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agendamento_consult.html')
