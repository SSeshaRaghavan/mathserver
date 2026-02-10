from django.shortcuts import render

def calculate_gst(request):
    p = 0
    gst = 0
    bill = 0

    if request.method == 'POST':
        p = float(request.POST.get('Price', 0))
        gst = float(request.POST.get('GST', 0))
        bill = p + (p * gst / 100)

    return render(request, 'serverside/math.html', {'bill': bill})