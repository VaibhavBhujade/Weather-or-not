# WeatherOrNot
## Contents of this file
* Introduction
* Setup
* Techstack
* API used
* Maintainer


## INTRODUCTION
Weather or Not is a simple weather app which fetches data from an API to display current weather forecast of the place chosen in preferred language. Currently three languages are supported. It also gives a three day forecast. 



## SETUP

### Initial Setup

1. Clone or download the code from the repository.
2. Navigate to the project folder WeatherOrNot
3. Install the dependencies by running `pip install -r requirements.txt`
4. Install flask `pip install flask`
5. Get API key from <a href="https://www.weatherapi.com/" title="Free Weather API">WeatherAPI.com</a> and assign it in `constants.py

### To run
1. Run command `flask run`
2. In your browser go to `localhost:5000`

### Developer mode
To enter into developer mode and debug run the following commands
```
set FLASK_ENV=development
set FLASK_DEBUG=1
set FLASK_APP=app.py
```


### Testing
Testing is done using the nose framework.
1. Install the dependencies for testing `pip install -r test-requirements.txt`
2. Navigate to the test folder. To run the tests `nosetests testsdk.py -v`
Exception handling and Time to retrieve information is tested.
When a user enters invalid place, an exception should be thrown. 
Since weather updates must be real-time, the time taken to retrieve information is critical.

<table>
  <tr>
    <th>Test id</th>
    <th>Test name</th>
    <th>Test Description</th>
    <th>Test Input</th>
    <th>Expected Output</th>
    <th>Test Result</th>
  </tr>
  <tr>
    <td>T01</td>
    <td>test_weather_with_invalid_place</td>
    <td>Exception should be thrown for invalid place entered</td>
    <td>Place: qqqww, Language= en</td>
    <td>Exception Thrown</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>T02</td>
    <td>test_forecast_with_invalid_place</td>
    <td>Exception should be thrown for invalid place entered</td>
    <td>Place: qqqqq, Language= en</td>
    <td>Exception Thrown</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>T03</td>
    <td>test_time_Weather</td>
    <td>Test should pass within time limit</td>
    <td><0.9</td>
    <td>Executed before 0.9</td>
    <td>Pass</td>
  </tr>
  <tr>
    <td>T04</td>
    <td>test_time_Forecast</td>
    <td>Test should pass within time limit</td>
    <td><0.9</td>
    <td>Executed before 0.9</td>
    <td>Pass</td>
  </tr>
</table>

## Screenshots

![Sorry!! Couldn't load.](/Demo/Capture.JPG)
![Sorry!! Couldn't load.](/Demo/Capture2.JPG)
![Sorry!! Couldn't load.](/Demo/Capture3.JPG)

## TECH STACK
* `python 3.8.3`
* `flask 1.1.2`
* `HTML5`
* `CSS`

## API used
Powered by <a href="https://www.weatherapi.com/" title="Free Weather API">WeatherAPI.com</a>

## MAINTAINER
This project has been developed in the second round of UBS Avant Garde Engineering Challenge in the time period of seven days. The contributor to the project is : 
* Mr. Vaibhav Bhujade (`VaibhavBhujade`)  
