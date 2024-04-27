from django.shortcuts import render
from django.views.generic import ListView
from .forms import CDRUploadForm
from .models import CallDetailRecord, Customer
from .serializers import CallDetailRecordSerializer
from rest_framework import generics

def upload_cdr(request):
    if request.method == 'POST':
        form = CDRUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cdr_file = request.FILES['cdr_file']
            for line in cdr_file:
                data = line.decode().strip().split(',')
                caller_number, callee_number, call_duration, call_date = data
                
                try:
                    caller_customer = Customer.objects.get(phone_number=caller_number)
                except Customer.DoesNotExist:
                    caller_customer = None
                
                try:
                    callee_customer = Customer.objects.get(phone_number=callee_number)
                except Customer.DoesNotExist:
                    callee_customer = None
                
                cdr = CallDetailRecord(
                    customer=caller_customer,
                    caller_number=caller_number,
                    callee_number=callee_number,
                    call_duration=int(call_duration),
                    call_date=call_date
                )
                cdr.save()
                
            return render(request, 'success.html')
    else:
        form = CDRUploadForm()
    return render(request, 'upload.html', {'form': form})

class CallDetailRecordList(generics.ListAPIView):
    serializer_class = CallDetailRecordSerializer

    def get_queryset(self):
        customer_id = self.request.query_params.get('customer_id')
        if customer_id:
            return CallDetailRecord.objects.filter(customer_id=customer_id)
        else:
            return CallDetailRecord.objects.all()
