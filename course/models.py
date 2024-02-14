from django.db import models as m 



class Course(m.Model):
    title = m.CharField(max_length=100)
    description = m.TextField()
    teacher = m.ForeignKey('Teacher', on_delete=m.CASCADE)

    def __str__(self):
        return self.title

class Teacher(m.Model):
    name = m.CharField(max_length=100)
    bio = m.TextField()
    # image = m.CharField(max_length=100)

    def __str__(self):
        return self.name




class Project(m.Model):
    title = m.CharField(max_length=100)
    description = m.TextField()
    link = m.SlugField()

    def __str__(self):
        return self.title
    
class ProjectImages(m.Model):
    image = m.CharField(max_length=100)
    project = m.ForeignKey(Project, on_delete=m.CASCADE)





class Message(m.Model):
    name = m.CharField(max_length=100)
    email = m.EmailField()
    subject = m.CharField(max_length=200)
    message = m.TextField()

    def __str__(self):
        return self.subject

class SocialMedia(m.Model):
    name = m.CharField(max_length=100)
    link = m.URLField()
    icon = m.CharField(max_length=100)

    def __str__(self):
        return self.name

class AboutUs(m.Model):
    title = m.CharField(max_length=100)
    description = m.TextField()

    def __str__(self):
        return self.title