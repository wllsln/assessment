# assessment
2015.06.30_Assessment

### Steps to perform tests on your local machine
1. Install pytest
> pip install -U pytest
2. Install unirest
> pip install unirest
3. Clone the git repository
> git clone https://github.com/wllsln/assessment
4. Change to that directory
> cd assessment
5. Run the tests in the current directory using pytest
> py.test

Any errors will be displayed in the screen output.

### Description of tests
Each test is described by the docstring from within the code.
The tests available are:
* test_location_code
* test_invalid
* test_valid_dates
* test_valid_temperatures

To add additional locations to be tested, simpliy edit test_weather.py and add the location in the lists valid_locations or invalid_locations.

To run an individual test rather than all the tests, you can specify that test name to py.test with the '-k' option. For example:
> py.test -k test_invalid
