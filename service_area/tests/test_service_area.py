import datetime

from django.contrib.gis.geos import Polygon
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from service_area.models import ServiceArea, ServiceProvider


class ServiceAreaTests(APITestCase):
    """Test for GET, POST, PATCH, DELETE api for ServiceArea"""

    def setUp(self):
        self.provier_data = {
            "name": "Alex",
            "email": "alex@gmail.com",
            "phone_number": "+919655782265",
            "language": "En",
            "currency": "USD",
        }
        self.provider = ServiceProvider.objects.create(**self.provier_data)
        self.provider.save()
        self.provider_id = self.provider.id
        self.area_polygon = Polygon(
            (
                (14.575939178466795, 25.32432169073797),
                (14.563064575195312, 25.31718389496166),
                (14.573020935058594, 25.289870184457822),
                (14.599456787109373, 25.295147176413156),
                (14.601001739501951, 25.31501143883031),
                (14.575939178466795, 25.32432169073797),
            )
        )
        self.service_area_data = {
            "name": "Test Area",
            "price": "200.00",
            "service_area": self.area_polygon,
        }

        self.serice_area = ServiceArea.objects.create(
            service_provider=self.provider, **self.service_area_data
        )

        self.serice_area_id = self.serice_area.id
        self.service_area_data["id"] = self.serice_area_id
        self.service_area_data["service_area"] = str(self.serice_area.service_area)
        self.service_area_data["service_provider"] = self.provider_id
        self.service_area_data["provider_name"] = self.provider.name

        self.new_serice_area_data = {
            "service_provider": self.provider_id,
            "name": "Test Area 2",
            "price": "200.00",
            "service_area": str(self.area_polygon),
        }

        self.patch_attribute = "price"
        self.area_patch_data = {self.patch_attribute: "300.00"}

    def test_get_service_area_list(self, *args):
        """
        Test to GET the service area list.
        """
        url = reverse("service-areas-list")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        api_response = resp.json()
        if (
            api_response
            and "created_at" in api_response[0]
            and "updated_at" in api_response[0]
        ):
            # updating id, created_at and updated_at in the provider data
            self.service_area_data["created_at"] = api_response[0]["created_at"]
            self.service_area_data["updated_at"] = api_response[0]["updated_at"]

        for key in api_response[0]:
            assert api_response[0][key] == self.service_area_data[key]

    def test_get_lat_long_area(self, *args):
        """
        Test to GET the service area list for given longitude and latitude.
        """
        url = reverse("service-areas-list")
        resp = self.client.get(url, {"latitude": "15.12321", "longitude": "14.12421"})

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        api_response = resp.json()

        if (
            api_response
            and "created_at" in api_response[0]
            and "updated_at" in api_response[0]
        ):
            # updating id, created_at and updated_at in the provider data
            self.service_area_data["created_at"] = api_response[0]["created_at"]
            self.service_area_data["updated_at"] = api_response[0]["updated_at"]

        for key in api_response[0]:
            assert api_response[0][key] == self.service_area_data[key]

    def test_create_service_area(self):
        """
        Test for the POST api on service-area.
        """
        url = reverse("service-areas-list")
        resp = self.client.post(url, self.new_serice_area_data, format="json")

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        api_response = resp.json()
        if (
            api_response
            and "created_at" in api_response
            and "updated_at" in api_response
        ):
            # updating id, created_at and updated_at in the provider data
            self.new_serice_area_data["id"] = api_response["id"]
            self.new_serice_area_data["created_at"] = api_response["created_at"]
            self.new_serice_area_data["updated_at"] = api_response["updated_at"]
            self.new_serice_area_data["provider_name"] = api_response["provider_name"]
        for key in api_response:
            assert api_response[key] == self.new_serice_area_data[key]

    def test_get_service_area_detail(self):
        """
        Test for the GET detail api on service-area.
        """
        url = reverse("service-areas-detail", kwargs={"pk": self.serice_area_id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        api_response = resp.json()
        if (
            api_response
            and "created_at" in api_response
            and "updated_at" in api_response
        ):
            # updating id, created_at and updated_at in the provider data
            self.service_area_data["created_at"] = api_response["created_at"]
            self.service_area_data["updated_at"] = api_response["updated_at"]
        for key in api_response:
            assert api_response[key] == self.service_area_data[key]

    def test_update_service_area(self):
        """
        Test for the UPDATE api on service-area.
        """
        url = reverse("service-areas-detail", kwargs={"pk": self.serice_area_id})
        resp = self.client.patch(
            url,
            data=self.area_patch_data,
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.area_patch_data[self.patch_attribute],
            resp.json()[self.patch_attribute],
        )

    def test_delete_service_area(self):
        """
        Test for the DELETE api on service-area.
        """
        url = reverse("service-areas-detail", kwargs={"pk": self.serice_area_id})
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ServiceArea.objects.filter(id=self.provider_id).exists())
