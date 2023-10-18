config = {
    "base_file_path": "./Q3 Reports",
    "endpoints": [
        {
            "base": "https://neno.pih-emr.org:11443/openmrs/ws/rest/v1/",
            "username": "",
            "password": "",
            "default_start_date": "2023-07-01",
            "default_end_date": "2023-09-30",
            "location": [
                "Neno District Hospital", "Ligowe HC", "Magaleta HC", "Nsambe HC", "Dambe Clinic", "Neno Mission HC",
                "Matandani Rural Health Center", "Luwani RHC"
            ]
        },
        {
            "base": "http://lisungwi.pih-emr.org:8100/openmrs/ws/rest/v1/",
            "username": "",
            "password": "",
            "default_start_date": "2023-09-30",
            "default_end_date": "2023-09-30",
            "location": [
                "Lisungwi Community Hospital", "Zalewa HC", "Matope HC", "Midzemaba HC", "Chifunga HC",
                "Nkhula Falls RHC"
            ]
        },
    ],
    "reports": [
        {
            "resource": "pihmalawi/report/moh-regimen-switch",
            "prefix": "MoH",
            "name": "Regimen Switch Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": False,
            "column_names_to_rename": [
                {"identifier": "ARV#"},
                {"gender": "Gender"},
                {"dob": "DOB"},
                {"artStartDate": "ART start date"},
                {"weight": "Weight"},
                {"previousRegimen": "Prev.Reg"},
                {"currentRegimen": "Curr.Reg"},
                {"arvs": "ARVs"},
                {"dispenseDate": "Curr.reg dispensed"},
            ],
            "columns_to_remove": [
                'arvsGiven', 'location', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-survival-analysis-general",
            "prefix": "MoH",
            "name": "Survival Analysis (General) Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"reg_cohort": "Reg Cohort"},
                {"interval_year": "Interval (months)"},
                {"subgroup": "Sub group"},
                {"total_reg_database": "Total Reg(database)"},
                {"alive": "Alive"},
                {"died": "Died"},
                {"defaulted": "Defaulted"},
                {"stopped": "Stopped"},
                {"to": "TO"},
                {"unknown": "Unknown"},
            ],
            "columns_to_remove": [
                'reportingYear', 'reportingQuarter', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-survival-analysis-children",
            "prefix": "MoH",
            "name": "Survival Analysis (Children) Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"reg_cohort": "Reg Cohort"},
                {"interval_year": "Interval (months)"},
                {"subgroup": "Sub group"},
                {"total_reg_database": "Total Reg(database)"},
                {"alive": "Alive"},
                {"died": "Died"},
                {"defaulted": "Defaulted"},
                {"stopped": "Stopped"},
                {"to": "TO"},
                {"unknown": "Unknown"},
            ],
            "columns_to_remove": [
                'reportingYear', 'reportingQuarter', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-survival-analysis-option-b",
            "prefix": "MoH",
            "name": "Survival Analysis (Option B) Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"reg_cohort": "Reg Cohort"},
                {"interval_year": "Interval (months)"},
                {"subgroup": "Sub group"},
                {"total_reg_database": "Total Reg(database)"},
                {"alive": "Alive"},
                {"died": "Died"},
                {"defaulted": "Defaulted"},
                {"stopped": "Stopped"},
                {"to": "TO"},
                {"unknown": "Unknown"},
            ],
            "columns_to_remove": [
                'reportingYear', 'reportingQuarter', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-regimen-dispensation",
            "prefix": "MoH",
            "name": "Regimen Dispensation Report",
            "use_start_date_in_request": False,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"identifier": "ARV#"},
                {"gender": "Gender"},
                {"dob": "DOB"},
                {"artStartDate": "ART start date"},
                {"weight": "Weight(Kg)"},
                {"artRegimen": "Regimen"},
                {"arvsGiven": "ARVs"},
                {"dispenseDate": "Dispensed date"},
            ],
            "columns_to_remove": [
                'location', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-regimen-dispensation-by-weight",
            "prefix": "MoH",
            "name": "Regimen Dispensation By Weight Report",
            "use_start_date_in_request": False,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"weightGroup": "Weight Band"},
                {"gender": "Gender"},
                {"nonStandard": "Unknown"},
            ],
            "columns_to_remove": [
                'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-cohort-disaggregated",
            "prefix": "MoH",
            "name": "Cohort Disaggregated Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"sortValue": "#"},
                {"ageGroup": "Age Group"},
                {"gender": "Gender"},
                {"txNew": "Tx new (new on ART)"},
                {"txCurr": "TX curr (receiving ART)"},
                {"txCurrIpt": "TX curr (received IPT)"},
                {"txCurrScreenedTb": "TX curr (screened for TB)"},
                {"nonStandard": "Unknown"},
            ],
            "columns_to_remove": [
                'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-tpt-new-initiation",
            "prefix": "MoH",
            "name": "TPT New Initiation Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"sortValue": "#"},
                {"district": "District"},
                {"gender": "Gender"},
                {"ageGroup": "Age Group"},
                {"newStartThreeHp": "3HP(Started new on ART)"},
                {"newStartSixH": "6HP(Started New on ART)"},
                {"previousStartThreeHp": "3HP(Started Previously on ART)"},
                {"previousStartSixH": "6H(Started Previously on ART)"},
            ],
            "columns_to_remove": [
                'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-tx-curr-mmd",
            "prefix": "MoH",
            "name": "TX_CURR MMD Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"sortValue": "#"},
                {"ageGroup": "Age Group"},
                {"gender": "Gender"},
                {"lessThanThreeMonths": "# of clients on <3 months of ARVs"},
                {"threeToFiveMonths": "# of clients on 3 - 5 months of ARVs"},
                {"sixMonthsPlus": "# of clients on >= 6 months of ARVs"},
            ],
            "columns_to_remove": [
                'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/pepfar-cohort-disaggregated",
            "prefix": "PEPFAR",
            "name": "Cohort Disaggregated Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"sortValue": "#"},
                {"ageGroup": "Age Group"},
                {"gender": "Gender"},
                {"txNew": "Tx new (new on ART)"},
                {"txCurr": "TX curr (receiving ART)"},
                {"txCurrIpt": "TX curr (received IPT)"},
                {"txCurrScreenedTb": "TX curr (screened for TB)"},
            ],
            "columns_to_remove": [
                'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/pepfar-tx-curr-mmd",
            "prefix": "PEPFAR",
            "name": "TX_CURR MMD Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"sortValue": "#"},
                {"ageGroup": "Age Group"},
                {"gender": "Gender"},
                {"lessThanThreeMonths": "# of clients on <3 months of ARVs"},
                {"threeToFiveMonths": "# of clients on 3 - 5 months of ARVs"},
                {"sixMonthsPlus": "# of clients on >= 6 months of ARVs"},
            ],
            "columns_to_remove": [
                'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/pepfar-tx-ml",
            "prefix": "PEPFAR",
            "name": "TX_ML Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"sortValue": "#"},
                {"ageGroup": "Age Group"},
                {"gender": "Gender"},
                {"died": "Died"},
                {"iit3moOrLessMo": "IIT <3 mo"},
                {"iit3to5Mo": "IIT 3-5 mo"},
                {"iit6+Mo": "IIT 6+ mo"},
                {"transferredOut": "Transferred out"},
                {"refusedStopped": "Refused (Stopped) "},
            ],
            "columns_to_remove": [
                'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/pepfar-tx-rtt",
            "prefix": "PEPFAR",
            "name": "TX_RTT Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"sortValue": "#"},
                {"ageGroup": "Age Group"},
                {"gender": "Gender"},
                {"returnedLessThanThreeMonths": "Returned <3 mo"},
                {"returnedThreeToFiveMonths": "Returned 3-5 mo"},
                {"returnedSixMonthsPlus": "Returned 6+ mo"},
            ],
            "columns_to_remove": [
                'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/pepfar-tb-prev",
            "prefix": "PEPFAR",
            "name": "TB_Prev Report",
            "use_start_date_in_request": False,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                {"sortValue": "#"},
                {"ageGroup": "Age Group"},
                {"gender": "Gender"},
                {"newStartThreeHp": "3HP(Started New on ART)"},
                {"newStartSixH": "6H(Started New on ART)"},
                {"previousStartThreeHp": "3HP(Started Previously on ART)"},
                {"previousStartSixH": "6H(Started Previously on ART)"},
                {"completedNewStartThreeHp": "3HP(Completed New on ART)"},
                {"completedNewStartSixH": "6H(Completed New on ART)"},
                {"completedOldThreeHp": "3HP(Completed Previously on ART)"},
                {"completedOldSixH": "6H(Completed Previously on ART)"},
            ],
            "columns_to_remove": [
                'facility_name', 'start_date', 'end_date'
            ]
        },
    ]
}