from zipfile import ZipFile

zip_ = ZipFile(".\\resources\\English for Information Technology [Pearson Longman].zip")
print(zip_.namelist())
# zip_.extract("English for Information Technology [Pearson Longman].pdf", "tmp")
zip_.extractall("tmp")
