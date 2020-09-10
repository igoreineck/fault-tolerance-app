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

First let the pyro name server running to start the server:

```python
python -m Pyro4.naming
```

Open another terminal, than activate your environment to start the master server:

```python
python server.py
```

The same could be do with the client:

```python
python client.py
```

Choose the desired option from the client menu:

- 1 - to echo a message
- 2 - list all messages
- 0 - exit the app

Then you can open as many server terminals you want, and close them just by pressing CTRL + C at the terminal and the data will still be consistent using the running servers

### Deactivating environment

If you close the terminal everything should be closed, but if you wish to close the environment, try to use:

```bash
deactivate
```

### To do

- [x] Allow call echo method on echo server, it takes as arg the message to be returned as a echo
- [x] Get already echoed messages list, this operation allow call getListOfMsg at echo servers to get the list of messages already sent by the clients
- [x] Reply the operations to other replica servers, the server can call a replica to other replica servers
- [x] Client can call the echo method on master server and this server can foward this call with the message to replica servers
- [ ] Tell the replica server quantity on server start

### Requirements

- [x] Allow N replica servers
- [x] Every server (master and replicas) should mantain all received message that can be called by the client with getListOfMsg method
- [x] If master server is down, the calling of echo method and getListOfMsg should be done to the next replica server and not be perceived by the user
- [x] Instantiate the server before the client
- [x] Ensure the server code is unique

### Optional

- [ ] The replica servers quantity should be equal the quantity the code is executed by the command line or steps below
- [x] Use a list of remote object name that represent the replica server
- [x] Allow users to kill the first server of list
- [ ] The first name of list could be the master server
- [x] When a new server is instantiated with a especific name of object, it should be added to the end of list
