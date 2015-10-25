# Local Installation

## Using Docker

* Creates a Ubuntu 14.04 image with pip and all dependencies from requirements_dev.txt installed.
* The container uses start.sh to run lagesonum.
* To build the image use
    * `docker build -t lagesonum .`
* To run the container with current changes use the following command
    * *`docker run -ti -v $(pwd):/tmp/lagesonum -p 0.0.0.0:8000:8000 lagesonum`
* To ease the use you can define an alias like
    * `alias lagesonum='docker run -ti -v $(pwd):/tmp/lagesonum -p 0.0.0.0:8000:8000 lagesonum'`
    * `lagesonum`

## Without Docker

* Ensure you are running python3 `python --version`
* if you don't have python3:
    * on MacOSX: `brew install python3 && brew install gettext`
    * on Ubuntu: `sudo apt-get update && sudo apt-get install python3-pip`
    * on Windows: download from [python.org](https://www.python.org/downloads/windows)

* Create a virtual environment to keep your packages separate from the system
    * on Ubuntu or MacOSX:
        * `pyvenv-3.5 ~/.virtualenvs/lagesonum`
        * `source ~/.virtualenvs/bin/activate`
    * on Windows:
        * TBD

* Set your environment variables
    * `export SECRET_KEY=ASDF`
    * `export DJANGO_SETTINGS_MODULE=lagesonum.settings_dev`

* Install development requirements
    * `pip3 install -r requirements_dev.txt`

* Create the database and give a username, email address and password
    * `python3 manage.py migrate`
    * `python3 manage.py createsuperuser`

* Compile translation files
	* `cd website`
	* `python3 ../manage.py compilemessages`

* Run the development server
    * `python3 manage.py runserver`

* Check the website at http://localhost:8000

* Add an example Place in the Django admin
	* `http://localhost:8000/admin/website/place/add/`
	* try Pattern `.*` to accept any string

## SMS Setup
Sign up for an account from Twilio, and add your credentials to the environment as TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN. You will need to purchase a phone number which is able to send and receive SMS, and set it in your environment as TWILIO_DEFAULT_SENDER in E164 format (eg, '+4912345678901')

If you wish to test SMS notifications locally, you can use [ngrok](https://ngrok.com) to get an externally routable web address. Run `ngrok http 8000`, and make a note of the Forwarding URL. Set up the Twilio number Request URL to 'http://RANDOM_ID.ngrok.com/sms/post/'
