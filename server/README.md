### Server setup

Set up server on Python 3.10 for these instructions to apply.
Must do this once on your device to set up the virtual enviornment:
```
cd server
python -m venv venv           # Create Python virtual env
source venv/bin/activate      # Enter venv **on macOS/Linux**
.\venv\bin\activate           # Enter venv **on Windows**
pip install -r requirements.txt
```

To start the backend server:
```
cd server
source venv/bin/activate  # Enter venv on macOS/Linux
.\venv\bin\activate       # Enter venv on Windows
python server.py              # To run routes
```
