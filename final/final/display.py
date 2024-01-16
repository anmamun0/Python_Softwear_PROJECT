from django.http import HttpResponse
from django.shortcuts import render

def func1(request):
    return render(request, 'homepag.html')

def func2(request):

    v_admin = request.GET.get('fill_admin', 'defalult')
    v_pass = request.GET.get('fill_pass', 'defalute')

    v_text = request.GET.get('our_text', 'default')
    v_box = request.GET.get('our_box', 'defalult')
    v_uper = request.GET.get('our_upper', 'off')
    v_remover = request.GET.get('our_newline_remover', 'off')
    v_our_speech_remover = request.GET.get('our_speech_remover', 'ff')
    v_our_text_counter = request.GET.get('our_text_counter', "off")



    if v_box == 'on' and v_pass == '124': 
        punc = '12345`=-!@$#%^&*()_+][|":;\?|.,><":;67890'
        analyzed =''
        for i in v_text:
            if i not in punc:
                analyzed += i
            dic = {
            'fast' :' Thats fast dic',
            'second': analyzed,
            'theard': v_admin
            }
        return render(request, 'loginpage.html', dic)

    elif(v_uper == 'on'):
        analyzed = ''
        for char in v_text:
            analyzed = analyzed + char.upper()
            dic = {
            'fast' :' Thats fast dic',
            'second': analyzed,
            'theard': v_admin
            }
        return render(request, 'loginpage.html', dic)

    elif(v_remover == 'on'):
        analyzed = ''
        for char in v_text:
            if char != "\n":
                analyzed = analyzed + char
                dic = {
                'fast' :' Thats fast dic',
                'second': analyzed,
                'theard': v_admin
                }
        return render(request, 'loginpage.html', dic)

    elif(v_our_speech_remover == 'on'):
        analyzed = ''
        for index,char in enumerate(v_text):
            if not(v_text[index] ==' ' and v_text[index+1] == " "):
                analyzed = analyzed + char
                dic = {
                'fast' :' Thats fast dic',
                'second': analyzed,
                'theard': v_admin
                }
        return render(request, 'loginpage.html', dic)
        
    elif(v_our_text_counter == 'on'):
        analyzed = 1
        for i , char in enumerate(v_text):
            analyzed += i

            dic = {
                'fast' :' Thats fast dic',
                'second': f'Here ar -{analyzed}- letter',
                'theard': v_admin
                }
        return render(request, 'loginpage.html', dic)
   
   

    else:
        return HttpResponse('Page Error')
