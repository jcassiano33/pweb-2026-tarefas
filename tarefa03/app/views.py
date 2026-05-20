from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def usuarios(request):
    lista_users = [
        {"nome": "Kaio Cruz", "matricula": 111, "idade": 17, "cidade": "São Paulo do Potengi"},
        {"nome": "Big Jhow", "matricula": 222, "idade": 15, "cidade": "Lagoa de Velhos"},
        {"nome": "Xexeu", "matricula": 333, "idade": 17, "cidade": "Bom Jesus"},
        {"nome": "Cassioto", "matricula": 444, "idade": 17, "cidade": "São Tomé"},
        {"nome": "Juninho", "matricula": 555, "idade": 18, "cidade": "São Tomé"},
    ]

    context = {
        "usuarios": lista_users,
    }
    
    return render(request, "app/usuarios.html", context)