## Wrapper scripts (optional but convenient)

### `run.sh` (Unix)
```bash
#!/bin/bash
# Simple wrapper – edit the default file names below
INPUT="studentNames.txt"
TEMPLATE="Assignment-02-Rubric.xlsx"
ASSIGNMENT="02"

python generate_rubrics.py -inputFile "$INPUT" -fileToCopy "$TEMPLATE" --assignment "$ASSIGNMENT"


### Make it executable
```bash
chmod +x run.sh
```
