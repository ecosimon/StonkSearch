from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import StockProfile

def stocks_view(request):
    ctx = {}
    url_parameter = request.GET.get('q')

    if url_parameter:
        # Remember to find the correct queryset and field lookup. You spent 3hrs debugging for a __ smh
        stocks = StockProfile.objects.filter(title__icontains=url_parameter)
    else:
        stocks = StockProfile.objects.all()

    ctx["stocks"] = stocks

    if request.is_ajax():
        html = render_to_string(
            template_name="stock-results.html",
            context={"stocks": stocks}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)

    return render(request, 'stocksearch.html', context=ctx)

# create add_stock_list function for ajax call.
