#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
import unirest

valid_locations = [
    ("Los Angeles"),
    ("San Francisco, CA"),
    ("北京")
]

invalid_locations = [
    ("Invalid location"),
    ("123141...!"),
    ("Los Angeles, Oregon")
]

class TestWeather:
    '''
    Tests the weather app.
    '''

    def setup_method(self, method):
        '''
        setup any state tied to test execution
        '''
        self.api_url = "https://george-vustrey-weather.p.mashape.com/api.php"
        mashape_key = "FUItEv3UXumsh0i7of4DPkbhhQqmp1DudF3jsnmWOdcAT90B6M"
        self.api_hdr = {"X-Mashape-Key": mashape_key,
                        "Accept": "application/json"}

    def teardown_method(self, method):
        '''
        teardown any state tied to test execution
        '''
        pass

    def request_with_location(self, location):
        '''
        Send the HTTP GET request to our service with the given location.
        '''
        params = {"location":location}
        response = unirest.get(self.api_url,
                               headers=self.api_hdr,
                               params=params)
        return response

    @pytest.mark.parametrize("location",
                             valid_locations+invalid_locations)
    def test_location_code(self, location):
        '''
        Test that the endpoint is functioning.
        We should get code 200 regardless of if the location is valid or
        not, just depending on if the webservice was reachable.
        '''
        code = 200  # expected result
        response = self.request_with_location(location)
        assert response.code == code

    @pytest.mark.parametrize("location", invalid_locations)
    def test_invalid(self, location):
        '''
        Test that the endpoint properly reports invalid locations.
        The response payload will have JSON response with message of
        "Location not found".
        '''
        # expected result
        code = 1
        message = "Location not Found"

        response = self.request_with_location(location)
        json_response = response.body[0]
        assert json_response['code'] == code
        assert json_response['message'] == message

    @pytest.mark.parametrize("location", valid_locations)
    def test_valid_dates(self, location):
        '''
        Test that the endpoint properly returns proper payload dates.
        We should have seven entries for seven dates.
        '''
        response = self.request_with_location(location)
        json_response = response.body
        assert len(json_response) == 7

    @pytest.mark.parametrize("location", valid_locations)
    def test_valid_temperature(self, location):
        '''
        Test that the endpoint properly returns proper payload
        temperature.
        "high" and "low" should be float. 
        Celsius values should be integers.
        '''
        response = self.request_with_location(location)
        json_response = response.body
        for day in json_response:
            assert float(day["high"])
            assert float(day["low"])
            assert day["high_celsius"].isdigit()
            assert day["low_celsius"].isdigit()

