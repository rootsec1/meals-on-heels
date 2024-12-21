"use client";

import {
  Button,
  Card,
  CardBody,
  CardFooter,
  CardHeader,
  CircularProgress,
  Divider,
} from "@nextui-org/react";
import "mapbox-gl/dist/mapbox-gl.css";
import { SnackbarProvider, enqueueSnackbar } from "notistack";
import { useCallback, useEffect, useRef, useState } from "react";
import { AiOutlineSearch } from "react-icons/ai";
import { FaLocationDot } from "react-icons/fa6";
import Map, {
  GeolocateControl,
  MapRef,
  Marker,
  NavigationControl,
  Popup,
} from "react-map-gl";

// Local imports
import {
  DEFAULT_SEARCH_RADIUS,
  LOCATION_CENTER_PALO_ALTO,
  MAPBOX_API_KEY,
} from "@/app/constants";
import { fetchNearbyFoodTrucks } from "@/app/services";
import { Input } from "@nextui-org/react";

interface PopupInfo {
  latitude: number;
  longitude: number;
  title: string;
  description: string;
  address: string;
  distance: number;
}

/**
 * Main component for the search page.
 * Allows users to search for nearby food trucks based on their location.
 */
export default function SearchPage() {
  const mapRef = useRef<MapRef | null>(null);
  const [searchLatitude, setSearchLatitude] = useState<number | null>(null);
  const [searchLongitude, setSearchLongitude] = useState<number | null>(null);
  const [searchRadius, setSearchRadius] = useState<number>(
    DEFAULT_SEARCH_RADIUS
  );

  const [foodTruckList, setFoodTruckList] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [popupInfo, setPopupInfo] = useState<PopupInfo | null>(null);

  /**
   * Displays a notification to the user.
   * @param message - The message to display.
   * @param isError - Whether the message is an error message.
   */
  function alertUser(message: string, isError: boolean) {
    enqueueSnackbar(message, {
      variant: isError ? "error" : "success",
      preventDuplicate: true,
      anchorOrigin: {
        vertical: "bottom",
        horizontal: "right",
      },
      autoHideDuration: 3000,
    });
  }

  /**
   * Fetches nearby food trucks based on the search coordinates and radius.
   */
  const getNearbyFoodTrucks = useCallback(async () => {
    // Validate search latitude and longitude
    if (!searchLatitude || !searchLongitude) {
      alertUser("Please enter a valid latitude and longitude", true);
      return;
    }

    try {
      setIsLoading(true);
      const foodTruckList = await fetchNearbyFoodTrucks(
        searchLatitude,
        searchLongitude,
        searchRadius
      );
      if ((foodTruckList as unknown as unknown[]).length === 0) {
        alertUser("No food trucks found nearby :(", true);
      }
      setFoodTruckList(foodTruckList ?? []);
    } catch (error) {
      console.error("Error fetching nearby food trucks:", error);
      alertUser("Error fetching nearby food trucks", true);
    } finally {
      setIsLoading(false);
    }
  }, [searchLatitude, searchLongitude, searchRadius]);

  useEffect(() => {
    // Set initial geolocation only once if not already set
    if (searchLatitude === null && searchLongitude === null) {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            setSearchLatitude(position.coords.latitude);
            setSearchLongitude(position.coords.longitude);
          },
          (error) => {
            console.error("Error getting geolocation:", error);
            setSearchLongitude(LOCATION_CENTER_PALO_ALTO.longitude);
          }
        );
      } else {
        console.error("Geolocation is not supported by this browser.");
      }
    }
  }, [searchLatitude, searchLongitude]);

  /**
   * Component for the left section of the page.
   * Contains input fields for latitude, longitude, and search radius.
   */
  function LeftSection() {
    return (
      <div className="text-xs">
        {/* Input for coordinates */}
        <div className="mt-4 flex gap-4">
          {/* Input for Latitude */}
          <div className="flex-1">
            <Input
              isClearable
              classNames={{
                label: "text-black/50",
                input: [
                  "bg-transparent",
                  "text-black/90",
                  "placeholder:text-default-700/50",
                ],
                innerWrapper: "bg-transparent",
                inputWrapper: [
                  "shadow-xl",
                  "bg-white",
                  "backdrop-blur-xl",
                  "hover:bg-default-200/70",
                  "!cursor-text",
                ],
              }}
              label="Latitude"
              placeholder="Ex: 37.76"
              radius="lg"
              startContent={
                <AiOutlineSearch className="text-black/50 mb-0.5 dark:text-white/90 text-slate-400 pointer-events-none flex-shrink-0" />
              }
              value={searchLatitude?.toString() || ""}
              onValueChange={(value) => {
                setSearchLatitude(value ? Number(value.trim()) : null);
              }}
            />
          </div>

          {/* Input for Longitude */}
          <div className="flex-1">
            <Input
              isClearable
              classNames={{
                label: "text-black/50",
                input: [
                  "bg-transparent",
                  "text-black/90",
                  "placeholder:text-default-700/50",
                ],
                innerWrapper: "bg-transparent",
                inputWrapper: [
                  "shadow-xl",
                  "bg-white",
                  "backdrop-blur-xl",
                  "hover:bg-default-200/70",
                  "!cursor-text",
                ],
              }}
              label="Longitude"
              placeholder="Ex: -122.41"
              radius="lg"
              startContent={
                <AiOutlineSearch className="text-black/50 mb-0.5 dark:text-white/90 text-slate-400 pointer-events-none flex-shrink-0" />
              }
              value={searchLongitude?.toString() || ""}
              onValueChange={(value) => {
                setSearchLongitude(value ? Number(value.trim()) : null);
              }}
            />
          </div>
        </div>

        {/* Input for search radius */}
        <div className="mt-4">
          <Input
            isClearable
            type="number"
            classNames={{
              label: "text-black/50",
              input: [
                "bg-transparent",
                "text-black/90",
                "placeholder:text-default-700/50",
              ],
              innerWrapper: "bg-transparent",
              inputWrapper: [
                "shadow-xl",
                "bg-white",
                "backdrop-blur-xl",
                "hover:bg-default-200/70",
                "!cursor-text",
              ],
            }}
            min={0.1}
            label="Radius (km)"
            placeholder="Ex: 5"
            radius="sm"
            value={searchRadius.toString()}
            onValueChange={(value) => setSearchRadius(Number(value))}
          />
        </div>

        {/* Button */}
        <Button
          className="w-full mt-8"
          color="secondary"
          variant="shadow"
          startContent={<AiOutlineSearch size={18} />}
          isDisabled={isLoading}
          isLoading={isLoading}
          onPress={getNearbyFoodTrucks}
        >
          Find food trucks nearby
        </Button>

        {/* List of food trucks retrieved from API */}
        {foodTruckList.length > 0 && (
          <div className="mt-4 h-[400px] overflow-hidden">
            <h2 className="text-lg font-bold mb-2">Food Trucks Nearby</h2>
            <div className="overflow-y-auto h-full">
              {foodTruckList.length > 0 ? (
                <div className="space-y-4">
                  {foodTruckList.map((foodTruck) => (
                    <Card
                      key={foodTruck["location_id"]}
                      className="shadow-sm hover:shadow-lg hover:cursor-pointer w-full"
                      isHoverable
                      isPressable
                      onPress={() => {
                        mapRef.current?.flyTo({
                          center: [
                            foodTruck["longitude"],
                            foodTruck["latitude"],
                          ],
                          zoom: 14,
                        });
                        setPopupInfo({
                          latitude: foodTruck["latitude"],
                          longitude: foodTruck["longitude"],
                          title: foodTruck["applicant"],
                          description: foodTruck["food_items"],
                          address: foodTruck["address"],
                          distance: foodTruck["distance"],
                        });
                      }}
                      onMouseLeave={() => setPopupInfo(null)}
                    >
                      {foodTruck["applicant"] && (
                        <CardHeader>
                          <h3 className="font-bold">
                            {foodTruck["applicant"]}
                          </h3>
                        </CardHeader>
                      )}
                      <Divider />
                      {foodTruck["food_items"] && (
                        <CardBody>
                          <p className="text-xs">{foodTruck["food_items"]}</p>
                        </CardBody>
                      )}
                      <Divider />
                      {(foodTruck["address"] || foodTruck["distance"]) && (
                        <CardFooter className="flex justify-between">
                          <p className="text-xs text-gray-500">
                            {foodTruck["address"]}
                          </p>
                          <p className="text-xs text-gray-500">
                            {Number(foodTruck["distance"]).toFixed(2)} km away
                          </p>
                        </CardFooter>
                      )}
                    </Card>
                  ))}
                </div>
              ) : (
                <p className="text-gray-500 p-4">No food trucks found nearby</p>
              )}
            </div>
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="flex h-screen">
      <SnackbarProvider />

      {/* Left section taking 1/3 of the width */}
      <div className="w-1/3 bg-gray-100 p-4">
        <h1 className="text-xl font-bold">meals ● on ● heels</h1>
        {/* Additional content can go here */}
        <LeftSection />
      </div>

      {/* Right section taking 2/3 of the width */}
      <div className="w-2/3">
        {searchLatitude && searchLongitude ? (
          <Map
            ref={mapRef}
            mapboxAccessToken={MAPBOX_API_KEY}
            initialViewState={{
              latitude: searchLatitude,
              longitude: searchLongitude,
              zoom: 13,
            }}
            style={{ width: "100%", height: "100%" }}
            mapStyle="mapbox://styles/mapbox/streets-v12"
          >
            {searchLatitude && searchLongitude && (
              <Marker
                latitude={searchLatitude}
                longitude={searchLongitude}
                anchor="bottom"
              >
                <FaLocationDot color="#03A9F4" size={32} />
              </Marker>
            )}
            {foodTruckList.map((foodTruck) => (
              <Marker
                key={foodTruck["location_id"]}
                latitude={foodTruck["latitude"]}
                longitude={foodTruck["longitude"]}
                anchor="bottom"
              >
                <FaLocationDot
                  color="#FF5722"
                  size={20}
                  onMouseEnter={() =>
                    setPopupInfo({
                      latitude: foodTruck["latitude"],
                      longitude: foodTruck["longitude"],
                      title: foodTruck["applicant"],
                      description: foodTruck["food_items"],
                      address: foodTruck["address"],
                      distance: foodTruck["distance"],
                    })
                  }
                  className="hover:cursor-pointer"
                />
              </Marker>
            ))}

            {popupInfo && (
              <Popup
                latitude={popupInfo.latitude}
                longitude={popupInfo.longitude}
                closeButton
              >
                <div className="p-1 text-xs">
                  <h3 className="font-bold">{popupInfo.title}</h3>
                  <p className="text-gray-500 mb-1">{popupInfo.address}</p>
                  <p>{popupInfo.description}</p>
                  <p className="text-xs text-gray-500 mt-1">
                    {popupInfo.distance.toFixed(2)} km away
                  </p>
                </div>
              </Popup>
            )}

            <GeolocateControl />
            <NavigationControl />
          </Map>
        ) : (
          <div className="h-screen flex items-center justify-center">
            <CircularProgress aria-label="Loading..." color="secondary" />
          </div>
        )}
      </div>
    </div>
  );
}
