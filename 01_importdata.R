# Name : 01_importdata

# Purpose: Import the dataset from MySQL into R

# Author : Moses Otieno

# Date : 24 Jan 2021


# ---- Libraries

library(tidyverse)
library(odbc)

# ---- Connect to the database

db <-  dbConnect(odbc(),
                 Driver = "MySQL ODBC 8.0 ANSI Driver",
                 Server = Sys.getenv("server"),
                 database = "meterreading",
                 uid = Sys.getenv("uid"),
                 pwd = Sys.getenv("pwd"))


#---- Pull the tables each company ----

# KPLC
kplcreadings <- as_tibble(dbGetQuery(db,'
select entry_date, reading from kplcreading
'))

# KIWASCO
kiwascoreadings <- as_tibble(dbGetQuery(db,'
select entry_date, reading from kiwascoreading
'))


# Create a function to manage the datasets

managereadings <- function(data){
  data <- data %>%
    mutate(units = reading - lag(reading),
           entry_date = as.Date(entry_date),
           daydiff = as.integer(entry_date - lag(entry_date)),
           units_perday = round(units/as.integer(daydiff),1),
           month_read = month(entry_date, label = T,
                              abbr = F),
           date_read = format(entry_date, "%d-%B-%Y"))
}


kplcreadings <- managereadings(kplcreadings) %>%
  mutate(source = "kplc")
kiwascoreadings <- managereadings(kiwascoreadings) %>%
  mutate(source = "kiwasco")


readings <- bind_rows(kplcreadings, kiwascoreadings)


# ---- Save the datasets

saveRDS(kplcreadings, file = "kplcreadings.rds")
saveRDS(kiwascoreadings, file = "kiwascoreadings.rds")


