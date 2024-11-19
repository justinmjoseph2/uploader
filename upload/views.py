from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .forms import DocumentForm

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'upload/upload_document.html', {'form': form})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'upload/document_list.html', {'documents': documents})

def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    return redirect('document_list')
