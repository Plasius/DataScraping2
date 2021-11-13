import profile

fileName = "data.csv"
fileContent = "name,position,exp_name,exp_company,exp_start_date,exp_end_date,study_name,study_institution,study_start_date,study_end_date,cert_name,cert_institution,cert_date\n"
i = 0
profs = []

while i < 10:  # pelda miatt 10 profil
    profs.append(profile.Profile("a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"))  # random adatok
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
