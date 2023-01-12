config = {
    "base_file_path": "./Q4 Reports",
    "endpoints": [{
        "base": "http://localhost:8081/openmrs/ws/rest/v1/",
        "username": "",
        "password": "",
        "default_start_date": "2022-04-01",
        "default_end_date": "2022-06-30",
        "location": [
            "Neno District Hospital", "Ligowe HC"
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
            "directory": "",
            "column_names": [

            ]
        },
    ]
}
