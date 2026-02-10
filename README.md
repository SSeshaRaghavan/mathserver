# Ex.04 Design a Website for Server Side Processing
## Date:10-02-2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage, using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
views.py
'''
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
'''
urls.py
```
from django.contrib import admin
from django.urls import path
from ss import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calculate_gst, name='calculate_gst'),
]
```
math.html
```
<html>
    <body>
        <h2>GST Calculator</h2>
        <form method="post">
            {% csrf_token %}
            <label>Price</label>
            <input type="text" name="Price" required>
            <label>GST</label>
            <input type="text" name="GST" required>
            <button type="submit">Calculate Bill</button>
        </form>
        <h3>Total Bill: {{bill}}</h3>
    </body>
</html>
```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-02-10 074503.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-02-10 074146.png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
