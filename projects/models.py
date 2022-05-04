from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.TextField(
        default="https://d2slcw3kip6qmk.cloudfront.net/marketing/blog/2019Q1/why-pm-is-important/why-is-project-management-important-header@2x.png"
    )
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title

class Upload(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title



# class MyData(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     technology = models.CharField(max_length=20)
#     image = models.FilePathField(path="/img")
#     date_created = models.DateTimeField(auto_now_add=True)