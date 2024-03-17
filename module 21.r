# Load the 'utils' package to use the unzip function
library(utils)

# Define the path to the zipped folder
zipped_folder_path <- "Employee Profile.zip"

# Unzip the folder
unzip(zipped_folder_path)

# Define the path to the CSV file within the unzipped folder
csv_file_path <- list.files(pattern = ".csv")

# Read the data from the CSV file
employee_data <- read.csv(csv_file_path)

# Display the data
print(employee_data)