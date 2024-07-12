# FetchCodingExercise
Coding Exercise for Fetch

Exercise is completed utilizing Python, PyTest, and SeleniumBase.

SeleniumBase (sbase) is a Python framework built off of Selenium to simplify many features, including method definitions, error logging, and test run report generation, among other features. Details can be found at https://seleniumbase.io. <br />
Make sure to have pip and Python pre-installed.


To run the test file:
1. Create a virtual environment using "venv"
    - For macOS/Linux terminal: (python3 -m venv [env name])
        - Ex: python3 -m venv sbase_env
    - For Windows CMD: (py -m venv [env name])
        - Ex: py -m venv sbase_env
2. Activate your virtual environment
    - For macOS/Linux terminal: (source [env name]/bin/activate)
        - Ex: source sbase_env/bin/activate
    - For Windows CMD: (call [env name]\\Scripts\\activate)
        - Ex: call sbase_env\\Scripts\\activate
3. While  in Virtual Environment (venv is activated) Install Seleniumbase directing from PyPI (Python Package Index):
    - pip3 install seleniumbase
4. Navigate to FetchCodingExercise directory and run the python file using Pytest:
    - pytest test_find_fake_gold_bar.py
    - Command-line options:
        - Add "-s" to see print outputs
        - Add "--demo" to run the test in sbase demo mode (runs slower and highlights elements as it runs)
        - Add "--html=report.html" to generate a report (using name specified) after the test suite completes
        - Add "--dashboard" to create a dashboard HTML document to display results of test suite
5. A new "latest_logs" folder should now appear in the Exercise directory,
    containing screenshots of each weighting from the test run

Screenshots are taken after every weighing, which can be found in the latest_logs folder that is regenerated after every test run.<br />
If using "--html=report.html" or "--dashboard", new HTML document(s) will be generated in the directory with test results
