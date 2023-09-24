# IOT-SOFTWARE
This repository contains a Flask application designed for real-time monitoring and control of water quality using IoT sensors and actuators. The system provides a user interface for visualizing sensor data and interacting with actuators.


## Features

- **User Authentication**: Secure login system to access the monitoring dashboard.
- **Real-time Monitoring**: Display of real-time data from six IoT sensors through gauge charts.
- **Dynamic Data Update**: The sensor data is dynamically updated using an API endpoint that fetches data from the server.
- **Control Interface**: Provides controls to interact with actuators based on sensor data.
- **SQLite Integration**: Data persistence using a SQLite database.
- **Responsive Design**: Compatible with both desktop and mobile devices.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yuvi-kephi/IOT-SOFTWARE.git
   ```
2. Navigate to the project directory:
   ```
   cd KEPHI_STP
   ```
3. Install the required Python libraries:
   ```
   pip install flask flask_sqlalchemy
   ```
4. Run the Flask application:
   ```
   python app.py
   ```

## Usage

1. Access the application through a web browser at `http://localhost:5000`.
2. Use the login page to access the monitoring dashboard.
3. View real-time sensor data displayed as gauge charts.
4. Use the control interface to interact with actuators based on the sensor data.

## Contributing

If you wish to contribute to this project, kindly fork the repository and submit a pull request.

---

**Note**: Ensure you have the necessary environment and dependencies set up before running the application. Also, ensure that your IoT devices are correctly set up and connected to the server for accurate data retrieval and control.
