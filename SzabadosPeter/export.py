import profile

fileName = "data.csv"
fileContent = "name,position,exp_name,exp_company,exp_start_date,exp_end_date,study_name,study_institution,study_start_date,study_end_date,cert_name,cert_institution,cert_date\n"
i = 0
profs = []

while i < 10:  # pelda miatt 10 profil
    prof = profile.Profile()
    prof.name = 'hey'+str(i)
    prof.exp_name = 'exp'+str(i)
    prof.study_name = 'study'+str(i)
    prof.cert_name = 'cert'+str(i)
    profs.append(prof) 
    i += 1

with open(fileName, "w", encoding="utf-8") as f:
    for prof in profs:
        fileContent += prof.name + ","
        fileContent += prof.position + ","
        fileContent += prof.exp_name + ","
        fileContent += prof.exp_company + ","
        fileContent += prof.exp_start_date + ","
        fileContent += prof.exp_end_date + ","
        fileContent += prof.study_name + ","
        fileContent += prof.study_institution + ","
        fileContent += prof.study_start_date + ","
        fileContent += prof.study_end_date + ","
        fileContent += prof.cert_name + ","
        fileContent += prof.cert_institution + ","
        fileContent += prof.cert_date + "\n"
    f.write(fileContent)
