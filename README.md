# Linkedin-Jobs

An Web automation using python and [Selenium Webdriver](https://selenium-python.readthedocs.io/index.html) for linkedin plataform, the aim is optimize search and apply for jobs. User set your credentials and the job type which he is looking for and the program search and apply for the jobs that can submit with linkedin feature "easy apply".


### Requirements
Before project installation, there are a few requirements for your computer:

- You need to have [python](https://www.python.org/downloads/) installed
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) installed if you use Firefox or [Chromedriver](https://chromedriver.chromium.org/downloads) for Chrome

### Installation

1. Clone this project in your machine.
```sh
$ git clone https://github.com/Lnvictor/linkedin-jobs
```

2. Copy the contrib/env-sample to .env in project root.
```sh
$ cp contrib/env-sample .env
```

3. Set your linkedin credentials in .env.

```.env
username=your_username
password=your_password
```

4. Then, install the project requirements:
```sh
$ pip install pipenv
$ pipenv sync
```


### How to run

To run the project is necessary set the job type that you are looking for in main.py and run:

```sh
$ pipenv run python main.py
```

### References

- [Selenium WebDriver Documentation](https://selenium-python.readthedocs.io/index.html)
- [Python with Selenium Course from Dunossauro](https://github.com/dunossauro/curso-python-selenium)
