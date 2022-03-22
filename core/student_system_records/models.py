from django.db import models




class StreetAddress(models.Model):
    line_number = models.IntegerField()
    text = models.TextField()

class Address(models.Model):
    street = models.ForeignKey(StreetAddress, on_delete=models.CASCADE)
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()

class tblStudent(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    stfname = models.CharField(max_length=30)
    stlname = models.CharField(max_length=30)
    stcourse = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    adress = models.ForeignKey(Address, on_delete=models.CASCADE, default=1)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    


class tblCourse(models.Model):
    course_desc = models.CharField(max_length=255)
    units = models.IntegerField()
    course_comments  = models.TextField(max_length=255)
    phone_number = models.CharField(max_length=12)



class tblStaff(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    fname = models.CharField(max_length=30)
    Iname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    adress = models.ForeignKey(Address, on_delete=models.CASCADE, default=1)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class tblStaff_Department(models.Model):
    course_line = models.IntegerField()


class tblProject_Transaction(models.Model):
    transaction_name = models.CharField(max_length=30)
    stundent_id = models.ForeignKey(tblStudent, on_delete=models.CASCADE, default=1)
    staff_id = models.ForeignKey( tblStaff, on_delete=models.CASCADE, default=1)
    transaction_date = models.DateTimeField(auto_now=True)
  

class tblStudent_Registration(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField(max_length=255)
    registration_date = models.DateTimeField(auto_now=True)

class tblStudent_Reports(models.Model):
    reports_name = models.CharField(max_length=30)
    student_records =  models.ForeignKey(tblStudent_Registration, on_delete=models.CASCADE, default=1)
    transaction_reports =  models.ForeignKey(tblProject_Transaction, on_delete=models.CASCADE, default=1)