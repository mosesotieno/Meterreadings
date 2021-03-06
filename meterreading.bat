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



START "" "C:\Program Files\R\R-4.1.2\bin\Rscript.exe" 01_importdata.R /b


:: Automatically commit the datasets and push them to repo

git add  meterreading/kiwascoreadings.rds meterreading/kplcreadings.rds


git commit -m "Updated the two datasets"

git push origin master

:: Run the python script to submit readings to mail
python "D:\InterestingTasks\meterreadings\04_sendupdates.py"


:: Launch the applcation

Rscript -e "rmarkdown::run('"D:/InterestingTasks/meterreadings/meterreading/meterreadingdash.Rmd"', shiny_args = list(launch.browser = TRUE))"

pause