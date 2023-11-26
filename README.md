# Code Compiler


## Project Tree

```css

project_root
│
├── src
│   ├── list_languages.py
│   └── main.py
│
├── bin
│   └── logfile.log
│
├── input
│   ├── language_list.txt
│   ├── code.txt
│   └── input.txt
│
├── .env
├── requirements.txt
└── README.md
```

## Overview


This project is a code execution tool that interacts with an online code compiler API. It consists of the following folders and files:

- **src:** Contains the main Python scripts.
  - `list_languages.py`: Retrieves and prints a list of available programming languages from the online code compiler API based on the contents of `language_list.txt` in the `input` folder.
  - `main.py`: Prompts the user for a programming language, checks its availability using the API, and then executes the code from `code.txt` in the `input` folder with corresponding input from `input.txt`. The output is stored in `output.txt` in the `bin` folder.
- **bin:** Stores the output of code execution (`output.txt`) and logs (`logfile.log`).
- **input:** Contains input files for code (`code.txt` and `input.txt`) and a list of languages (`language_list.txt`).
- **.env:** Environment configuration file.
- **requirements.txt:** Specifies the project's dependencies. Developers can install these dependencies using the `pip install -r requirements.txt` command to ensure a consistent environment.
- **README.md:** Documentation file.
- **.gitignore:** Ignored files and directories for version control.
- **LICENSE:** License information for the project.


## Installation

1. Use the following command to install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

2. Set the following environment variables in the `.env` file. You can get these details by subscribing to -  [Online Code Compiler](https://rapidapi.com/Glavier/api/online-code-compiler/)

  ```markdown

  - `API_KEY`: Your API key for authentication.
  - `HOST` : Host for the online compiler. [online-code-compiler.p.rapidapi.com]
  - `LANGUAGE_LIST_URL` : API base URL to GET Languages. [https://online-code-compiler.p.rapidapi.com/v1/languages/]
  - `COMPILE_CODE_URL` : API base URL to POST Request on online code compiler to execute the code. [https://online-code-compiler.p.rapidapi.com/v1/]

  ```

## Usage


1. Execute the `list_languages.py` script to retrieve and display the list of available programming languages. The information is sourced from the `language_list.txt` file located in the `input` directory. Note that this file is pre-populated for reference, and user don't need to run this script.

  
   ```bash
   python src/list_languages.py
   ```

2. Execute the `main.py` script to run user-specified code. The script will prompt the user for a programming language input. It will then perform the following steps:

   1. Check if the specified language exists using the `get_language` API call.
   2. Verify the presence of the `code.txt` file in the `input` directory, containing the code to be executed.
   3. Check for the existence of the `input.txt` file in the `input` directory for providing input to the code.
   4. If all checks pass, the script will execute the code and return the output, which will be recorded in `output.txt` in the `bin` directory.
   5. Logs for all operations will be generated and recorded in `logfile.log` in the `bin` directory. <br><br>

    ```bash
    python src/main.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.