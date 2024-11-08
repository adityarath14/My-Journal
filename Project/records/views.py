from django.shortcuts import render,get_object_or_404, redirect
from .models import Record
from .forms import RecordForm
from django.contrib import messages
# Create your views here.
def create_record(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created successfully!')
            return redirect('record_list')
    else:
        form = RecordForm()
    return render(request, 'create_record.html', {'form': form})

# List view
def record_list(request):
    records = Record.objects.all()
    return render(request, 'record_list.html', {'records': records})

# Update view
def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully!')
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'update_record.html', {'form': form})

# Delete view
def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == "POST":
        record.delete()
        messages.success(request, 'Record deleted successfully!')
        return redirect('record_list')
    return render(request, 'delete_record.html', {'record': record})