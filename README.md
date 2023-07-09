# New Russian wine

This is a website of the "New Russian Wine" wine store.
This project was written to make it easy to add different wines and drinks to the wine store website page. To make changes to the site, you only need to edit the `wine.xlsx` file, or create a similar file and pass the file path. The script will do everything itself for you.

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

8. Add or delete some drinks.  
   
   There are two possible ways to do it:
   1. By changing the file wine.xlsx, which is in the root of the project
      - If you'd already run the website, stop it by pressing `Ctrl + C` in terminal;
      - Open `wine.xlsx`, make changes to it, save and quit the file;
      - Run the website again and browse it (steps six and seven) to display the changes you made in `wine.xlsx`.
      
   2. By creating an excel file similar in structure to `wine.xlsx` and passing the path to the file.
      - If you'd already run the website, stop it by pressing `Ctrl + C` in terminal;
      - Create a new excel file with the column names from `wine.xlsx` and add all the data that you nedd. Remember to save the path to the file to pass it in the next step.
      - Run the website again:
         ```
         python3 main.py -f path/to/the/file/new_wine_file.xlsx
         ```
      - Browse [http://127.0.0.1:8000](http://127.0.0.1:8000).
   
   <b> Remember that every time you edit the excel file, you must stop and rerun the website to display the changes. </b>

## Project Objectives

The code is written for educational purposes
