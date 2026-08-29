@echo off
REM Wrapper for Windows – edit the default file names
set INPUT=studentNames.txt
set TEMPLATE=Assignment-02-Rubric.xlsx
set ASSIGNMENT=02

python generate_rubrics.py -inputFile "%INPUT%" -fileToCopy "%TEMPLATE%" --assignment "%ASSIGNMENT%"
