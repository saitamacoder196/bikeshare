# Explore US Bikeshare Data

## Project Description
This project uses Python to explore bikeshare data from three major cities in the US: Chicago, New York City, and Washington. The goal is to analyze and calculate descriptive statistics to better understand the usage of the bikeshare systems.

## Installation Requirements
- Python 3
- pandas
- NumPy
- Streamlit

## Installation Guide

### Step 1: Set Up a Virtual Environment
A virtual environment helps to manage dependencies for your project and prevents conflicts between packages. Follow these steps to set up a virtual environment:

#### Using `venv`:
1. Open your terminal or command prompt.
2. Navigate to your project directory where `bikeshare.py` is located.
3. Create a virtual environment by running:
   ```bash
   python -m venv bikeshare_env
   ```
   This will create a directory named `bikeshare_env` containing the virtual environment.

### Step 2: Activate the Virtual Environment
Once the virtual environment is created, you need to activate it:

#### On Windows:
1. Run:
   ```bash
   bikeshare_env\Scripts\activate
   ```

#### On MacOS/Linux:
1. Run:
   ```bash
   source bikeshare_env/bin/activate
   ```

After activation, your terminal prompt will change to indicate that the virtual environment is active.

### Step 3: Install the Required Packages
With the virtual environment active, you can now install the necessary packages using the `requirements.txt` file.

Create a file named `requirements.txt` with the following content:
```plaintext
pandas
numpy
streamlit
```

Install the packages by running:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

### CLI Application
1. Ensure that you have installed all the necessary libraries.
2. Place the data files `chicago.csv`, `new_york_city.csv`, and `washington.csv` in the same directory as the `bikeshare.py` file.
3. Run the `bikeshare.py` file using the command: `python bikeshare.py`.
4. Follow the instructions in the terminal to view descriptive statistics and raw data.

#### Example
Below is an example of a session with the application:

```plaintext
Hello! Let's explore some US bikeshare data!
Please choose a city:
1. Chicago
2. New York City
3. Washington
Enter the number corresponding to the city: 1
Please choose a month:
1. January
2. February
3. March
4. April
5. May
6. June
7. All
Enter the number corresponding to the month or "7" for no month filter: 7
Please choose a day of the week:
1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday
6. Saturday
7. Sunday
8. All
Enter the number corresponding to the day or "8" for no day filter: 8

Calculating The Most Frequent Times of Travel...

Most Popular Month: 6
Most Popular Day of Week: Wednesday
Most Popular Start Hour: 17

Calculating The Most Popular Stations and Trip...

Most Popular Start Station: Streeter Dr & Grand Ave
Most Popular End Station: Streeter Dr & Grand Ave
Most Popular Trip: Streeter Dr & Grand Ave to Streeter Dr & Grand Ave

Calculating Trip Duration...

Total Travel Time: 280871787
Mean Travel Time: 936.23929

Calculating User Stats...

User Types:
Subscriber    238889
Customer      61110
Name: User Type, dtype: int64

Would you like to see 5 lines of raw data? Enter yes or no: no

Would you like to restart? Enter yes or no.
```

### Streamlit Web Application
1. Run the Streamlit application using the command:
   ```bash
   streamlit run bikeshare_app.py
   ```
2. Open your web browser and go to the URL provided by Streamlit to use the application.