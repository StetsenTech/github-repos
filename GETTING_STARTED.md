# GETTING STARTED

## Requirements

The following are required to be installed on the system to use this project.

- [Python 3.6.8](https://www.python.org/downloads/release/python-368/)

- PIP (Python 3)

- [Virtualenv](https://virtualenv.pypa.io/) **or** [VirtualenvWrapper](https://virtualenvwrapper.readthedocs.io/)

## Installing Requirements

### Python 3

- Macs with [Homebrew](https://brew.sh/): `brew install python3`
- Ubuntu: `sudo apt-get install python3`

### PIP (Python 3)

- Macs with Homebrew: `brew install python3-pip`
- Ubuntu: `sudo apt-get install python3-pip`

## Setup Environment

1. Ensure all requirements are installed
   - Follow the links to find out how to install each requirement per environment

2. Create a new virtual environment for this project
   - For virtualenv: `virtualenv {env_path} -p $(which python3)`
   - For virtualenvwrapper: `mkvirtualenv {env_name} -p $(which python3)`

3. Activate the created virtual environment
   - For virtualenv: `source {env_path}/bin/activate`
   - For virtualenvwrapper: `workon {env_name}`

4. Check to see if environment is setup
   - Check to see if virtualenv is active: `which python`
   - Check Python version: `python --version`

5. Install package requirements for project
   - `pip install -r requirements.txt`
