#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
import unirest

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

    @pytest.mark.parametrize("location,code", [
        ("Los Angeles", 200),
        ("San Francisco, CA", 200),
        ("Invalid location", 200),
        ("123141...!", 200),
        ("北京", 200)
    ])
    def test_location(self, location, code):
        '''
        Test that the endpoint is functioning.
        We should get code 200 regardless of if the location is valid or
        not, just depending on if the webservice was reachable.
        '''
        response = self.request_with_location(location)
        assert response.code == code

