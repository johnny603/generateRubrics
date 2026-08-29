# generateRubrics

A simple tool to create individual rubric copies for each student

## Features
- Reads a list of student names from a text file.
- Copies a rubric template (`.xlsx`, `.csv`, `.pdf`, or any file type) for every student.
- Renames each copy with the student’s name and assignment number.
- Places all copies into a single folder (`Rubrics` by default).
- Works on macOS, Linux, and Windows.
- **No Python libraries required** to copy your real Excel rubric files!

## Quick Demo (using the built-in dummy CSVs)

If you just want to test the script without any real files:

```
# 1. Generate two fake CSV rubric files (uses built-in Python only)
python3 samples/make_demo_files.py

# 2. Run the generator on the fake files
python3 generateRubrics.py -inputFile samples/studentNames.txt -fileToCopy samples/Assignment-01-Rubric.csv --assignment 01

# 3. Check the output
ls Rubrics/
Testing with Your Own Real Rubric Files (.xlsx, etc.)
Follow these steps to test the tool with your actual course rubrics:
```


## Get your real rubric file

Download or locate your official assignment rubric (e.g., Assignment-02-Rubric.xlsx) from your course materials.

Place it directly in the generateRubrics/ folder (or inside samples/ – anywhere is fine).

## Prepare your student list

Create a studentNames.txt file with one student name per line (or edit the existing one in the samples/ folder).

Example:

```
JaneDoe
JohnSmith
AliceWonder
```
Run the generator (No pip install required!)


```
python3 generateRubrics.py -inputFile studentNames.txt -fileToCopy Assignment-02-Rubric.xlsx --assignment 02
(If your file is in the samples/ folder, just add the path: -fileToCopy samples/Assignment-02-Rubric.xlsx)
```

Check the results
The script creates a folder called Rubrics/. Inside, you’ll see:

```
JaneDoe-Assignment-02-Rubric.xlsx
JohnSmith-Assignment-02-Rubric.xlsx
AliceWonder-Assignment-02-Rubric.xlsx
```
Open any of them in Excel – they are perfect, independent copies of your original rubric, ready for grading!

## Why openpyxl is Optional
You DO NOT need openpyxl to copy or rename Excel files. The script treats all files as generic binary data, so it works with .xlsx, .pdf, .docx, or any other format without installing anything.

The samples/make_demo_files.py script attempts to use openpyxl only to create dummy .xlsx files from scratch. If you don't have openpyxl, it automatically creates .csv files instead (which also open in Excel).

Conclusion: For your real grading workflow, just drop in your real .xlsx rubrics and run the script – zero external dependencies!

## Usage
```
python3 generateRubrics.py -inputFile <names.txt> -fileToCopy <rubric.xlsx> [--assignment <num>] [--outputFolder <dir>]
```
Troubleshooting
"File not found" error: Double-check that the path to your rubric file is correct.

Permission errors: Make sure you have write access to the folder where you're running the script.

Virtual environment warning: If you see the externally-managed-environment error when trying to install openpyxl, ignore it – you don't need it unless you specifically want to regenerate the dummy .xlsx demo files from scratch.

Why This Tool Saves Time
Avoids manual copy-paste errors – every student gets an identical template.

Batch processing – generate rubrics for an entire class in seconds.

Works everywhere – no need to compile an .exe or switch operating systems.

---

## Demo:

1. Put your real `Assignment-02-Rubric.xlsx` in this folder.
2. Make sure your `studentNames.txt` has your real class list.
3. Run:
   ```
   python3 generateRubrics.py -inputFile studentNames.txt -fileToCopy Assignment-02-Rubric.xlsx --assignment 02
   ```
That's it! Your Rubrics/ folder will populate with real .xlsx copies.
