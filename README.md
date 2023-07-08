# New Russian wine

This is a website of the "New Russian Wine" wine store.
This project was written to make it easy to add different wines and drinks to the wine store website page. To make changes to the site, you only need to edit the `wine.xlsx` file, and the script will do everything itself for you.

### How to run

1. Firstly, you have to install python and pip (package-management system) if they haven't been already installed.
2. Open directory when you'd like to save the project. After use git to clone the repository and save all the code:
   ```sh
   git clone git@github.com:michaelmatasyants/wine.git
   ```
3. Create a virtual environment with its own independent set of packages using [virtualenv/venv](https://docs.python.org/3/library/venv.html). It'll help you to isolate the project from the packages located in the base environment.
   ```sh
   python3 -m venv .venv
   ```

4. Activate virtual environment:

   For Linux
   ```sh
   source .venv/bin/activate
   ```

   For Windows
   ```console
   .venv\Scripts\activate.bat
   ```

5. Install all the packages used in this project, in your virtual environment which you've created on the step 4. Use the `requirements.txt` file to install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

6. Run the website on local server:
    ```sh
    python3 main.py
    ```
7. Browse [http://127.0.0.1:8000](http://127.0.0.1:8000).

8. To add or delete some drinks:
   - Open `wine.xlsx`, make changes to it, save and quit the file;
   - If you already ran the website, stop running it by pressing `Ctrl + C`;
   - Run the website again to display the changes you made in `wine.xlsx`.

## Project Objectives

The code is written for educational purposes
