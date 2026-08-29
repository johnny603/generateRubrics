# Use Case: Grading Assignment 02

## Scenario
You are a TA or instructor for CSC 215. You have just received a lot of submissions for Assignment 02. 
You need to create an individual rubric file for each student, fill in their grades, and return them.

## Steps with this tool

1. **Prepare your files**  
   - Put the list of student names in `studentNames.txt` (one per line).  
   - Place the official rubric template (e.g., `Assignment-02-Rubric.xlsx`) in the project folder.

2. **Generate all rubrics**  
   ```bash
   python generate_rubrics.py -inputFile studentNames.txt -fileToCopy Assignment-02-Rubric.xlsx --assignment 02
