import pdfkit as pdf

def gerar_checklist():
    """Gerar o pdf do checklist baseado na tela CheckList

    Args:
        switch_horario (MDSwitch): inativo = abertura, ativo = fechamento
        check_container (MDGridLayout): Container dos checkbox e labels correspondentes
    """
            
    options = {
        'page-size': 'A4',
        'margin-top': '0.60in',
        'margin-right': '0.50in',
        'margin-bottom': '0.60in',
        'margin-left': '0.50in',
        'enable-local-file-access': '',
    }
    
    html = f'''
    <!DOCTYPE html>
    <html lang="pt-br">
        <head>
            <meta http-equiv="content-type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <div class="main">
            <div class="container">
            <div class="logo"> <img src="logo_color.png" alt=""> </div>
            <div class="title">
                <h1>Check List</h1>
            </div>
            <div class="data">
                <div class="nome"> <label for="nome">Nome:</label></div>
                <div class="cargo"> <label for="cargo">Cargo:</label></div>
                <div class="matricula"> <label for="matricula">Matricula:</label></div>
            </div>
            <div class="checkers">
                <div class="check">
                    <img src="unchecked.png">
                    <label for="paneis1">Lorem ipsum dolor sit amet consectetur 
                    adipisicing elit.</label>
                </div>
                <div class="check">
                    <img src="unchecked.png">
                    <label for="paneis1">Lorem ipsum dolor sit amet consectetur 
                    adipisicing elit.</label>
                </div>
                <div class="check">
                    <img src="unchecked.png">
                    <label for="paneis1">Paneis </label>
                </div>
                <div class="check">
                    <img src="unchecked.png">
                    <label for="paneis1">Paneis </label>
                </div>
                <div class="check">
                    <img src="unchecked.png">
                    <label for="paneis1">Paneis </label>
                </div>
                <div class="check">
                    <img src="unchecked.png">
                    <label for="paneis1">Paneis </label>
                </div>
            </div>
            <div class="obs">
                <p>Obs:</p>
                <hr>
                <hr>
                <hr>
                <hr>
            </div>
            <div class="firma">
                <div class="verified">
                <label for="verified">Verificado por:</label>
                <input type="text" name="verified" id="">
            </div>
            <div class="asignatura">
                <label for="asignatura">Gerencia:</label>
                <input type="text" name="assinatura" id="">
            </div>
            </div>
            <div class="footer">
                <footer>Fortaleza - CE 01 / 12 / 2023</footer>
            </div>
            </div>
            </div>
        </body>
    </html>
    '''
    pdf.from_string(html, output_path='Check-List.pdf', css='recursos/html/style.css', options=options)
    
gerar_checklist()