from flask import Flask, render_template, render_template_string

app = Flask(__name__)

# Página HTML principal com botões para redirecionamento
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Controle de Problemas Urbanos</title>
</head>
<body>
    <div style="display: flex;">
        <div style="flex: 1;">
            <h3>Categorias</h3>
            <button onclick="window.location.href='/asfalto'">Asfalto</button><br>
            <button onclick="window.location.href='/lixo'">Lixo</button><br>
            <button onclick="window.location.href='/bueiro'">Bueiro</button><br>
            <button onclick="window.location.href='/inflacao'">Inflação</button><br>
            <button onclick="window.location.href='/obstrucao'">Obstrução de via</button><br>
            <button onclick="window.location.href='/matagal'">Matagal</button><br>
            <button onclick="window.location.href='/sinalizacao'">Sinalização</button>
        </div>
        <div style="flex: 2; padding-left: 20px;">
            <!-- Usar iframe diretamente para exibir o vídeo -->
            <iframe src="http://192.168.1.3:8080/video" width="500" height="400" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            <p>Problemas relatados: 208</p>
        </div>
    </div>
</body>
</html>
"""

# Rota para a página inicial
@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

# Rotas para cada categoria, renderizando os arquivos em /templates

# @app.route('/asfalto')
# def asfalto():
#     return render_template('asfalto.html')
@app.route('/asfalto')
def asfalto():
    issues = [
        {"image_url": "/static/images/asfalto1.jpg", "address": "Rua Machado de Assis, 334, Vila Brasilia", "date": "20/11/2024", "status": "Pendente", "action": "Resolver"},
        {"image_url": "/static/images/asfalto2.jpg", "address": "Avenida Central, 108, Centro", "date": "22/11/2024", "status": "Em andamento", "action": "Acompanhar"},
        {"image_url": "/static/images/asfalto3.jpg", "address": "Rua D, 456, Jardim São Paulo", "date": "25/11/2024", "status": "Resolvido", "action": "Ver detalhes"},
    ]
    
    resolved = 30
    pending = 70
    in_progress = 12

    return render_template('asfalto.html', issues=issues, resolved=resolved, pending=pending, in_progress=in_progress)



# @app.route('/lixo')
# def lixo():
#     return render_template('lixo.html')
@app.route('/lixo')
def lixo():
    issues = [
        {"image_url": "/static/images/lixo1.jpg", "address": "Rua C, 234, Bairro das Flores", "date": "15/11/2024", "status": "Pendente", "action": "Resolver"},
        {"image_url": "/static/images/lixo2.jpg", "address": "Avenida das Árvores, 512, Jardim das Palmeiras", "date": "18/11/2024", "status": "Em andamento", "action": "Acompanhar"},
        {"image_url": "/static/images/lixo3.jpg", "address": "Rua E, 987, Parque das Águas", "date": "20/11/2024", "status": "Resolvido", "action": "Ver detalhes"},
    ]
    
    resolved = 50
    pending = 40
    in_progress = 8

    return render_template('lixo.html', issues=issues, resolved=resolved, pending=pending, in_progress=in_progress)



# @app.route('/bueiro')
# def bueiro():
#     return render_template('bueiro.html')
@app.route('/bueiro')
def bueiro():
    issues = [
        {"image_url": "/static/images/bueiro1.jpg", "address": "Rua das Palmeiras, 245, Vila Verde", "date": "10/11/2024", "status": "Pendente", "action": "Resolver"},
        {"image_url": "/static/images/bueiro2.jpg", "address": "Avenida Rio Branco, 350, Centro", "date": "13/11/2024", "status": "Em andamento", "action": "Acompanhar"},
        {"image_url": "/static/images/bueiro3.jpg", "address": "Rua São Jorge, 1000, Bairro do Sol", "date": "17/11/2024", "status": "Resolvido", "action": "Ver detalhes"},
    ]
    
    resolved = 25
    pending = 50
    in_progress = 5

    return render_template('bueiro.html', issues=issues, resolved=resolved, pending=pending, in_progress=in_progress)


# @app.route('/inflacao')
# def inflacao():
#     return render_template('inflacao.html')
@app.route('/inflacao')
def inflacao():
    issues = [
        {"image_url": "/static/images/inflacao1.jpg", "address": "Rua da Liberdade, 310, Vila Nova", "date": "30/10/2024", "status": "Pendente", "action": "Resolver"},
        {"image_url": "/static/images/inflacao2.jpg", "address": "Avenida Brasil, 220, Centro", "date": "05/11/2024", "status": "Em andamento", "action": "Acompanhar"},
        {"image_url": "/static/images/inflacao3.jpg", "address": "Rua das Margaridas, 710, Jardim das Flores", "date": "12/11/2024", "status": "Resolvido", "action": "Ver detalhes"},
    ]
    
    resolved = 40
    pending = 35
    in_progress = 15

    return render_template('inflacao.html', issues=issues, resolved=resolved, pending=pending, in_progress=in_progress)



# @app.route('/obstrucao')
# def obstrucao():
#     return render_template('obstrucao.html')
@app.route('/obstrucao')
def obstrucao():
    issues = [
        {"image_url": "/static/images/obstrucao1.jpg", "address": "Rua da Paz, 500, Bairro Nova Esperança", "date": "22/10/2024", "status": "Pendente", "action": "Resolver"},
        {"image_url": "/static/images/obstrucao2.jpg", "address": "Avenida São Paulo, 1020, Centro", "date": "25/10/2024", "status": "Em andamento", "action": "Acompanhar"},
        {"image_url": "/static/images/obstrucao3.jpg", "address": "Rua das Américas, 750, Jardim Botânico", "date": "28/10/2024", "status": "Resolvido", "action": "Ver detalhes"},
    ]
    
    resolved = 30
    pending = 50
    in_progress = 10

    return render_template('obstrucao.html', issues=issues, resolved=resolved, pending=pending, in_progress=in_progress)



# @app.route('/matagal')
# def matagal():
#     return render_template('matagal.html')
# Dados simulados para a página de Matagal
@app.route('/matagal')
def matagal():
    issues = [
        {"image_url": "/static/images/matagal1.jpg", "address": "Rua do Sol, 500, Jardim do Sol", "date": "01/10/2024", "status": "Pendente", "action": "Resolver"},
        {"image_url": "/static/images/matagal2.jpg", "address": "Avenida Amazonas, 1023, Vila Nova", "date": "05/10/2024", "status": "Em andamento", "action": "Acompanhar"},
        {"image_url": "/static/images/matagal3.jpg", "address": "Rua dos Lírios, 200, Bairro das Flores", "date": "10/10/2024", "status": "Resolvido", "action": "Ver detalhes"},
    ]
    
    resolved = 20
    pending = 30
    in_progress = 10

    return render_template('matagal.html', issues=issues, resolved=resolved, pending=pending, in_progress=in_progress)



# @app.route('/sinalizacao')
# def sinalizacao():
#     return render_template('sinalizacao.html')
@app.route('/sinalizacao')
def sinalizacao():
    issues = [
        {"image_url": "/static/images/sinalizacao1.jpg", "address": "Rua São José, 45, Bairro Centro", "date": "10/10/2024", "status": "Pendente", "action": "Resolver"},
        {"image_url": "/static/images/sinalizacao2.jpg", "address": "Avenida Presidente Vargas, 123, Zona Norte", "date": "15/10/2024", "status": "Em andamento", "action": "Acompanhar"},
        {"image_url": "/static/images/sinalizacao3.jpg", "address": "Rua do Comércio, 500, Centro", "date": "20/10/2024", "status": "Resolvido", "action": "Ver detalhes"},
    ]
    
    resolved = 25
    pending = 40
    in_progress = 10

    return render_template('sinalizacao.html', issues=issues, resolved=resolved, pending=pending, in_progress=in_progress)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
