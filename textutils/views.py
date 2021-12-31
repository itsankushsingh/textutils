from django.http import HttpResponse
from django.shortcuts import render 
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('''<h1>Ankush</h1> <a href="http://www.google.com"><h1>Google</h1></a>''')

# Analyzing Page
def analyze(request):
    #Get The text
    djtext = request.POST.get('text', 'default')
    
    
    # Check CheckBox Value
    removepunc = request.POST.get('removepunc', 'off')
    capall = request.POST.get('capall', 'off')
    newline = request.POST.get('newline', 'off')
    
    
    # Remove Punctuations
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>/?.@#$%^&*_~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
    
    
    # Capitalzed
    if capall =="on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose':'Capitalzed Sentences', 'analyzed_text':analyzed}
        djtext = analyzed
        
    
    # New Line Remove 
    if newline =="on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char
        params = {'purpose':'New Lines Removed ', 'analyzed_text':analyzed}
        

    if (removepunc == "on" and newline == "on" and capall == "on"):
            params['purpose']="Removed Punctuations -" +  " Capitalzed Sentences And" + " New Lines Removed"
    elif (removepunc == "on" and capall == "on"):
            params['purpose']="Removed Punctuations And" +  " Capitalzed Sentences"
    elif (removepunc == "on" and newline == "on"):
            params['purpose']="Removed Punctuations And" +  " New Lines Removed"
    elif (newline == "on" and capall == "on"):
            params['purpose']="Capitalzed Sentences And" + " New Lines Removed"
            
            
    # If Check Box Is Not Checked 
    if (newline !="on" and removepunc !="on" and capall !="on"):
        return render(request, 'error.html')
        
    return(render(request, 'analyze.html',params))
   
    


# About Page
def about(request):
    return render(request, 'about.html')