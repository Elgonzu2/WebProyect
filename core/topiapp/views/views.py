from django.shortcuts import render

def publications_list (request):
	data= {

	}
	return render(request, 'publicaciones/list.html, data')