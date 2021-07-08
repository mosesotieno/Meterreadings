import os

# The following example uses the backup of the database. Other operations are similar.
os.system("mysqldump -u root -p Hiss@2020 meterreading > mysql.sql")

# The above code can also be optimized, how to optimize yourself according to the needs, the principle is so
