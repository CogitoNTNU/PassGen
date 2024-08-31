# PassGen

A simple wordbased password generator written in python. Generates passwords with a mix of words, numbers and special characters. Norwegian wordlist taken from [UIO](https://www.uio.no/studier/emner/matnat/ifi/nedlagte-emner/INF1001/h16/Obligatoriske%20innleveringer/ordliste.txt) (the program uses a subset of words that are 4-9 characters in length) and special characters are taken from the [OWASP list](https://www.owasp.org/index.php/Password_special_characters) with some exceptions for readability.

## Usage

```bash
usage: main.py [-h] [-w W] [-n N] [-s S] [-c C] [-i I]

options:
  -h, --help  show this help message and exit
  -w W        Number of words to generate default is 4
  -n N        Number of numbers to generate default is 2
  -s S        Number of special characters to generate default is 2
  -c C        Minimum number of capital letters to generate default is 1, larger values than w will get same result as w
  -i I        Number of iterations to generate passwords default is 1
```

## Installation

Just install python3 clone the repository and run the program with the desired options.