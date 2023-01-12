import pandas as pd
from datetime import date
import os


class ReportGenerator:
    def __init__(self, reports, config):
        self.__reports = reports
        self.__config = config

    def get_data_frame(self):
        base_location = self.__config["base_file_path"]
        for idx, x in enumerate(self.__config["reports"]):
            report_name = str(x['name'])
            prefix = str(x["prefix"])
            complete_report_path = os.path.join(base_location, prefix, report_name)
            reports_by_name = self.__reports[int(idx)][report_name]
            for index, each_report in enumerate(reports_by_name):
                report_df = pd.DataFrame.from_dict(each_report)
                for each_column in x['column_names']:
                    key = list(each_column.keys())[0]
                    value = each_column[key]
                    report_df.rename(columns={key: value}, inplace=True)

                facility = report_df['facility_name'].iat[0]
                start_date_split = str(report_df['start_date'].iat[0]).split('-')
                end_date_split = str(report_df['end_date'].iat[0]).split('-')
                start_date = date(day=int(start_date_split[2]), month=int(start_date_split[1]),
                                  year=int(start_date_split[0])).strftime("%d%b%Y")
                end_date = date(day=int(end_date_split[2]), month=int(end_date_split[1]),
                                year=int(end_date_split[0])).strftime("%d%b%Y")
                report_date = start_date + " - " + end_date
                report_df.drop(x['columns_to_remove'], axis=1, inplace=True)
                new_file = os.path.join(complete_report_path,
                                        prefix + ' ' + facility + ' ' + report_name + ' ' + report_date + '.csv')
                report_df.to_csv(new_file, index=False)
