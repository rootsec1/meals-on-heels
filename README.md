# Meals on Heels

Meals on Heels is a simple yet powerful application that helps you find nearby food trucks based on your geolocation. The app allows you to visualize food trucks on an interactive map and provides details such as the name, food items, address, and the distance from your current location.

![Meals on Heels](https://github.com/user-attachments/assets/9afa7eaa-7848-4520-add4-7de502c6b431)

---

## Demo (click to watch on YouTube)

[![Watch Demo here](https://img.youtube.com/vi/U05Zj20NZts/0.jpg)](https://youtu.be/U05Zj20NZts)

Link: https://youtu.be/U05Zj20NZts

---

## Features

- Perform geolocation-based searches for food trucks.
- Interactive map using Mapbox to view and explore food truck locations.
- Search functionality with customizable radius in kilometers.
- Food truck details include name, food items, address, and distance.
- User-friendly interface built with modern tools.

---

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- **Python**: Version `3.9.6`
- **Node.js**: Version `23.5.0`

---

## Built With

### **Backend**
- **Python 3.9.6**
- **Django**: Web framework.
- **Django REST Framework (DRF)**: API development.

### **Frontend**
- **Next.js**: React framework with support for server-side rendering and API routes.
- **TypeScript**: For type safety.
- **NextUI**: Component library for beautiful and responsive designs.
- **Mapbox**: Interactive map layer to display food trucks.

---

## Setup Instructions

Follow these steps to set up and run the app on **Mac** or **Linux**.

### **Clone the Repository**
```bash
git clone https://github.com/rootsec1/meals-on-heels.git
cd meals-on-heels
```

### **Backend Setup**
1. Open a terminal and navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment:
   ```bash
   virtualenv -p python3 env
   ```
   If `virtualenv` is not installed:
   ```bash
   python3 -m pip install virtualenv
   ```
3. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```
4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run database migrations:
   ```bash
   python manage.py migrate
   ```
6. Seed the database with food truck data using the custom management command:
   ```bash
   python manage.py seed_food_truck_data
   ```
7. Start the backend server on all interfaces (port `8000`):
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

Here’s the updated setup instructions for the **Frontend (web-ui)**, including the creation of the `.env` file for environment variables.

---

### **Frontend Setup**

1. Open another terminal and navigate to the `web-ui` directory:
   ```bash
   cd web-ui
   ```

2. Install required packages:
   ```bash
   npm install
   ```

3. Create a new file called `.env` in the `web-ui` directory:
   ```bash
   touch .env
   ```

4. Open the `.env` file in your preferred text editor and add the following line:
   ```env
   NEXT_PUBLIC_MAPBOX_API_KEY=<your-mapbox-token>
   ```
   Replace `<your-mapbox-token>` with your actual Mapbox API key. If you don't have one, you can generate it by signing up at [Mapbox](https://console.mapbox.com/account/access-tokens).

5. Start the frontend development server:
   ```bash
   npm run dev
   ```

6. Open your browser and navigate to:
   ```
   http://localhost:3000
   ```

--- 

## Usage Instructions

1. When you load the application, your browser will prompt for geolocation access.
2. Once you allow access:
   - The latitude and longitude fields will be pre-filled with your current location.
3. Adjust the radius (in kilometers) or leave it as the default (5 km).
4. Click the **Find Food Trucks Nearby** button.
5. Interact with the application:
   - **Map**: Hover over or click on markers to view food truck details.
   - **List View**: Click on food trucks in the sidebar to see details.

---

## Running Tests

To run unit tests for the backend:
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Execute the following command:
   ```bash
   python manage.py test -v 2
   ```
![Screenshot 2024-12-21 at 3 58 26 PM](https://github.com/user-attachments/assets/8dfb69fa-e3a9-4819-85f5-b83af818cf6e)

---

## File Structure

### **Frontend: `web-ui/`**
```
web-ui/
├── .next/
├── .vscode/
├── app/
│   ├── constants.ts          # Application constants
│   ├── favicon.ico           # Application icon
│   ├── globals.css           # Global styles
│   ├── layout.tsx            # Main layout file
│   ├── page.tsx              # Main page
│   ├── providers.tsx         # React providers
│   ├── services.ts           # API calls
├── node_modules/
├── public/
├── .env                      # Environment variables
├── .gitignore                # Git ignored files
├── .nvmrc                    # Node.js version
├── eslint.config.mjs         # ESLint configuration
├── next-env.d.ts             # Next.js environment types
├── next.config.js            # Next.js configuration
├── package-lock.json         # Lockfile for npm
├── package.json              # Node.js dependencies
├── postcss.config.mjs        # PostCSS configuration
├── README.md                 # Frontend README
├── tailwind.config.ts        # Tailwind CSS configuration
├── tsconfig.json             # TypeScript configuration
```

### **Backend: `backend/`**
```
backend/
├── .vscode/
├── backend/
├── core/
│   ├── assets/seed/
│   │   ├── food_truck_dataset.csv  # Seed data
│   ├── management/commands/
│   │   ├── seed_food_truck_data.py # Seed data command
│   ├── migrations/
│   │   ├── 0001_initial.py         # Initial migration
│   ├── service/
│   │   ├── __init__.py
│   │   ├── admin.py                # Admin panel settings
│   │   ├── apps.py                 # Django app config
│   │   ├── constants.py            # Backend constants
│   │   ├── models.py               # Database models
│   │   ├── serializer.py           # Serializers
│   │   ├── tests.py                # Backend tests
│   │   ├── urls.py                 # URL routing
│   │   ├── views.py                # API views
├── env/
├── .gitignore                     # Git ignored files
├── .python-version                # Python version
├── db.sqlite3                     # SQLite database
├── manage.py                      # Django entry point
├── requirements.txt               # Backend dependencies
```
---

## Future Improvements

- **Comprehensive Tests**:
  - Add more unit tests for both backend and frontend.
  - Include tests for UI elements to ensure component functionality.
  
- **Deployment**:
  - Deploy the backend and frontend using cloud services like AWS, Azure, or Vercel.
  
- **Database Migration**:
  - Move from SQLite3 to MySQL for better scalability and production readiness.
---

## License

This project is licensed and cannot be used, copied, modified, or distributed without explicit permission from the repository owner.
