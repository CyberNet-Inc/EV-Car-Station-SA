# EV Car Station SA

EV Car Station SA is a comprehensive application developed to help users locate nearby Electric Vehicle (EV) charging stations across South Africa. It integrates real-time data with a user-friendly interface, allowing users to plan routes, view station details, and manage usage effectively.

## Features

- **User Dashboard**: Locate nearby EV charging stations, view details, and plan routes.
- **Server Dashboard**: Manage charging station data, track user statistics, and monitor system status.
- **Real-time Updates**: Retrieves real-time data from external APIs.
- **User Authentication**: Secure login and registration using JWT for session management.
- **Mapping**: Interactive map view using Folium, integrated within a PyQt application.

## Technology Stack

- **Frontend**: Python, PyQt5 for GUI
- **Backend**: Flask for web framework
- **Database**: PostgreSQL for managing data
- **Mapping Library**: Folium for interactive maps

## Setup Instructions

### Prerequisites

- Install Python 3.9
- Install PostgreSQL
- Required Python packages:
  "bash
  pip install -r requirements.txt
"

### Database Setup

- Create PostgreSQL user and database:
  "sql
  CREATE USER your_username WITH PASSWORD 'your_password';
  CREATE DATABASE ev_charger_db;
  GRANT ALL PRIVILEGES ON DATABASE ev_charger_db TO your_username;
"
- Update SQLAlchemy connection URI in `app.py`

### Running the Application

1. **Start the Backend**
   "bash
   python app.py
   "
2. **Run the Frontend**
   "bash
   python main.py
   "

## Deployment

- **Docker**: Use Docker and Docker Compose for deployment.
- **CI/CD**: Integrate with services like GitHub Actions for continuous deployment.

## Author

CyberNet-Inc

## License

This project is licensed under the MIT License.