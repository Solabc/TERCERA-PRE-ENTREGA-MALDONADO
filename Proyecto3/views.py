from django.http import HttpResponse

from django.template import Template, Context




def probando_template(request):
    
    nombre= "Soledad"
    apeliido= "Maldonado"
    diccionario= {"nombre": nombre, "apellido": apeliido}
    
    mi_html = open(r"C:\Users\Educacion\Desktop\PROYECTO\Proyecto3\plantillas\templates1.html")
    
    plantilla = Template(mi_html.read())
    
    mi_html.close()
    
    mi_contexto = Context(diccionario)
    
    documento = plantilla.render(mi_contexto)
    
    return HttpResponse(documento)

    

