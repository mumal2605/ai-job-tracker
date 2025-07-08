# tracker/views.py
from django.shortcuts import render, redirect
from .models import JobApplication
from .services import extract_skills_from_jd 
from .services import extract_skills_from_jd, extract_skills_from_resume

def home(request):
    if request.method == 'POST':
       
        company_name = request.POST.get('company_name')
        job_description = request.POST.get('job_description')
        resume = request.FILES.get('resume')

        application = JobApplication.objects.create(
            company_name=company_name,
            job_description=job_description,
            resume=resume
        )

        
        jd_skills = extract_skills_from_jd(application.job_description)

        
        application.job_skills = jd_skills
        
        resume_skills = extract_skills_from_resume(application.resume.path)
        application.resume_skills = resume_skills

        if jd_skills and resume_skills:
            matching_skills = set(jd_skills).intersection(set(resume_skills))
            match_score = round((len(matching_skills) / len(jd_skills)) * 100)
        else:
            match_score = 0

        application.match_percentage = match_score

        application.save()

        
        return redirect('results', pk=application.id)
        

    return render(request, 'tracker/home.html')


def results(request, pk):
    application = JobApplication.objects.get(pk=pk)
    jd_skills_set = set(application.job_skills)
    resume_skills_set = set(application.resume_skills)

    matching_skills = jd_skills_set.intersection(resume_skills_set)
    missing_skills = jd_skills_set.difference(resume_skills_set)

    context = {
        'application': application,
        'matching_skills': list(matching_skills),
        'missing_skills': list(missing_skills),
    }
    return render(request, 'tracker/results.html', context)