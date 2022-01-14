from .models import *
from django.utils import timezone

def claer_evaluator(request):
    evaluator = Evaluator.objects.all()
    try:
        for e in evaluator:
            if e.evaluation_set.count() == 0:
                EvaLabel.objects.filter(evaluator = e,  create_date__gte = timezone.now() + timezone.timedelta(hours=1)).delete() 
                Evaluator.objects.get(id = e.id, create_date__gte = timezone.now() + timezone.timedelta(hours=1)).delete()               
    except Exception as e:
        pass
        
            
    