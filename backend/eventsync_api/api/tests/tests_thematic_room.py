from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.utils import timezone
from datetime import timedelta
from core.models import Event, ThematicRoom, Local, ESUser


class ThematicRoomTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = ESUser.objects.create_user(
            email="testuser@example.com",
            password="testpass123",
            cpf="12345678901",
            name="Test User",
            birth_date="2000-01-01",
            phone="12345678901",
        )
        self.client.force_authenticate(user=self.user)
        # Setup for the Event and Local objects
        self.local = Local.objects.create(
            street_name="Street Test",
            street_number="123",
            city="City Test",
            state="State Test",
            cep="00000-000",
            reference="Reference Test",
            local_name="Local Test",
        )

        self.event = Event.objects.create(
            name="Evento Exemplo",
            start_date=timezone.now().date(),
            end_date=(timezone.now() + timedelta(days=5)).date(),
            max_quantity=100,
            min_quantity=10,
            hours_quantity=20,
            description="Descrição do Evento Exemplo",
            local=self.local,
            status="upcoming",
            event_type="conference",
        )
        self.thematic_room_data = {
            "event": self.event,
            "name": "Sala Temática Exemplo",
            "start_date": timezone.now().date(),
            "end_date": (timezone.now() + timedelta(days=2)).date(),
            "start_time": "10:00",
            "speaker": "John Doe",
            "description": "Descrição da Sala Temática Exemplo",
            "hours_quantity": 20,
            "articles": "Artigo 1, Artigo 2",
            "max_quantity": 50,
            "min_quantity": 5,
            "local": "Local Exemplo",
        }
        self.thematic_room = ThematicRoom.objects.create(**self.thematic_room_data)

    def test_list_thematic_rooms(self):
        url = reverse("thematic_room_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_thematic_room(self):
        # Criação de uma Sala Temática
        url = reverse("thematic_room_list")
        data = {
            "name": "Sala Temática Exemplo",
            "event": self.event.id,
            "start_date": timezone.now().date(),
            "end_date": (timezone.now() + timedelta(days=2)).date(),
            "start_time": "10:00",
            "speaker": "John Doe",
            "description": "Descrição da Sala Temática Exemplo",
            "hours_quantity": 20,
            "articles": "Artigo 1, Artigo 2",
            "max_quantity": 50,
            "min_quantity": 5,
            "local": "Local Exemplo",
        }

        response = self.client.post(url, data, format="json")
        # Assert se a sala temática foi criada corretamente
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ThematicRoom.objects.count(), 2)
        self.assertEqual(ThematicRoom.objects.last().name, "Sala Temática Exemplo")

    def test_retrieve_thematic_room(self):
        """Teste para detalhar uma sala temática"""
        url = reverse("thematic_room_detail", kwargs={"pk": self.thematic_room.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.thematic_room.name)

    def test_update_thematic_room(self):
        """Teste para atualizar todos os campos de uma sala temática"""
        url = reverse("thematic_room_detail", kwargs={"pk": self.thematic_room.pk})
        data = {
            "name": "Sala Temática Atualizada",
            "event": self.event.id,
            "start_date": timezone.now().date(),
            "end_date": (timezone.now() + timedelta(days=4)).date(),
            "start_time": "15:00",
            "speaker": "Jane Doe",
            "description": "Descrição Atualizada da Sala Temática",
            "hours_quantity": 30,
            "articles": "Artigo Atualizado 1, Artigo Atualizado 2",
            "max_quantity": 60,
            "min_quantity": 10,
            "local": "Local Atualizado",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.thematic_room.refresh_from_db()
        self.assertEqual(self.thematic_room.name, "Sala Temática Atualizada")
        self.assertEqual(self.thematic_room.speaker, "Jane Doe")
        self.assertEqual(self.thematic_room.hours_quantity, 30)

    def test_partial_update_thematic_room(self):
        """Teste para atualizar parcialmente uma sala temática"""
        url = reverse("thematic_room_detail", kwargs={"pk": self.thematic_room.pk})
        data = {"name": "Sala Temática Parcialmente Atualizada"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.thematic_room.refresh_from_db()
        self.assertEqual(
            self.thematic_room.name, "Sala Temática Parcialmente Atualizada"
        )

    def test_delete_thematic_room(self):
        """Teste para excluir uma sala temática"""
        url = reverse("thematic_room_detail", kwargs={"pk": self.thematic_room.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ThematicRoom.objects.count(), 0)
