# Hello!

This is a simple app for the college that uses Replication as a technique to deal with Fault Tolerance in distributed systems scenario.

## Testing

If it's possible, I recommend you to use Python 3.5+ to run this application.

### Creating a virtual environment
Make sure that you have **virtualenv** installed in your machine too. After that, create an environment and give a name to him, like this:
```bash
virtualenv venv
```

### Activating
With your virtual environment created. Activate him with:
```bash
source venv/bin/activate
```

### Installing dependencies
With your environment activated, try to use `pip` to install the libraries:
```bash
pip install -r requirements.txt
```

### Running
If everything worked fine, you should be able to run the server without troubles:
```python
python server.py
```
The same could be do with the client:
```python
python client.py
```

### Deactivating environment
If you close the terminal everything should be closed, but if you wish to close the environment, try to use:
```bash
deactivate
```
