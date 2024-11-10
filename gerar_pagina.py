def gerar_pagina():
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>O Mundo em que Quero Viver</title>
        <link rel="stylesheet" href="style.css">
        <script>
            function mostrarSolucoes(id) {
                var secao = document.getElementById(id);
                var botao = document.getElementById('btn_' + id);
                
                // Verifica se a solução já está visível, para alternar entre esconder e mostrar
                if (secao.style.display === "none" || secao.style.display === "") {
                    secao.style.display = "block";
                    botao.textContent = "Esconder solução"; // Muda o texto do botão
                } else {
                    secao.style.display = "none";
                    botao.textContent = "Veja como"; // Restaura o texto original
                }
            }
        </script>
    </head>
    <body>
        <header>
            <h1>Podemos criar o mundo que desejamos</h1>
        </header>

        <section>
            <h2>1. Sustentabilidade: Cuidando do Nosso Planeta</h2>
            <button id="btn_sustentabilidade" class="btn" onclick="mostrarSolucoes('solucoes_sustentabilidade')">Veja como</button>
            <div id="solucoes_sustentabilidade" style="display:none;">
                <p>A sustentabilidade é fundamental para garantir que as gerações futuras tenham acesso a recursos naturais suficientes para viver bem...</p>
                <p><strong>Possíveis soluções:</strong> Implementação de políticas de reciclagem mais eficazes, uso de energias renováveis, redução do consumo de plásticos, entre outras.</p>
            </div>
        </section>

        <section>
            <h2>2. Desigualdade Social: Como Podemos Reduzir</h2>
            <button id="btn_desigualdade" class="btn" onclick="mostrarSolucoes('solucoes_desigualdade')">Veja como</button>
            <div id="solucoes_desigualdade" style="display:none;">
                <p>A desigualdade social é um problema crítico que afeta milhões de pessoas ao redor do mundo...</p>
                <p><strong>Possíveis soluções:</strong> Aumento de investimentos em educação, programas de redistribuição de riqueza, e políticas públicas de inclusão social.</p>
            </div>
        </section>

        <section>
            <h2>3. Saúde: Garantindo Bem-Estar para Todos</h2>
            <button id="btn_saude" class="btn" onclick="mostrarSolucoes('solucoes_saude')">Veja como</button>
            <div id="solucoes_saude" style="display:none;">
                <p>A saúde é um direito básico e essencial para todos...</p>
                <p><strong>Possíveis soluções:</strong> Acesso universal à saúde de qualidade, programas de prevenção e políticas de saúde pública mais eficazes.</p>
            </div>
        </section>

        <section>
            <h2>4. Fome Mundial: Como Acabar com a Fome no Mundo</h2>
            <button id="btn_fome" class="btn" onclick="mostrarSolucoes('solucoes_fome')">Veja como</button>
            <div id="solucoes_fome" style="display:none;">
                <p>A fome é um dos maiores desafios da humanidade, afetando milhões de pessoas...</p>
                <p><strong>Possíveis soluções:</strong> Melhor distribuição de alimentos, redução de desperdício de comida, apoio a programas de alimentação sustentável.</p>
            </div>
        </section>

        <footer>
            <p>Juntos podemos criar um futuro mais justo e sustentável para todos.</p>
        </footer>
    </body>
    </html>
    """
    # Criar e salvar o arquivo HTML
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(html)
    print("Página HTML gerada com sucesso!")

# Executar a função para gerar a página
gerar_pagina()
