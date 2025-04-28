# Genpass

Strong password generator

## 💻 Prerequisites

- Python3.13

## ☕ How to use
To use Genpass, follow these steps:

- **Unix:**

    This command generates a 18 character password and excludes the possibility of the characters "ab123H%":
    ```
    python3 genpass/main.py -l 18 -e ab123H%
    ```
- **Windows:**

    replace ```python3```to ```python``. The options are the same.


### options

- ```-l``` : password length (default 20)
- ```-e``` : characters to exclude from password
- ```-h, --help``` : show help message and exit

## 📝 License
This project is under license. See the [LICENSE](LICENSE.md) file for more details.
