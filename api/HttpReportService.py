import json

import requests
from requests.auth import HTTPBasicAuth


class HttpReportService:
    def __init__(self, config):
        self.__config = config
        self.__reports = []

    def get_location_for_all_endpoints(self):
        locations = []
        for each_endpoint in self.__config["endpoints"]:
            for each_location in each_endpoint["location"]:
                locations.append(each_location)
        locations = locations
        return locations

    def get_location_endpoint(self, location):
        for each_endpoint in self.__config["endpoints"]:
            for each_location in each_endpoint["location"]:
                if location == each_location:
                    return each_endpoint

    def get_reports_from_server(self):
        locations = self.get_location_for_all_endpoints()
        for each_report in self.__config["reports"]:
            report_for_all_locations = []
            reports = []
            for location in locations:
                location_end_point = self.get_location_endpoint(location)
                start_date = location_end_point['default_start_date']
                end_date = location_end_point['default_end_date']
                url = location_end_point["base"] + each_report["resource"]
                params = {
                    "location": location
                }
                if each_report['use_start_date_in_request']:
                    params['startDate'] = start_date
                if each_report['use_end_date_in_request']:
                    params['endDate'] = end_date
                get_report = requests.get(url, params=params,
                                          auth=HTTPBasicAuth(username=location_end_point["username"],
                                                             password=location_end_point["password"]))
                if get_report.status_code == 200:
                    report_json = json.loads(get_report.text)
                    for e in report_json:
                        e["facility_name"] = location
                        e['start_date'] = start_date
                        e['end_date'] = end_date
                    report_for_all_locations.append(report_json)
            reports.append(
                {
                    each_report["name"]: report_for_all_locations
                }
            )
            if len(reports) > 0:
                self.__reports = reports

    def get_reports(self):
        return self.__reports
