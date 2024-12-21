import axios from "axios";
// Local
import { API_HOST } from "@/app/constants";

export async function fetchNearbyFoodTrucks(
  latitude: number,
  longitude: number,
  radius: number = 5
) {
  const apiResponse = await axios.get(
    `${API_HOST}/search/?lat=${latitude}&lng=${longitude}&radius=${radius}`
  );
  const foodTruckList = apiResponse.data;
  return foodTruckList["data"];
}
