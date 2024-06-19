# Load required libraries
install.packages("dplyr") # Uncomment and run this line if you haven't installed the 'dplyr' package
library(dplyr)

# Read the CSV file
data <- read.csv("genes.csv")

# Group data by the "consequence" column
grouped_data <- data %>% group_by(Consequence)

# Create a directory to save the separate files (if it doesn't already exist)
dir_name <- "separated_genes"
if (!dir.exists(dir_name)) {
  dir.create(dir_name)
}

# Function to save each group to a separate CSV file
save_group_to_csv <- function(group) {
  consequence_name <- unique(group$Consequence)
  file_name <- paste0(dir_name, "/", consequence_name, "_genes.csv")
  write.csv(group, file_name, row.names = FALSE)
}

# Apply the function to each group and save them to separate CSV files
grouped_data %>% group_walk(save_group_to_csv)
