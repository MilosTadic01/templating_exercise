
# Zootopia with API

This is a templating exercise which was gradually expanded to include interfacing of a python script with an API.


## Installation

To install this project, clone the repository and install the dependencies in requirements.txt. If on Windows, rely on `pip` rather than pip3.

```bash
  pip3 install -r requirements.txt
```

Furthermore, you'll need to register on api-ninjas.com in order to obtain an API key. Thereafter replace *your_api_key* in the following command and run it:

```bash
  echo API_KEY='your_api_key' > .env
```
## Usage/Examples

Program execution:

```bash
python3 animals_web_generator.py
```

Runtime printout:

```bash
Enter name of animal to produce a webpage about: cheetah

Webpage was successfully generated in file animals.html
```

## Feedback

If you have any feedback, please reach out to me @MilosTadic01


## License

[CC0 1.0 Universal](https://choosealicense.com/licenses/cc0-1.0/)

