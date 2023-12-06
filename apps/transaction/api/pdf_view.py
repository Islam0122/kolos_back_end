from rest_framework.views import APIView
from distributor.api.serializers import DistributorSerializer
from transaction.api.serializers import InvoiceItemsSerializer, ReturnInvoiceItemsSerializer, ReturnInvoiceItemsSerializerPDF
from transaction.models import Invoice, ReturnInvoice
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseServerError
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO


def save_pdf(params: dict):
    try:
        template = get_template('invoice.html')
        html = template.render(params)

        pdf_bytes = BytesIO()

        pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), pdf_bytes)

        if pdf.err:
            raise Exception(f'Error during PDF generation: {pdf.err}')

        pdf_bytes.seek(0)

        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

        return response

    except Exception as e:
        return HttpResponseServerError(f'Internal Server Error: {str(e)}')


class GeneratePdf(APIView):
    def get(self, request, pk):
        invoice = get_object_or_404(Invoice, pk=pk)

        products_invoice_data = InvoiceItemsSerializer(instance=invoice.order_product.all(), many=True).data
        total_amount = sum(item['total_price'] for item in products_invoice_data)
        params = {
            'invoice_data': {
                'identification_number': invoice.identification_number_invoice,
                'distributor': DistributorSerializer(invoice.distributor).data,
                'sale_date': invoice.sale_date,
                'products_invoice': products_invoice_data,
                'total_amount': total_amount,
            }
        }

        response = save_pdf(params)

        if response.status_code == 200:
            return response
        else:
            return Response({'status': response.status_code})


def save_return_pdf(params: dict):
    try:
        template = get_template('return_invoice.html')
        html = template.render(params)

        pdf_bytes = BytesIO()

        pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), pdf_bytes)

        if pdf.err:
            raise Exception(f'Error during PDF generation: {pdf.err}')

        pdf_bytes.seek(0)

        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

        return response

    except Exception as e:
        return HttpResponseServerError(f'Internal Server Error: {str(e)}')



class GenerateReturnPdf(APIView):
    def get(self, request, pk):
        return_invoice = get_object_or_404(ReturnInvoice, pk=pk)

        products_return_invoice_data = ReturnInvoiceItemsSerializerPDF(instance=return_invoice.return_product.all(),
                                                                    many=True).data
        total_amount = sum(item['total_price'] for item in products_return_invoice_data)
        print(products_return_invoice_data)
        params = {
            'return_invoice_data': {
                'distributor': DistributorSerializer(return_invoice.distributor).data,
                'return_date': return_invoice.return_date,
                'products_return_invoice': products_return_invoice_data,
                'total_amount': total_amount,

            }
        }

        response = save_return_pdf(params)

        if response.status_code == 200:
            return response
        else:
            return Response({'status': response.status_code})