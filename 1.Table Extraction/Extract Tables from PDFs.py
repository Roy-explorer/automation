import camelot

tables = camelot.read_pdf('1.Table Extraction/foo.pdf', pages='1', flavor='lattice')
print(tables)

tables.export('1.Table Extraction/foo.csv', f='csv', compress=True)
tables[0].to_csv('1.Table Extraction/foo.csv')  # to a csv file
print(tables[0].df)  # to a df
