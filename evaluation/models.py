from django.db import models

class DifinedLabel(models.Model):
    name = models.CharField(max_length=252)
    common_status = models.BooleanField(default=False)
    sort_order = models.CharField(max_length=3, default=0)

    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length=252)
    sort_order = models.IntegerField()
   
    class Meta:
        ordering = ['sort_order'] 
    
    def __str__(self):
        return  '(' + str(self.sort_order) +') ' + self.name

class Label(models.Model):
    name = models.ForeignKey(DifinedLabel, on_delete=models.PROTECT, related_name='dlabels')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions')
    value = models.CharField(max_length=1, default=0)
    
    def __str__(self):
        return self.name.name
    
class Option(models.Model):
    name = models.CharField(max_length=252)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    next_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null = True, blank = True, related_name='next_question')
    statement = models.TextField(null = True, blank = True,)
    next_step = models.TextField(null = True, blank = True,)
    overall = models.CharField(max_length=1, default=0)
    positive = models.CharField(max_length=1, default=0)
    dont_know = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name + '(' + str(self.question.sort_order) + ')'
    
class LogicalString(models.Model):
    options = models.ManyToManyField(Option)
    text = models.TextField(null = True, blank = True,)
    overall = models.CharField(max_length=1, default=0)
    positive = models.CharField(max_length=1, default=0)
    
    def __str__(self):
        return self.text
    
class Lslabel(models.Model):
    name = models.ForeignKey(DifinedLabel, on_delete=models.PROTECT, related_name='ls_dlabels')
    logical_string = models.ForeignKey(LogicalString, on_delete=models.CASCADE, related_name='logical_strings')
    value = models.CharField(max_length=1, default=0)
    
    def __str__(self):
        return self.name.name
    
    
    
    
class Biofuel(models.Model):
    name = models.CharField(max_length=252)

    def __str__(self):
        return self.name
    
class Evaluator(models.Model):
    name = models.CharField(max_length=252)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=16)
    orgonization = models.CharField(max_length=252)
    biofuel = models.ForeignKey(Biofuel, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Evaluation(models.Model):
    evaluator = models.ForeignKey(Evaluator, on_delete=models.RESTRICT, related_name='eva_evaluator')    
    option = models.ForeignKey(Option, on_delete=models.RESTRICT, related_name='eva_option')
    question = models.ForeignKey(Question, on_delete=models.RESTRICT,null=True, blank=True, related_name='eva_question')
    statement_genarated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.evaluator.name
    
    @property
    def get_question_comment(self):
        eva_comment = EvaComments.objects.filter(question = self.question, evaluator = self.evaluator)
        return eva_comment
        
    
class EvaComments(models.Model):
    evaluator = models.ForeignKey(Evaluator, on_delete=models.RESTRICT, related_name='coment_evaluator')    
    question = models.ForeignKey(Question, on_delete=models.RESTRICT, related_name='comment_question')   
    comments = models.TextField(max_length=600) 
    
    def __str__(self):
        return self.comments
    
    
class EvaLabel(models.Model):
    label = models.ForeignKey(DifinedLabel, on_delete=models.PROTECT, related_name='labels')
    evaluator = models.ForeignKey(Evaluator, on_delete=models.RESTRICT, related_name='evaluators')   
    sort_order = models.CharField(max_length=3, default=0)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.label.name
    
class EvaLebelStatement(models.Model):
    evalebel = models.ForeignKey(EvaLabel, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT, null=True, blank=True)
    option_id = models.CharField(max_length=252, null=True, blank=True)
    statement = models.TextField(blank=True, null=True)
    next_step = models.TextField(blank=True, null=True)
    positive = models.CharField(max_length=1, default=0)
    dont_know = models.BooleanField(default=False)
    assesment = models.BooleanField(default=False)
    evaluator = models.CharField(max_length=250, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.statement
class OptionSet(models.Model):
    option_list = models.CharField(max_length=252, unique = True)
    text = models.TextField()
    positive = models.CharField(max_length=1, default=0)
    overall = models.CharField(max_length=1, default=0)
    ls_id = models.CharField(max_length=252, default=0)
    
    
    def __str__(self):
        return str(self.option_list) + str(self.text)
