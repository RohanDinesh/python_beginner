print("this dictionary converts e letter month names into full name")

month_convertor={
    "jan":"January" ,
    "feb":"February" ,
    "mar":"March" ,
    "apr":"April" ,
    "may":"May" ,
    "jun":"June" ,
    "jul":"July",
    "aug":"August",
    "sep":"September",
    "oct":"October",
    "nov":"November",
    "dec":"December"
}

result=input("Enter 3 letter short name of any month: \n")
print(month_convertor[result])