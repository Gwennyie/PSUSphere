from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student

from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm
from django.urls import reverse_lazy 

# Organization Views
class HomePageView(ListView):
    model = Organization, OrgMember, Student
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationList(ListView): 
     model = Organization 
     context_object_name = 'organization' 
     template_name = 'org_list.html' 
     paginate_by = 5 

class OrganizationCreateView(CreateView): 
     model = Organization 
     form_class = OrganizationForm 
     template_name = 'org_form.html' 
     success_url = reverse_lazy('organization-list') 

class OrganizationUpdateView(UpdateView): 
     model = Organization 
     form_class = OrganizationForm 
     template_name = 'org_form.html' 
     success_url = reverse_lazy('organization-list') 

class OrganizationDeleteView(DeleteView): 
     model = Organization 
     template_name = 'org_del.html' 
     success_url = reverse_lazy('organization-list') 


# OrgMember Views

class OrgMemberList(ListView):
    model = OrgMember
    template_name = "orgmember_list.html"
    paginate_by = 5

class OrgMemberCreate(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy("orgmember-list")


class OrgMemberUpdate(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy("orgmember-list")

class OrgMemberDelete(DeleteView):
    model = OrgMember
    template_name = "orgmember_delete.html"
    success_url = reverse_lazy("orgmember-list")


# Student Views

class StudentList(ListView):
    model = Student
    template_name = "student_list.html"
    paginate_by = 5


class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student-list")


class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student-list")


class StudentDelete(DeleteView):
    model = Student
    template_name = "student_delete.html"
    success_url = reverse_lazy("student-list")
