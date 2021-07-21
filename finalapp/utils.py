from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template import Context


# def render_to_pdf(path, params):
#     template = get_template(path)
#     html = template.render(params)
#     print('html',html)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     else:
#         return HttpResponse("Error Rendering PDF", status=400)



def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    # pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result, link_callback=links)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


















'''def render_pdf_view(path, data):
    # template_path = 'user_printer.html'
    # context = {'myvar': 'this is your template context'}
    # template = get_template(path)
    # html = template.render(params)
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    # template = get_template(template_path)
    # html = template.render(context)
    template = get_template(path)
    html = template.render(data)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response'''






'''
class render_to_pdf:

    @staticmethod
    def render_to_pdf(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)
'''