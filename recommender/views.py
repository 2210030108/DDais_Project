# Inside your views.py
from django.shortcuts import render
from .models import WashingMachine
from .forms import WashingMachineFilterForm


def washing_machine_list(request):
    washing_machines = WashingMachine.objects.all()
    return render(request, 'washing_machine_list.html', {'washing_machines': washing_machines})


from django.db.models import Q


def washing_machine_filter(request):
    washing_machines = WashingMachine.objects.all()

    if request.method == 'POST':
        form = WashingMachineFilterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('product_name')
            min_rating = form.cleaned_data.get('ratings')
            price_range = form.cleaned_data.get('price_range')

            # Start with all washing machines
            queryset = WashingMachine.objects.all()

            # Apply filters based on user input
            if name:
                queryset = queryset.filter(product_name__icontains=name)

            if min_rating:
                queryset = queryset.filter(ratings__gte=min_rating)

            if price_range == '0':
                # No filtering for "Any Price" option
                pass
            else:
                # Extract min_price and max_price based on selected option
                price_range = int(price_range)
                if price_range == 10000:
                    min_price = 0
                    max_price = 10000
                elif price_range == 20000:
                    min_price = 10000
                    max_price = 20000
                elif price_range == 30000:
                    min_price = 20000
                    max_price = 30000
                else:
                    min_price = 30000
                    max_price = 32000

                # Filter queryset based on the extracted min_price and max_price
                queryset = queryset.filter(price__gte=min_price, price__lt=max_price)

            # Now, you have filtered queryset based on all criteria
            washing_machines = queryset
    else:
        form = WashingMachineFilterForm()

    return render(request, 'washing_machine_filter.html', {'form': form, 'washing_machines': washing_machines})
