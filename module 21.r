
library(utils)


zipped_folder_path <- "Employee Profile.zip"


unzip(zipped_folder_path)


csv_file_path <- list.files(pattern = ".csv")

employee_data <- read.csv(csv_file_path)

print(employee_data)
