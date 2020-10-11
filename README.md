# CEFT -- Coding Exercise From Tristan

CEFT is a Python3.6 + Selenium UI automation framework.

## Installation & Configuration

Please build your test environment simply using the command below:

```bash
pip install -r requirements.txt
```

## Usage

```
1. run command below to create docker containers (1 Selenium Grid Hub and 3 Nodes):
docker-compose -f docker-compose.yml up

2. run command below to start the script:
python ./run.py

3. Launch VNC Viewer (on Mac) and enter the following Remote Chrome Server address to connect to remote screen:
localhost:5900

```

## Notes
1. By default a test user account has been used for testing to log into the test system;   The current test user account will be deleted within 7 days owing to security concern.    However, you can use your own account to execute the test simply via replacing the user credential from ./data/testdata/data_info.xlsx  ( make sure username in cell B1 and password in cell B2 ); 
2. "Send Email" module has been commented out. To enable this function please: 
```
    1. set receiver from "./public/common/sendemail.py"
       recvaddress = ['receiver@xxx.xx']
       sendaddr_name = 'sender@xxx.xx'
       sendaddr_pswd = 'YOUR EMAIL PASSWORD'
```
```
    2. uncomment out below lines from "./run.py"
       #mail = sendmail.SendMail()
       #mail.send()
```
3. Please find below the link for the screen recording video:  https://drive.google.com/file/d/1CUtJA1c-yO625MEkXEC9tfxM_gglH443/view?usp=sharing
4. Please be aware that to run the script on another docker container (for example RFireFox), you will need to make the below changes in the code:
```
    1. Stop/Remove the docker containers via command:  "docker-compose -f docker-compose.yml down";
    2. Run command below to make sure containers have been removed correctly:  "docker ps -a";
    3. In ./config/globalparam.py, line 38 change the default browser from current 'RChrome' to 'RFireFox';
    4. Re-run the docker compose command to start new containers: "docker-compose -f docker-compose.yml up";
    5. In VNC Viewer start a new connection with Server address "localhost:5902".
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

# Containerised-Selenium
