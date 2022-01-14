from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib import messages
from django.urls import reverse
from django_xhtml2pdf.utils import generate_pdf



def index(request):    
    print(request.session.items())
    
    try:
        session_evaluator = Evaluator.objects.get(email = request.session['evaluator'])
    except:
        session_evaluator = False
        
        
    
            
    
    
    if  (session_evaluator is False) or ('question' not in request.session):         
        if request.method == "POST":         
            form = EvaluatorForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                orgonization = form.cleaned_data['orgonization']
                biofuel = form.cleaned_data['biofuel']
                
                new_evaluator = Evaluator(name = name, email = email, phone = phone, orgonization = orgonization, biofuel = biofuel )
                new_evaluator.save()               
                
                request.session['evaluator'] = email
                
                first_question = Question.objects.all().order_by('sort_order').first()               
                request.session['question'] = first_question.id
                
                
                
                defined_label = DifinedLabel.objects.all()
                
                
                for dl in defined_label:
                    new_evalabel = EvaLabel(label = dl, evaluator = Evaluator.objects.get(email = email), sort_order=dl.sort_order)
                    new_evalabel.save()
                request.session['option'] = ''
                    
                    
                    
                
                
                return HttpResponseRedirect('/')
                
                
        else:
            form = EvaluatorForm()
            
            
        context = {
        'form': form,
        'evaluator': False,
        }
        return render(request, 'evaluation/index.html', context = context)
    else:
        
        if 'active' not in request.session:
            request.session['active'] = '' 
        question = Question.objects.get(id = request.session['question'])
        options = Option.objects.filter(question = question)   
        evaluator_data = Evaluator.objects.get(email =  request.session['evaluator'])
        try:
            selected_option = Option.objects.get(id = request.session['option'])
        except Exception as e:
            selected_option = ''
        eva_lebels = EvaLabel.objects.filter(evaluator = evaluator_data).order_by('sort_order')
        context = {   
            'question': question,         
            'optns': options,
            'evaluator': True,
            'evaluator_data': evaluator_data,
            'eva_lebels': eva_lebels,
            'selected_option': selected_option,
            'acive': request.session['active']
            
        }
        return render(request, 'evaluation/index.html', context = context)

def option_add(request):
    if request.method == 'POST':
        option_id = request.POST['option_id'] 
        
        comment = request.POST['comment'] 
        question = Question.objects.get(id = request.session['question'])
        evaluator = Evaluator.objects.get(email = request.session['evaluator'])       
        new_eva_comment = EvaComments(evaluator = evaluator, question = question, comments = comment)
        new_eva_comment.save()
        
        request.session['option'] = option_id
        request.session['active'] = 'disabled'
                     
            
        return HttpResponseRedirect('/')   
    
def Genarator(request, selected_option):
    question = selected_option.question
    set_labels = Label.objects.filter(question =  question, value = 1)
            
    for set_label in set_labels: 
        defined_label = DifinedLabel.objects.get(name = set_label.name)     
        eva_label = EvaLabel.objects.get(label = defined_label, evaluator = Evaluator.objects.get(email = request.session['evaluator']))      
        new_evalebel_statement = EvaLebelStatement(evalebel = eva_label, option_id = selected_option.id, statement = selected_option.statement, next_step = selected_option.next_step, question = selected_option.question, positive = selected_option.positive, evaluator =  request.session['evaluator'])
        new_evalebel_statement.save()            
        
    logical_strings = LogicalString.objects.all()
    logical_options = []  
        
    for logical_string in logical_strings:           
        text = logical_string.text          
        sting_options = logical_string.options.all()
        option_list = []            
        for s_o in sting_options:
            option_list.append(str(s_o.id))
        logical_options.append(option_list)
        
        try:
            '''
            edit if any changed
            '''
            option_set = OptionSet.objects.get(option_list = option_list)
            option_set.text = text  
            option_set.save()                          
        except Exception as e:                
            '''
            delete changed to re input
            '''
            lo_except_last = [x for x in logical_options if x != option_list]
            unmatched = [item for item in logical_options if not item in lo_except_last ]               
            try:
                for u in unmatched:
                    OptionSet.objects.get(option_list = u).delete()     
            except Exception as e:
                pass                      
            new_option_set = OptionSet(option_list = option_list, text = text )
            new_option_set.save()       
    
    eva_statement = EvaLebelStatement.objects.filter(evaluator = request.session['evaluator'])
    es_option_id = set()
    for es in eva_statement:           
        es_option_id.add(es.option_id)
    eoi = list(es_option_id) 
    
    defined_common_label = DifinedLabel.objects.get(common_status = True)  
    eva_label_common = EvaLabel.objects.get(label = defined_common_label, evaluator = Evaluator.objects.get(email = request.session['evaluator']))       
    
    if eoi in logical_options:
        try:
            common_statement = OptionSet.objects.get(option_list = eoi)            
            new_evalebel_statement_common = EvaLebelStatement(evalebel = eva_label_common, statement = common_statement.text, evaluator =  request.session['evaluator'])
            new_evalebel_statement_common.save()
        except Exception as e:
            pass
    
    if selected_option.overall == str(1):            
        new_evalebel_statement_common = EvaLebelStatement(evalebel = eva_label_common, statement = selected_option.statement, evaluator =  request.session['evaluator'])
        new_evalebel_statement_common.save()  
    
    
  
    
def option_append(request):    
    request.session['active'] = '' 
    try:  
        selected_option = Option.objects.get(id = request.session['option'])
    except Exception as e:
        messages.warning(request, 'Option didnt Submitted!')
        return HttpResponseRedirect('/') 
    new_evaluation = Evaluation(evaluator = Evaluator.objects.get(email = request.session['evaluator']), option = selected_option, question = Question.objects.get(id = request.session['question'] ) )
    new_evaluation.save() 
         
    try:
        next_question_id = selected_option.next_question.id
        request.session['question'] = next_question_id
        request.session['option'] = ''        
        
        Genarator(request, selected_option)       
        
        return HttpResponseRedirect('/')  
              
    except Exception as e:  
        
        try:  
            selected_option = Option.objects.get(id = request.session['option'])
        except Exception as e:
            messages.warning(request, 'Option didnt Submitted!')
            return HttpResponseRedirect('/')                 
        evaluator =  Evaluator.objects.get(email = request.session['evaluator'])           
        evaluation = Evaluation.objects.filter(evaluator = evaluator)
        for e in evaluation:                
            e.statement_genarated = True
            e.save()  
        Genarator(request, selected_option)                   
        try:
            del request.session['question'] 
            # request.session['evaluator'] = ''             
        except KeyError:
            pass 
         
        return HttpResponseRedirect(reverse('evaluation:report'))  
    


def report(request):
    
    if request.session['evaluator'] == '':
        messages.warning(request, 'Please Fillup The Form To Get Started!')        
        return HttpResponseRedirect('/')
    
    
    
    current_evaluator = Evaluator.objects.get(email = request.session['evaluator'])
    evaluation = Evaluation.objects.filter(evaluator = current_evaluator)
    eva_label = EvaLabel.objects.filter(evaluator = current_evaluator).order_by('sort_order')
    eva_statment = EvaLebelStatement.objects.filter(evaluator = request.session['evaluator'] )
    context = {
        'evaluation': evaluation,
        'current_evaluator': current_evaluator,
        'eva_label': eva_label,
        'eva_statment': eva_statment    
        
    }  
    
    resp = HttpResponse(content_type='application/pdf')
    # resp['Content-Disposition'] = 'attachment; filename=Client_Summary.pdf'
    result = generate_pdf( 'evaluation/report.html', context = context, file_object=resp)
    return result
    
        
        
        
        
    
    
    
