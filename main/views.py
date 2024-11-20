# from django.http import HttpResponse
# from django.shortcuts import render
# import wikipedia
# # Create your views here.

# def wiki_search(request):
#     result={}
#     if request.method=='POST':
#         search=request.POST['search']
#         try:
#             result={
#                 'search':wikipedia.summary(search)
#             }
#         except:
#             return HttpResponse("Wrong Input")
#         return render(request,'index.html',result)
#     return render(request,"index.html")


from django.http import HttpResponse
from django.shortcuts import render
import wikipedia
from bs4 import BeautifulSoup
from translate import Translator
# Patch the wikipedia library to specify the 'lxml' parser
wikipedia.BeautifulSoup = lambda html: BeautifulSoup(html, features="lxml")
import wikipediaapi

def chunk_text(text, max_length=500):
    """Splits text into chunks of max_length characters."""
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(' '.join(current_chunk + [word])) <= max_length:
            current_chunk.append(word)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks


def wiki_search(request):
    result = None
    translated_result = None
    wiki_wiki = wikipediaapi.Wikipedia('english')  # Use English Wikipedia

    if request.method == 'POST':
        if 'search' in request.POST:
            search = request.POST.get('search', '').strip()
            if not search:
                return HttpResponse("Search query cannot be empty.")
            page = wiki_wiki.page(search)
            if page.exists():
                result = page.summary
            else:
                return HttpResponse("No matching Wikipedia page found.")
        
        if 'translate' in request.POST:
            text_to_translate = request.POST.get('text_to_translate', '')
            target_language = request.POST.get('target_language', 'en')
            try:
                chunks = chunk_text(text_to_translate)
                translator = Translator(to_lang=target_language)
                translated_chunks = [translator.translate(chunk) for chunk in chunks]
                translated_result = ' '.join(translated_chunks)
            except Exception as e:
                return HttpResponse(f"An error occurred during translation: {str(e)}")

    return render(request, 'index.html', {
        'search': result,
        'translated_result': translated_result
    })