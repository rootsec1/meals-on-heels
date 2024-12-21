from django.test import TestCase
from core.models import FoodTruckModel
from core.service.food_truck_service import calculate_distance, search_nearby_food_trucks


class TestFoodTruckUtils(TestCase):
    def setUp(self):
        """
        Set up test data for FoodTruckModel.
        """
        # Create food trucks with test data
        FoodTruckModel.objects.create(
            location_id=1,
            applicant="Truck 1",
            facility_type="Push Cart",
            cnn=123456,
            location_description="San Francisco",
            address="123 Market Street",
            blocklot="0001-0001",
            block="0001",
            lot="0001",
            permit="23MFF-00001",
            status="APPROVED",
            food_items="Burgers, Fries",
            x=6000000.0,
            y=2100000.0,
            latitude=37.7749,  # San Francisco
            longitude=-122.4194,
            schedule_url="http://example.com/schedule1",
            days_hours="Mon-Sun: 10AM - 9PM",
            noi_sent="2023-01-01",
            received=20230101,
            prior_permit=True,
            location="San Francisco",
            fire_prevention_districts=1,
            police_districts=2,
            supervisor_districts=3,
            zip_codes=94103,
            neighborhoods_old=5,
        )
        FoodTruckModel.objects.create(
            location_id=2,
            applicant="Truck 2",
            facility_type="Truck",
            cnn=654321,
            location_description="Downtown SF",
            address="456 Mission Street",
            blocklot="0002-0002",
            block="0002",
            lot="0002",
            permit="23MFF-00002",
            status="APPROVED",
            food_items="Pizza, Pasta",
            x=6000005.0,
            y=2100005.0,
            latitude=37.7849,  # Nearby in San Francisco
            longitude=-122.4094,
            schedule_url="http://example.com/schedule2",
            days_hours="Mon-Fri: 11AM - 8PM",
            noi_sent="2023-02-01",
            received=20230201,
            prior_permit=False,
            location="Downtown SF",
            fire_prevention_districts=1,
            police_districts=3,
            supervisor_districts=3,
            zip_codes=94105,
            neighborhoods_old=10,
        )
        FoodTruckModel.objects.create(
            location_id=3,
            applicant="Truck 3",
            facility_type="Cart",
            cnn=789012,
            location_description="Oakland",
            address="789 Broadway",
            blocklot="0003-0003",
            block="0003",
            lot="0003",
            permit="23MFF-00003",
            status="APPROVED",
            food_items="Tacos, Burritos",
            x=6000010.0,
            y=2100010.0,
            latitude=37.8049,  # Oakland
            longitude=-122.2711,
            schedule_url="http://example.com/schedule3",
            days_hours="Sat-Sun: 9AM - 7PM",
            noi_sent="2023-03-01",
            received=20230301,
            prior_permit=True,
            location="Oakland",
            fire_prevention_districts=2,
            police_districts=5,
            supervisor_districts=1,
            zip_codes=94607,
            neighborhoods_old=15,
        )

    def test_calculate_distance(self):
        """
        Test the calculate_distance function.
        """
        # San Francisco to Oakland
        dist = calculate_distance(37.7749, -122.4194, 37.8049, -122.2711)
        self.assertAlmostEqual(dist, 13.45, places=1)  # Expected ~13.45 km

        # Same location
        dist = calculate_distance(37.7749, -122.4194, 37.7749, -122.4194)
        self.assertEqual(dist, 0.0)

    def test_search_nearby_food_trucks_within_radius(self):
        """
        Test food truck search within a specified radius.
        """
        # Centered in San Francisco, 5 km radius
        results = search_nearby_food_trucks(37.7749, -122.4194, 5)

        # Only "Truck 1" and "Truck 2" should be within 5 km
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["applicant"], "Truck 1")
        self.assertEqual(results[1]["applicant"], "Truck 2")

        # Check the distance field
        self.assertAlmostEqual(
            results[0]["distance"], 0.0, places=1)  # Exact location
        self.assertAlmostEqual(
            results[1]["distance"], 1.4, places=1)  # ~1.4 km away

    def test_search_nearby_food_trucks_out_of_radius(self):
        """
        Test food truck search where no trucks are within the radius.
        """
        # Centered in San Francisco, 1 km radius
        results = search_nearby_food_trucks(35.996948, -78.899017, 5) # No food trucks in DB for Durham, NC

        # No food trucks should be within 1 km
        self.assertEqual(len(results), 0)

    def test_search_nearby_food_trucks_sorted_by_distance(self):
        """
        Test that the food trucks are returned sorted by distance.
        """
        # Centered in San Francisco, 15 km radius
        results = search_nearby_food_trucks(37.7749, -122.4194, 15)

        # All three trucks should be returned, sorted by distance
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0]["applicant"], "Truck 1")  # Closest
        self.assertEqual(results[1]["applicant"], "Truck 2")
        self.assertEqual(results[2]["applicant"], "Truck 3")  # Farthest
        self.assertLess(results[0]["distance"], results[1]["distance"])
        self.assertLess(results[1]["distance"], results[2]["distance"])
