:: ----------------------------- Begin Header -----------------------------------
:: Name of the batch file : meterreading.bat
::
:: Purpose : Run the insert_readings.py and 01_importdata.R
::           This script will automate entry of meter readings
::           on a daily basis and update the dataset appropriately
::
:: Input  :  insert_readings.py
::           01_importdata.R
::
:: Output : Updated MySQL database and updated dataset
::
::
:: Authors : Moses Otieno
::
::
:: Contact Email : motieno@kemricdc.org
::
::
:: First version : 24 June 2021
::
::
:: Reviewed :
::
:: ----------------------------- End Header--------------------------------------


:: Change the directory appropriately

D:
cd "D:\InterestingTasks\meterreadings"


:: Run the python script to enter meter readings
python "D:\InterestingTasks\meterreadings\insert_readings.py"

:: Run the R script to update the datasets

START "" "C:\Program Files\R\R-4.0.5\bin\x64\Rscript.exe" 01_importdata.R /b

:: Automatically commit the datasets and push them to repo

git add kiwascoreadings.rds kplcreadings.rds

git commit -m "Updated the two datasets"

git push origin master


pause