# Genpass: Password Generator Tool

## Create secure, strong, and unpredictable passwords

Genpass is a command-line tool designed to create strong, unpredictable passwords. Leveraging the power of Python, Genpass offers a simple yet powerful solution for generating passwords of varying lengths and complexities, and also allows you to exclude specific characters for greater control.

## ⚙️ System Requirements

Before using the program, make sure your system meets the following prerequisites:

- **Python:** Version 3.13 or higher must be installed on your machine. You can download the latest version from the official [Python website](https://www.python.org).

## 🚀 How to use:

Using Genpass is incredibly simple. Just follow the instructions below, depending on your operating system:

- **Unix (macOS, Linux, etc.)::**

    To generate a password with a specific length and exclude certain characters, use the following command structure:

    ```bash
    python3 genpass/main.py -l <length> -e <excluded_characters>
    ```
    **Example:** To generate a password with 18 characters, excluding the characters "a", "b", "1", "2", "3", "H", and "%", run:

    ```bash
    python3 genpass/main.py -l 18 -e ab123H%
    ```

- **Windows:**

    The command structure remains the same, but you'll typically replace ```python3``` with ```python```:

    ```bash
    python genpass/main.py -l <length> -e <excluded_characters>
    ```
    **Example**: To achieve the same result as the Unix example above on Windows, execute:

    ```bash
    python genpass/main.py -l 18 -e ab123H%
    ```

### Available Options: Tuning Password Generation

The following command line options give you precise control over password generation:

- ```-l```: This option allows you to specify the desired length of the password. The value you provide should be an integer representing the number of characters. If you omit this option, Genpass will default to generating a 20-character password.

    **Example:** ```python genpass/main.py -l 32``` will generate a password with 32 characters.

- ```-e```: Use this option to define a string of characters that you want to explicitly exclude from the generated password. This can be useful if certain systems or personal preferences restrict the use of specific symbols or letters.

    **Example:** ```python genpass/main.py -e "!@#$"``` will generate a password that does not contain any of the characters: !, @, #, or $.

- ```-h```, ```--help```: This option displays a helpful message outlining the available commands and options, providing a quick reference guide directly in your terminal.

    **Example:** ```python genpass/main.py -h``` or ```python genpass/main.py --help``` will show the help information.

## 📝 Licensing Information

This project operates under a specific license. For comprehensive details regarding the permissions and limitations of using, distributing, and modifying this software, please refer to the [LICENSE](LICENSE.md) file located in the project's root directory. We encourage you to review this file to understand your rights and responsibilities.
