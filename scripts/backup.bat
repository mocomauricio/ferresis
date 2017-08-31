@echo off 

ECHO "copiando la base de datos"
CD "C:\"
MKDIR %date:~0,2%%date:~3,2%%date:~8,2% 
CD  %date:~0,2%%date:~3,2%%date:~8,2% 
COPY "C:\Users\RDCrep130117\PROYECTOS\ferresis\ferresis\db.sqlite3" "."
ECHO "backup terminado"
PAUSE