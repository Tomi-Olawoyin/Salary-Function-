employee_database = {
        "NATHANIEL FORD": {"position": "GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY", "basepay": 167411.18, "overtimepay":0, "Otherpay":400184.25, "benefits": "Not Provided", "totalpay":567595.43, "totalpaybenefits": 567595.43, "year":2011},
        "GARY JIMENEZ": {"position": "CAPTAIN III (POLICE DEPARTMENT)", "basepay": 155966.02, "overtimepay":245131.88, "Otherpay":137811.38, "benefits": "Not Provided", "totalpay":538909.28, "totalpaybenefits": 538909.28, "year":2011},
        "ALBERT PARDINI": {"position": "CAPTAIN III (POLICE DEPARTMENT)", "basepay": 212739.13, "overtimepay":106088.18, "Otherpay":16452.6, "benefits": "Not Provided", "totalpay":335279.91, "totalpaybenefits": 335279.91, "year":2011},
        "CHRISTOPHER CHONG": {"position": "WIRE ROPE CABLE MAINTENANCE MECHANIC", "basepay": 77916, "overtimepay":56120.71, "Otherpay":198306.9, "benefits": "Not Provided", "totalpay":332343.61, "totalpaybenefits": 332343.61, "year":2011},
        "PATRICK GARDNER": {"position": "DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)", "basepay": 134401.6, "overtimepay":9737, "Otherpay":182234.59, "benefits": "Not Provided", "totalpay":326373.19, "totalpaybenefits": 326373.19, "year":2011}

     }



def get_employee_details(employee_name):

   employee_database = {
        "NATHANIEL FORD": {"position": "GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY", "basepay": 167411.18, "overtimepay":0, "Otherpay":400184.25, "benefits": "Not Provided", "totalpay":567595.43, "totalpaybenefits": 567595.43, "year":2011},
        "GARY JIMENEZ": {"position": "CAPTAIN III (POLICE DEPARTMENT)", "basepay": 155966.02, "overtimepay":245131.88, "Otherpay":137811.38, "benefits": "Not Provided", "totalpay":538909.28, "totalpaybenefits": 538909.28, "year":2011},
        "ALBERT PARDINI": {"position": "CAPTAIN III (POLICE DEPARTMENT)", "basepay": 212739.13, "overtimepay":106088.18, "Otherpay":16452.6, "benefits": "Not Provided", "totalpay":335279.91, "totalpaybenefits": 335279.91, "year":2011},
        "CHRISTOPHER CHONG": {"position": "WIRE ROPE CABLE MAINTENANCE MECHANIC", "basepay": 77916, "overtimepay":56120.71, "Otherpay":198306.9, "benefits": "Not Provided", "totalpay":332343.61, "totalpaybenefits": 332343.61, "year":2011},
        "PATRICK GARDNER": {"position": "DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)", "basepay": 134401.6, "overtimepay":9737, "Otherpay":182234.59, "benefits": "Not Provided", "totalpay":326373.19, "totalpaybenefits": 326373.19, "year":2011}

     }
   if employee_name in employee_database:
       
                 return employee_database[employee_name]
   else:
       
                return "Employee not found in database"
   
employee_name = "NATHANIEL FORD"
employee_details = get_employee_details(employee_name)
print("Employee Details for", employee_name, ":", employee_details)

try:
    
    total_salary_all_employees = sum(employee['totalpay'] for employee in employee_database.values())

    
    highest_paid_employee = max(employee_database, key=lambda x: employee_database[x]['totalpay'])

    
    lowest_paid_employee = min(employee_database, key=lambda x: employee_database[x]['totalpay'])

    
    print("Total Salary for all Employees:", total_salary_all_employees)
    print("Highest Paid Employee:", highest_paid_employee, "- Total Pay:", employee_database[highest_paid_employee]['totalpay'])
    print("Lowest Paid Employee:", lowest_paid_employee, "- Total Pay:", employee_database[lowest_paid_employee]['totalpay'])

except KeyError as e:
    print("Error: Key not found in employee database:", e)
except Exception as e:
    print("An error occurred:", e)


import csv
import zipfile
import os

employee_database = {
    "NATHANIEL FORD": {"position": "GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY", "basepay": 167411.18, "overtimepay":0, "Otherpay":400184.25, "benefits": "Not Provided", "totalpay":567595.43, "totalpaybenefits": 567595.43, "year":2011},
    "GARY JIMENEZ": {"position": "CAPTAIN III (POLICE DEPARTMENT)", "basepay": 155966.02, "overtimepay":245131.88, "Otherpay":137811.38, "benefits": "Not Provided", "totalpay":538909.28, "totalpaybenefits": 538909.28, "year":2011},
    "ALBERT PARDINI": {"position": "CAPTAIN III (POLICE DEPARTMENT)", "basepay": 212739.13, "overtimepay":106088.18, "Otherpay":16452.6, "benefits": "Not Provided", "totalpay":335279.91, "totalpaybenefits": 335279.91, "year":2011},
    "CHRISTOPHER CHONG": {"position": "WIRE ROPE CABLE MAINTENANCE MECHANIC", "basepay": 77916, "overtimepay":56120.71, "Otherpay":198306.9, "benefits": "Not Provided", "totalpay":332343.61, "totalpaybenefits": 332343.61, "year":2011},
    "PATRICK GARDNER": {"position": "DEPUTY CHIEF OF DEPARTMENT,(FIRE DEPARTMENT)", "basepay": 134401.6, "overtimepay":9737, "Otherpay":182234.59, "benefits": "Not Provided", "totalpay":326373.19, "totalpaybenefits": 326373.19, "year":2011}
}


employee_name = "NATHANIEL FORD"
employee_details = employee_database.get(employee_name)

if employee_details:
    
    csv_file_path = f"{employee_name}_details.csv"

    
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = employee_details.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(employee_details)


    zipped_folder_path = "Employee Profile.zip"

    
    with zipfile.ZipFile(zipped_folder_path, 'w') as zipf:
        zipf.write(csv_file_path, os.path.basename(csv_file_path))

    print(f"Employee details for {employee_name} exported to '{csv_file_path}' and saved within '{zipped_folder_path}'.")
else:
    print(f"Employee '{employee_name}' not found in the database.")
