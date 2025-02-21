# Cloud File Sharely

### Project Structure
```
PROJECT_ROOT
|── OAuth_client_ID_credentials_desktop
|   ├── credentials.json                 # Google OAuth2 credentials
|   └── token.json                       # Google OAuth2 token
├── data                                 # Data
├── Sharely                              # Project Package
│   ├── file_information.py              #
│   ├── sheet_downloader.py              # 
│   |
│   ├── csv_task_processor.py            #
│   ├── sheet_cell_color_manager.py      # 
│   └── share_file.py                    # 
|── main.py                              # Main entry
├── log                                  # STD output, STD Error output stream
└── venv                                 # pip vertial env
```


### Create the environment

#### With pip vertial environment
python --version `3.10.1`
```
pip3 install virtualenv
virtualenv venv --python=python3.10.1
source venv/bin/activate
pip install -r requirements.txt
deactivate
rm -rf venv     # remove the venv
```

#### Credentials.json Example 
```json
{
    "installed": {
        "client_id": "",
        "project_id": "",
        "auth_uri": "",
        "token_uri": "",
        "auth_provider_x509_cert_url": "",
        "client_secret": "",
        "redirect_uris": [
            "http://localhost"
        ]
    }
}
```

#### token.json Example 
```json
{
    "token": "",
    "refresh_token": "",
    "token_uri": "",
    "client_id": "",
    "client_secret": "",
    "scopes": [
        ""
    ],
    "expiry": ""
}
```

### License
Released under [MIT](./LICENSE) by @RobinHsieh 

This software can be modified and reused without restriction.
The original license must be included with any copies of this software.
If a significant portion of the source code is used, please provide a link back to this repository.