cd C:\Users\taeuks\temp\EDGAR

forvalues y = 1993/2019 {
    forvalues q = 1/4 {
    import delimited ./csv/Y`y'Q`q'.csv, clear
    save ./stata/Y`y'Q`q', replace
    }
}

clear

forvalues y = 1993/2019 {
    forvalues q = 1/4 {
    append using ./stata/Y`y'Q`q'
    }
}
label data "Full Panel of EDGAR filings"
save ./stata/Panel, replace

use ./stata/Panel
gsort cik
duplicates drop cik, force
keep cik companyname
label data "CIK List"
save ./stata/ciklist, replace