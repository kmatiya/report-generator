import json

import requests
from requests.auth import HTTPBasicAuth


class HttpReportService:
    def __init__(self, config):
        self.__config = config
        self.__reports = []

    def get_reports_from_server(self):
        for each_endpoint in self.__config["endpoints"]:
            reports = []
            for each_report in self.__config["reports"]:
                report_for_all_locations = []
                for each_location in each_endpoint["location"]:
                    url = each_endpoint["base"] + each_report["resource"]
                    params = {
                        # "startDate": each_endpoint["default_start_date"],
                        "date": each_endpoint["default_end_date"],
                        "location": each_location
                    }
                    get_report = requests.get(url, params=params,
                                              auth=HTTPBasicAuth(username=each_endpoint["username"],
                                                                 password=each_endpoint["password"]))
                    if get_report.status_code == 200:
                        report_for_all_locations.append(json.loads(get_report.text))
                reports.append(
                    {
                        each_report["name"]: report_for_all_locations
                    }
                )
            if len(reports) > 0:
                self.__reports = reports

    def get_reports(self):
        return self.__reports
