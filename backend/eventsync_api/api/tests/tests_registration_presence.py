from core.models import ESUser, Event, RegistrationPresence
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class RegistrationPresenceTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a user and authenticate
        self.user = ESUser.objects.create_user(
            email="testuser@example.com",
            password="testpass123",
            cpf="12345678901",
            name="Test User",
            birth_date="2000-01-01",
            phone="12345678901",
        )
        self.client.force_authenticate(user=self.user)

        # Create another user for testing registration
        self.participant = ESUser.objects.create_user(
            email="participant@example.com",
            password="testpass123",
            cpf="12345678902",
            name="Participant",
            birth_date="1995-05-05",
            phone="12345678902",
        )

        # Create an event
        self.event = Event.objects.create(
            name="Test Event",
            start_date="2024-10-10",
            end_date="2024-10-12",
            max_quantity=100,
            min_quantity=10,
            hours_quantity=5,
            description="Test Event Description",
            local=None,
            status="upcoming",
            event_type="conference",
        )

    def test_create_registration_presence(self):
        url = reverse("event_registration_list")
        params = {"event_id": self.event.pk, "user_id": self.participant.pk}
        response = self.client.post(
            f"{url}?event_id={params['event_id']}&user_id={params['user_id']}"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RegistrationPresence.objects.count(), 1)
        self.assertEqual(RegistrationPresence.objects.first().user, self.participant)

    def test_retrieve_registration_presence(self):
        RegistrationPresence.objects.create(user=self.participant, event=self.event)

        url = reverse(
            "event_registration_detail",
            kwargs={"event_id": self.event.pk, "user_id": self.participant.pk},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], self.participant.pk)

    def test_update_registration_presence(self):
        registration = RegistrationPresence.objects.create(
            user=self.participant, event=self.event
        )

        url = reverse(
            "event_registration_detail",
            kwargs={"event_id": self.event.pk, "user_id": self.participant.pk},
        )
        data = {"presence": True}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        registration.refresh_from_db()
        self.assertTrue(registration.presence)

    def test_delete_registration_presence(self):
        registration = RegistrationPresence.objects.create(
            user=self.participant, event=self.event
        )

        url = reverse(
            "event_registration_detail",
            kwargs={"event_id": self.event.pk, "user_id": self.participant.pk},
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(RegistrationPresence.objects.count(), 0)
