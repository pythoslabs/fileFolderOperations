#Get just hte file names - not the extensions 
list_files = os.listdir(DIR)
# sample file name of the first file in the list
list_files[0])[:-4]  # easier way to do , than splitting on '.' to get the file name
