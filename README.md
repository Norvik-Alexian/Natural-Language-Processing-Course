## Specific SRF time 
this [website]('https://strftime.org/) provide specifc SRF time code.

## Python File Modes
* `r` - opens a file for reading. (default)
* `w` - opens a file for writing. creates a new file if it does not exist or truncates the file if it exits.
* `x` - opens a file for exclusive creation. If the file already exists, the operation fails.
* `a` - opens a file for appending at the end of the file without truncating it, creates a new file if it does not exist
* `t` - opens in text mode. (default)
* `b` - opens in binary mode.
* `+` - opens a file for updating (reading and writing)

## Working with PDF files
* Often you may need to read in text data from a PDF file.
* We can use the `PyPDF2` library to read in text data from a PDF file.
* Some PDFs are created through scanning, instead of being exported from a text editor like Word
* These scanned PDF are more like image files, making it much harder to extract the text.