import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from service_area.models import ServiceProvider


class ServiceProviderTests(APITestCase):
    """Test for GET, POST, PATCH, DELETE api for ServiceProvider"""

    def setUp(self):
        self.provier_data = {
            "name": "Alex",
            "email": "alex@gmail.com",
            "phone_number": "+919655782265",
            "language": "En",
            "currency": "USD",
        }
        self.provider = ServiceProvider.objects.create(**self.provier_data)

        self.provider_id = self.provider.id
        self.provier_data["id"] = self.provider.id
        self.provier_data["created_at"] = str(self.provider.created_at)
        self.provier_data["updated_at"] = str(self.provider.updated_at)

        self.new_provier_data = {
            "name": "Provider 2",
            "email": "user2@gmail.com",
            "phone_number": "+917611182253",
            "language": "En",
            "currency": "USD",
        }

        self.patch_attribute = "phone_number"
        self.provider_patch_data = {self.patch_attribute: "+919999999999"}

    def test_get_providers_list(self, *args):
        """
        Test to GET the service providers list.
        """
        url = reverse("providers-list")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        api_response = resp.json()
        if (
            api_response
            and "created_at" in api_response[0]
            and "updated_at" in api_response[0]
        ):
            # updating id, created_at and updated_at in the provider data
            self.provier_data["id"] = api_response[0]["id"]
            self.provier_data["created_at"] = api_response[0]["created_at"]
            self.provier_data["updated_at"] = api_response[0]["updated_at"]
        assert [self.provier_data] == api_response

    def test_create_provider(self):
        """
        Test for the POST api on serviceprovider.
        """
        url = reverse("providers-list")
        resp = self.client.post(url, self.new_provier_data, format="json")

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        api_response = resp.json()
        if (
            api_response
            and "created_at" in api_response
            and "updated_at" in api_response
        ):
            # updating id, created_at and updated_at in the provider data
            self.new_provier_data["id"] = api_response["id"]
            self.new_provier_data["created_at"] = api_response["created_at"]
            self.new_provier_data["updated_at"] = api_response["updated_at"]
        self.assertEqual(self.new_provier_data, api_response)

    def test_get_provider_detail(self):
        """ "
        Test for the GET detail api on service provider.
        """
        url = reverse("providers-detail", kwargs={"pk": self.provider_id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        api_response = resp.json()
        if (
            api_response
            and "created_at" in api_response
            and "updated_at" in api_response
        ):
            # updating id, created_at and updated_at in the provider data
            self.provier_data["created_at"] = api_response["created_at"]
            self.provier_data["updated_at"] = api_response["updated_at"]
        self.assertEqual(self.provier_data, api_response)

    def test_update_provider(self):
        """
        Test for the UPDATE api on service provider.
        """
        url = reverse("providers-detail", kwargs={"pk": self.provider_id})
        resp = self.client.patch(
            url,
            data=self.provider_patch_data,
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.provider_patch_data[self.patch_attribute],
            resp.json()[self.patch_attribute],
        )

    def test_delete_provider(self):
        """ "
        Test for the DELETE api on service provider.
        """
        url = reverse("providers-detail", kwargs={"pk": self.provider_id})
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ServiceProvider.objects.filter(id=self.provider_id).exists())
