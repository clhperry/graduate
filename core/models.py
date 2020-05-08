from django.db import models

class Course(models.Model):
    course_id = models.IntegerField(null=True)
    course_name = models.TextField()
    credits = models.IntegerField(null=True)
    dept = models.TextField()
    sbm_req = models.TextField()
    sbm_econ_req = models.TextField()
    sbm_math_req = models.TextField()
    sbm_bba_req = models.TextField()
    acct_req = models.TextField()
    ecof_math_req = models.TextField()
    ecof_req = models.TextField()
    econ_req = models.TextField()
    fina_acct_req = models.TextField()
    fina_comp_req = models.TextField()
    fina_req = models.TextField()
    gbus_3000_req = models.TextField()
    gbus_req = models.TextField()
    is_comp_req = models.TextField()
    is_req = models.TextField()
    is_analytics_req = models.TextField()
    is_audit_req = models.TextField()
    mark_req = models.TextField()
    mgmt_csr_req = models.TextField()
    mgmt_consulting_req = models.TextField()
    mgmt_entr_req = models.TextField()
    mgmt_deal_req = models.TextField()
    mgmt_hr_req = models.TextField()
    om_option_elective_req = models.TextField()
    om_option_req = models.TextField()
    om_req = models.TextField()
    qfin_math_a_req = models.TextField()
    qfin_math_b_req = models.TextField()
    qfin_electives_a_req = models.TextField()
    qfin_electives_b_req = models.TextField()
    qfin_electives_c_req = models.TextField()
    qfin_req = models.TextField()
    

    def __str__(self):
        return self.course_name
    

'''
reader = csv.reader(csvfile) 
for line in reader: 
    course = Course.objects.create()
course_id = line[0],
        course_name = line[1],
        credits = line[2],
        dept = line[3],
        sbm_req = line[4],
        sbm_econ_req = line[5],
        sbm_math_req = line[6],
        sbm_bba_req = line[7],
        acct_req = line[8],
        ecof_math_req = line[9],
        ecof_req = line[10],
        econ_req = line[11],
        fina_acct_req = line[12],
        fina_comp_req = line[13],
        fina_req = line[14],
        gbus_3000_req = line[15],
        gbus_req = line[16],
        is_comp_req = line[17],
        is_req = line[18],
is_analytics_req = line[19],
        is_audit_req = line[20],
        mark_req = line[21],
        mgmt_csr_req = line[22],
        mgmt_consulting_req = line[23],
        mgmt_entr_req = line[24],
        mgmt_deal_req = line[25],
        mgmt_hr_req = line[26],
        om_option_elective_req = line[27],
        om_option_req = line[28],
        om_req = line[29],
        qfin_math_a_req = line[30],
        qfin_math_b_req = line[31],
        qfin_electives_a_req = line[32],
        qfin_electives_b_req = line[33],
        qfin_electives_c_req = line[34],
        qfin_req = line[35],
        course.save()
'''


