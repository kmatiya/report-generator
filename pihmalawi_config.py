config = {
    "base_file_path": "./Q4 Reports",
    "endpoints": [
        {
            "base": "http://localhost:8081/openmrs/ws/rest/v1/",
            "username": "",
            "password": "",
            "default_start_date": "2022-04-01",
            "default_end_date": "2022-06-30",
            "location": [
                "Neno District Hospital", "Ligowe HC", "Magaleta HC", "Nsambe HC", "Dambe Clinic", "Neno Mission HC",
                "Matandani Rural Health Center", "Luwani RHC"
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
                # {"identifier": "ARV#"},
                # {"gender": "Gender"},
                # {"dob": "DOB"},
                # {"artStartDate": "ART start date"},
                # {"weight": "Weight(Kg)"},
                # {"artRegimen": "Regimen"},
                # {"arvsGiven": "ARVs"},
                # {"dispenseDate": "Dispensed date"},
            ],
            "columns_to_remove": [
                # 'location', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-cohort-disaggregated",
            "prefix": "MoH",
            "name": "Cohort Disaggregated Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                # {"identifier": "ARV#"},
                # {"gender": "Gender"},
                # {"dob": "DOB"},
                # {"artStartDate": "ART start date"},
                # {"weight": "Weight(Kg)"},
                # {"artRegimen": "Regimen"},
                # {"arvsGiven": "ARVs"},
                # {"dispenseDate": "Dispensed date"},
            ],
            "columns_to_remove": [
                # 'location', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-tpt-new-initiation",
            "prefix": "MoH",
            "name": "TPT New Initiation Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                # {"identifier": "ARV#"},
                # {"gender": "Gender"},
                # {"dob": "DOB"},
                # {"artStartDate": "ART start date"},
                # {"weight": "Weight(Kg)"},
                # {"artRegimen": "Regimen"},
                # {"arvsGiven": "ARVs"},
                # {"dispenseDate": "Dispensed date"},
            ],
            "columns_to_remove": [
                # 'location', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/moh-tx-curr-mmd",
            "prefix": "MoH",
            "name": "TX_CURR MMD Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                # {"identifier": "ARV#"},
                # {"gender": "Gender"},
                # {"dob": "DOB"},
                # {"artStartDate": "ART start date"},
                # {"weight": "Weight(Kg)"},
                # {"artRegimen": "Regimen"},
                # {"arvsGiven": "ARVs"},
                # {"dispenseDate": "Dispensed date"},
            ],
            "columns_to_remove": [
                # 'location', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/pepfar-cohort-disaggregated",
            "prefix": "PEPFAR",
            "name": "Cohort Disaggregated Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                # {"identifier": "ARV#"},
                # {"gender": "Gender"},
                # {"dob": "DOB"},
                # {"artStartDate": "ART start date"},
                # {"weight": "Weight(Kg)"},
                # {"artRegimen": "Regimen"},
                # {"arvsGiven": "ARVs"},
                # {"dispenseDate": "Dispensed date"},
            ],
            "columns_to_remove": [
                # 'location', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/pepfar-cohort-disaggregated",
            "prefix": "PEPFAR",
            "name": "TX_CURR MMD Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                # {"identifier": "ARV#"},
                # {"gender": "Gender"},
                # {"dob": "DOB"},
                # {"artStartDate": "ART start date"},
                # {"weight": "Weight(Kg)"},
                # {"artRegimen": "Regimen"},
                # {"arvsGiven": "ARVs"},
                # {"dispenseDate": "Dispensed date"},
            ],
            "columns_to_remove": [
                # 'location', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/pepfar-tx-ml",
            "prefix": "PEPFAR",
            "name": "TX_ML Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                # {"identifier": "ARV#"},
                # {"gender": "Gender"},
                # {"dob": "DOB"},
                # {"artStartDate": "ART start date"},
                # {"weight": "Weight(Kg)"},
                # {"artRegimen": "Regimen"},
                # {"arvsGiven": "ARVs"},
                # {"dispenseDate": "Dispensed date"},
            ],
            "columns_to_remove": [
                # 'location', 'facility_name', 'start_date', 'end_date'
            ]
        },
        {
            "resource": "pihmalawi/report/pepfar-tx-rtt",
            "prefix": "PEPFAR",
            "name": "TX_RTT Report",
            "use_start_date_in_request": True,
            "use_end_date_in_request": True,
            "column_names_to_rename": [
                # {"identifier": "ARV#"},
                # {"gender": "Gender"},
                # {"dob": "DOB"},
                # {"artStartDate": "ART start date"},
                # {"weight": "Weight(Kg)"},
                # {"artRegimen": "Regimen"},
                # {"arvsGiven": "ARVs"},
                # {"dispenseDate": "Dispensed date"},
            ],
            "columns_to_remove": [
                # 'location', 'facility_name', 'start_date', 'end_date'
            ]
        },
    ]
}
