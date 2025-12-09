This is my first attempt to create some sort of survey tool where people can click on some sort of front-end UI to fill out a form that sends the information to a database.


The way I see it, there are three parts to this

1. Front-End
2. Some sort of Backend API
3. Back End Database


# set up environment

As always, let's make sure we have python setup and configured before we do anthing else: 

## you will need python 3.10 - use pyenv perhaps to be able to install various pythons

## virtual environment
```
$ python3 --version
$ python3.10 -m venv .venv-3.10
$ source .venv-3.10/bin/activate
(venv) $
```

## install requirements
`pip install -r requirements.txt`




# Middle API Connection #

I am going to start with the middle part of this for now as it is the most familiar to me. Hopefully getting some traction going will motivate me to to push through and finish this project. 

chatgpt says that the best version to use is fastapi. 0.124.0 is the newest version so I will put that into the requirements.txt file.

Now that we have our framework, we still need some sort of server to actually run our project. Chat GPT says that uvicorn is the best bet for this. After doing a quick Google search, uvicorn is an Asynchronous Server Gateway Interface (ASGI). Essentially this is a tool for running python applications. 

PYPL says that 0.38.0 is the newest uvicorn version so I will throw that in to requirements.txt as well.

