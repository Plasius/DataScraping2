#az export csv formátum miatt kell lecserélni az adatokban lévő vesszőket
class Profile:
    def __init__(self, name, position, exp_name, exp_company, exp_start_date, exp_end_date,  study_institution, study_name, study_start_date, study_end_date):
        self.name = name.replace(",", ";")
        self.position = position.replace(",", ";")

        #experience
        self.exp_name = exp_name.replace(",", ";")
        self.exp_company = exp_company.replace(",", ";")
        self.exp_start_date = exp_start_date.replace(",", ";")
        self.exp_end_date = exp_end_date.replace(",", ";")

        # study:
        self.study_name = study_name.replace(",", ";")
        self.study_institution = study_institution.replace(",", ";")
        self.study_start_date = study_start_date.replace(",", ";")
        self.study_end_date = study_end_date.replace(",", ";")


    # Ez a function hívodik meg amikor egy Profile object-et belerakunk egy print() parancsba
    def __str__(self):
        return f"{self.name},{self.position},{self.exp_name},{self.exp_company},{self.exp_start_date},{self.exp_end_date},{self.study_name},{self.study_institution},{self.study_start_date}, {self.study_end_date}"
