from django.db import models
from blog.models import Member, Discipline
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Subject(models.Model):
    subject_name = models.CharField(max_length=200, unique=True)
    related_disciplines = models.ManyToManyField(Discipline, blank=True)
    slug = models.SlugField(default="", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_name)
        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.subject_name)


class Topic(models.Model):
    topic_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, default="", blank=True)
    related_image = models.URLField(blank=True, default="")
    related_subjects = models.ManyToManyField(Subject, blank=True)
    related_disciplines = models.ManyToManyField(Discipline, blank=True)
    related_theory = RichTextField(
        blank=True, null=True, config_name="default")
    slug = models.SlugField(default="", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic_name)
        super(Topic, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.topic_name)


class SubTopic(models.Model):
    subtopic_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500, default="", blank=True)
    related_image = models.URLField(blank=True, default="")
    related_subject = models.ManyToManyField(Subject, blank=True)
    topic = models.ManyToManyField(Topic, blank=True)
    related_theory = RichTextField(
        blank=True, null=True, config_name="default")
    slug = models.SlugField(default="", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subtopic_name)
        super(SubTopic, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.subtopic_name)


class Question(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    question_text = RichTextField(blank=True, null=True, config_name='default')
    option_a = RichTextField(blank=True, null=True, config_name='option')
    option_b = RichTextField(blank=True, null=True, config_name='option')
    option_c = RichTextField(blank=True, null=True, config_name='option')
    option_d = RichTextField(blank=True, null=True, config_name='option')
    correct_choice = models.IntegerField()
    solution = RichTextField(blank=True, null=True,
                             config_name="default",)
    solution_image = models.URLField(blank=True, default="")
    video_solution_url = models.CharField(max_length=1000, blank=True)
    subject = models.ManyToManyField(Subject, blank=True)
    topic = models.ManyToManyField(Topic, blank=True)
    subtopic = models.ManyToManyField(SubTopic, blank=True)
    comma_saperated_tags = models.CharField(
        max_length=500, default="", blank=True)
    slug = models.SlugField(default="", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class MemberSolvedQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    solving_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.member.first_name + self.member.last_name)


class MemberCompletedTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    completing_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.member.first_name + self.member.last_name)
