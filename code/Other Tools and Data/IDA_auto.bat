::cd C:\Program Files (x86)\IDA 6.8
idaq -c -A -S"idc\analysis.idc" "D:\demo_longlongint.exe"
idaq -Ohexrays:outfile:ALL -A "D:\demo_longlongint.idb"
idaq -A -S"idc\analysis.idc" "D:\demo_longlongint.idb"