# Download EDGAR

- A series of codes (WSL, Python, Stata) that downloads SEC filings from EDGAR.

- Run in the order of:
    - `makedir.sh`: Creates subdirectories that will contain output.
    - `DownloadEDGAR.sh`: Downloads files from EDGAR using wget.
    - `ConvertCSV.py`: Converts downloaded files in `.idx` into `.csv` format.
    - `ConvertStata.do`: Reads the `.csv` files above, converts to Stata format. It also creates:
      - `Panel.dta`: a combined panel dataset of EDGAR filings.
      - `CIKList.dta`: a list of distinct identifiers (CIK), matched with firm names. 

- In a Windows environment with wget, Python, and Stata, the above sequence of codes can be run using `run.bat`.