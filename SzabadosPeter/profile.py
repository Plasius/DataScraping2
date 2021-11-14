class Profile:
    def __init__(self):
        self.name = ''
        self.position = ''

        #experience
        self.exp_name = ''
        self.exp_company = ''
        self.exp_start_date = ''
        self.exp_end_date = ''

        # study:
        self.study_name = ''
        self.study_institution = ''
        self.study_start_date = ''
        self.study_end_date = ''

        # certificate:
        self.cert_name = ''
        self.cert_institution = ''
        self.cert_date = ''

    # Ez a function hívodik meg amikor egy Profile object-et belerakunk egy print() parancsba
    def __str__(self):
        print(self.name, self.position, self.exp_name)
        print(self.exp_company, self.exp_start_date, self.exp_end_date)
        print(self.study_name, self.study_institution, self.study_start_date, self.study_end_date)
        print(self.cert_name, self.cert_institution, self.cert_date)
