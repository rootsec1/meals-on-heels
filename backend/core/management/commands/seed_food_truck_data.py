import csv

from django.core.management.base import BaseCommand
from core.models import FoodTruckModel


DATASET_PATH = "core/assets/seed/food_truck_dataset.csv"


class Command(BaseCommand):
    help = "Seeds food truck data from CSV file"

    def handle(self, *args, **options):
        # Check if FoodTruckModel is empty in DB, if empty seed the data
        if FoodTruckModel.objects.exists():
            print("Food Truck data already seeded.")
            return

        # Open the CSV file in core/assets/seed folder
        with open(DATASET_PATH) as csv_file:
            # Read the CSV file and automatically read the first row as header
            reader = csv.DictReader(csv_file)
            # Loop through each row in the CSV file
            for row in reader:
                try:
                    # Create a FoodTruckModel object with the data from the CSV file
                    food_truck_model = {
                        "location_id": row.get("locationid"),
                        "applicant": row.get("Applicant"),
                        "facility_type": row.get("FacilityType"),
                        "cnn": row.get("cnn"),
                        "location_description": row.get("LocationDescription"),
                        "address": row.get("Address"),
                        "blocklot": row.get("blocklot"),
                        "block": row.get("block"),
                        "lot": row.get("lot"),
                        "permit": row.get("permit"),
                        "status": row.get("Status"),
                        "food_items": row.get("FoodItems"),
                        "x": row.get("X"),
                        "y": row.get("Y"),
                        "latitude": row.get("Latitude"),
                        "longitude": row.get("Longitude"),
                        "schedule_url": row.get("Schedule"),
                        "days_hours": row.get("dayshours"),
                        "noi_sent": row.get("NOISent"),
                        "received": row.get("Received"),
                        # Ensure boolean conversion
                        "prior_permit": bool(int(row.get("PriorPermit", 0))),
                        "location": row.get("Location"),
                        "fire_prevention_districts": row.get("Fire Prevention Districts"),
                        "police_districts": row.get("Police Districts"),
                        "supervisor_districts": row.get("Supervisor Districts"),
                        "zip_codes": row.get("Zip Codes"),
                        "neighborhoods_old": row.get("Neighborhoods (old)"),
                    }

                    FoodTruckModel.objects.update_or_create(
                        location_id=row.get("locationid"),
                        defaults=food_truck_model
                    )
                except:
                    continue

        count_of_food_trucks = FoodTruckModel.objects.count()
        print(f"Successfully seeded {count_of_food_trucks} food trucks.")
