from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import get_template
from blog.models import Post, Category
from xhtml2pdf import pisa
from django.http import HttpResponse
import feedparser
from django.template.loader import get_template

def pdf_report_create(request,category_slug,slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    template_path = 'main/detailed_pdf.html'

    context = {'post': post}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="products_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

