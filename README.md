# agent-py

## Requirements

- Python > 3.12
- virtualenv [intall](https://virtualenv.pypa.io/en/latest/installation.html)

## Install project
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.dev.txt
```

## Before launching any command you must be in your venv
```sh
source .venv/bin/activate
```

## Launch the project
```sh
make help
make run
#or
make debug
```

## Configuration

Environment variable:

- AGENT_ENV: local/production
- AGENT_VERSION: app version, default 1.0.0, endpoint /version
- AGENT_DESCRIPTION: app description
- AGENT_DEBUG: activate debug mode (boolean)

local : enable reload mode (default)
prod : no hot reload

## Usage

Run project with `make debug` and consult url in log for api doc at `/docs` or `/redoc`.

Application is running 2 threads, one for the API to expose metrics and one for collecting metrics.
