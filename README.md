# Salary-Function-README

## Introduction
This repository contains Python and R scripts to export employee details to a CSV file, save it within a zipped folder, and then unzip the folder to display the data. This README provides detailed instructions on how to use the provided code.

## Requirements
- Python 3.x
- R

## Usage

### Step 1: Python Script
1. Open the Python script (`export_employee_data.py`) in a text editor or an integrated development environment (IDE).
2. Modify the `employee_database` dictionary to include the employee details you want to export.
3. Specify the `employee_name` variable with the name of the employee whose details you want to export.
4. Run the Python script. It will export the employee's details to a CSV file and save it within a zipped folder named "Employee Profile."

### Step 2: Unzipping the Folder using R
1. Open an R environment or an R script editor.
2. Run the R script (`unzip_employee_data.R`) provided in this repository.
3. The R script will unzip the "Employee Profile" folder and display the data from the CSV file.

## File Structure
- `export_employee_data.py`: Python script to export employee details to a CSV file and save it within a zipped folder.
- `unzip_employee_data.R`: R script to unzip the folder created by the Python script and display the data from the CSV file.
- `Employee Profile.zip`: Zipped folder containing the exported employee details.
- `README.md`: This README file providing instructions on using the Python and R code.

## Notes
- Make sure to have the required dependencies (Python 3.x and R) installed on your system before running the scripts.
- Adjust the file paths in the scripts if the zipped folder is located in a different directory.

## Contact
If you encounter any issues or have any questions, feel free to contact me.
