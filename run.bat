SET "PYTHON_PATH=C:\Users\nikit\AppData\Local\Programs\Python\Python310\python.exe"
:: Set base directory to the location of this script
SET BASE_DIR=%~dp0

"%PYTHON_PATH%" "%BASE_DIR%aimodel\extraction.py"
"%PYTHON_PATH%" "%BASE_DIR%aimodel\LLM_prediction.py"
