# tracker/models.py
from django.db import models

class JobApplication(models.Model):
    company_name = models.CharField(max_length=100)
    job_description = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    
    job_skills = models.JSONField(null=True, blank=True)
    resume_skills = models.JSONField(null=True, blank=True)
    match_percentage = models.IntegerField(null=True, blank=True)
     
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.id}"