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
            start_date = each_endpoint['default_start_date']
            end_date = each_endpoint['default_end_date']
            for each_report in self.__config["reports"]:
                report_for_all_locations = []
                for each_location in each_endpoint["location"]:
                    location = each_location
                    url = each_endpoint["base"] + each_report["resource"]
                    params = {
                        "location": location
                    }
                    if each_report['use_start_date_in_request']:
                        params['startDate'] = start_date
                    if each_report['use_end_date_in_request']:
                        params['endDate'] = end_date
                    get_report = requests.get(url, params=params,
                                              auth=HTTPBasicAuth(username=each_endpoint["username"],
                                                                 password=each_endpoint["password"]))
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
