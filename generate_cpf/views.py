from django.shortcuts import render
from generate_cpf.validation import Validation
from generate_cpf.generate import Generate

# Create your views here.

def index(request):
    if request.method == 'POST':
        post_generate = request.POST.get('generate')
        post_validate = request.POST.get('validate')

        if post_validate:
            cpf_user = request.POST.get('validate')
            validate = Validation()
            post_validate = validate.validate_cpf(cpf_user)
            context = {
                'post_validate': post_validate,
            }
            return render(request, 'generate_cpf/index.html', context)
        
        if post_generate:
            generate = Generate()
            post_generate = generate.generate_cpf()
            context = {
                'post_generate': post_generate            
            }
            return render(request, 'generate_cpf/index.html', context)

    context = {
                    
    }
    return render(request, 'generate_cpf/index.html', context)