import uuid
from io import BytesIO
from django.template.loader import get_template
from rest_framework.views import APIView
from xhtml2pdf import pisa
from core.settings.local import BASE_DIR
from distributor.api.serializers import DistributorSerializer
from transaction.api.serializers import InvoiceItemsSerializer
from transaction.models import Invoice
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


def save_pdf(params: dict):

    template = get_template('invoice.html')
    html = template.render(params)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response)
    file_name = uuid.uuid4()
    try:
        with open(str(BASE_DIR) + f'/{file_name}.pdf', 'wb+') as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), output)

    except Exception as e:
        print(e)

    if pdf.err:
        return f'Error during PDF generation: {pdf.err}', False
    return file_name, True


class GeneratePdf(APIView):
    def get(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)

        products_invoice_data = InvoiceItemsSerializer(instance=invoice.order_product.all(), many=True).data
        total_amount = sum(item['total_price'] for item in products_invoice_data)
        params = {
            'invoice_data': {
                'distributor': DistributorSerializer(invoice.distributor).data,
                'created_at': invoice.created_at,
                'products_invoice': products_invoice_data,
                'total_amount': total_amount,
            }
        }
        print(params['invoice_data'])

        file_name, status = save_pdf(params)

        if not status:
            return Response({'status': 400})

        return Response({'status': 200, 'sms': 'Successfully created'})
