:: ----------------------------- Begin Header -----------------------------------
:: Name of the batch file : MeterreadingReminder.bat
::
:: Purpose : Send reminder whenever the entries have not been made into the DB
::
:: Input  :  03_confirmentry.py
::
::
:: Output : Email sent if entry not made
::
::
:: Authors : Moses Otieno
::
::
:: Contact Email : motieno@kemricdc.org
::
::
:: First version : 25 June 2021
::
::
:: Reviewed :
::
:: ----------------------------- End Header--------------------------------------


:: Change the directory appropriately

D:
cd "D:\InterestingTasks\meterreadings"


:: Run the python script to enter meter readings
python "D:\InterestingTasks\meterreadings\03_confirmentry.py"
