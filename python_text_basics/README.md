# Python Text Basics

## Python File Modes
* `r` - opens a file for reading. (default)
* `w` - opens a file for writing. creates a new file if it does not exist or truncates the file if it exits.
* `x` - opens a file for exclusive creation. If the file already exists, the operation fails.
* `a` - opens a file for appending at the end of the file without truncating it, creates a new file if it does not exist
* `t` - opens in text mode. (default)
* `b` - opens in binary mode.
* `+` - opens a file for updating (reading and writing)

## Working with PDF files
* We can use the `PyPDF2` library to read in text data from a PDF file.
* Some PDFs are created through scanning, instead of being exported from a text editor like Word
* These scanned PDF are more like image files, making it much harder to extract the text.

## Identifiers and Characters in Patterns in Regular Expressions
Characters such as a digit or a single string have different codes that represent them. You can use these to build up a 
pattern string. Notice how these make heavy use of the backwards slash \ . Because of this when defining a pattern string
for regular expression we use the format `r"mypattern"`. Placing the `r` in front of the string allows python to understand
that the `\` in the pattern string are not meant to be escape slashes.

* \d - a digit
* \w - alphanumeric
* \s - White space
* \D - a non digit
* \W - non-alphanumeric
* \S - non-whitespace
* `+` - Occurs one or more time
* {3} - Occurs exactly 3 times
* {2, 4} - Occurs 2 to 4 times
* {3,} - Occurs 3 or more
* \* - Occurs zero or more times
* ? - Once or none
