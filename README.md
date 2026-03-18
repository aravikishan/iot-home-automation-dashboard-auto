# IoT Home Automation Dashboard

## Overview
The IoT Home Automation Dashboard is a comprehensive platform designed to manage and automate IoT devices within a smart home environment. This project provides an intuitive dashboard for users to monitor and control various devices, set automation rules, and manage user profiles. The solution is ideal for homeowners and developers looking to enhance their smart home systems with a user-friendly interface and robust backend support. By leveraging FastAPI and SQLite, the application ensures fast performance and easy scalability.

## Features
- **User Management**: Create, view, and manage user profiles with specific roles and permissions.
- **Device Control**: Monitor and control the status of connected IoT devices such as lights and thermostats.
- **Automation Rules**: Define and manage automation rules to automate device actions based on specific conditions.
- **Responsive UI**: A clean and responsive user interface built with Bootstrap for seamless interaction across devices.
- **Database Initialization and Seeding**: Automatic setup and seeding of the database with initial data for quick startup.
- **RESTful API**: Expose RESTful endpoints for integration with other applications or services.

## Tech Stack
| Technology   | Description                        |
|--------------|------------------------------------|
| Python       | Programming language               |
| FastAPI      | Web framework for building APIs    |
| SQLite       | Lightweight database engine        |
| Jinja2       | Templating engine for HTML         |
| Bootstrap    | CSS framework for responsive design|

## Architecture
The project is structured to separate concerns effectively, with a backend API built using FastAPI and a frontend rendered using Jinja2 templates. The backend serves static files and templates, and interacts with an SQLite database to manage data.

```plaintext
+------------------+
|   Frontend UI    |
| (HTML Templates) |
+---------+--------+
          |
          v
+---------+--------+
|  FastAPI Server  |
|  (app.py)        |
+---------+--------+
          |
          v
+---------+--------+
|   SQLite DB      |
| (iot_home_automation.db) |
+------------------+
```

### API Endpoints
| Method | Path            | Description                                 |
|--------|-----------------|---------------------------------------------|
| GET    | /               | Render the main dashboard page              |
| GET    | /devices        | Render the devices management page          |
| GET    | /automation     | Render the automation rules page            |
| GET    | /users          | Render the user profiles page               |
| GET    | /settings       | Render the settings page                    |
| GET    | /api/devices    | Retrieve a list of all devices              |
| POST   | /api/devices    | Add a new device                            |
| GET    | /api/rules      | Retrieve a list of all automation rules     |
| POST   | /api/rules      | Add a new automation rule                   |
| GET    | /api/users      | Retrieve a list of all users                |

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iot-home-automation-dashboard-auto.git
   cd iot-home-automation-dashboard-auto
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your web browser and visit:
   ```
   http://localhost:8000/
   ```

## Project Structure
```
.
├── Dockerfile                   # Docker configuration file
├── app.py                       # Main application file with API routes
├── requirements.txt             # Python dependencies
├── start.sh                     # Shell script to start the application
├── static/
│   └── css/
│       └── bootstrap.min.css    # Bootstrap CSS for styling
└── templates/
    ├── automation.html          # HTML template for automation rules page
    ├── dashboard.html           # HTML template for dashboard page
    ├── devices.html             # HTML template for devices page
    ├── settings.html            # HTML template for settings page
    └── users.html               # HTML template for user profiles page
```

## Screenshots
*Screenshots of the application can be added here to showcase the UI and features.*

## Docker Deployment
To deploy the application using Docker, use the following commands:
1. Build the Docker image:
   ```bash
   docker build -t iot-home-automation-dashboard-auto .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 iot-home-automation-dashboard-auto
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes. Ensure your code follows the project's coding standards.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---
Built with Python and FastAPI.