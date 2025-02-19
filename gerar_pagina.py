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
            <h1 style="font-family: 'Playfair Display', serif; text-align: center; color: white;">Podemos criar o mundo que desejamos</h1>
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

        <section>
            <h2>5. Educação: Construindo um Futuro Melhor</h2>
            <button id="btn_educacao" class="btn" onclick="mostrarSolucoes('solucoes_educacao')">Veja como</button>
            <div id="solucoes_educacao" style="display:none;">
                <p>A educação é a chave para a transformação social e econômica...</p>
                <p><strong>Possíveis soluções:</strong> Expansão do acesso à educação de qualidade para todos, investimentos em formação de professores e infraestrutura escolar.</p>
            </div>
        </section>

        <section>
            <h2>6. Pobreza: Como Erradicar a Pobreza Global</h2>
            <button id="btn_pobreza" class="btn" onclick="mostrarSolucoes('solucoes_pobreza')">Veja como</button>
            <div id="solucoes_pobreza" style="display:none;">
                <p>A pobreza continua sendo uma das maiores barreiras para o bem-estar humano...</p>
                <p><strong>Possíveis soluções:</strong> Melhoria das condições de trabalho, políticas de redistribuição de renda e criação de oportunidades para os mais vulneráveis.</p>
            </div>
        </section>

        <section>
            <h2>7. Justiça: Promovendo um Sistema Justo para Todos</h2>
            <button id="btn_justica" class="btn" onclick="mostrarSolucoes('solucoes_justica')">Veja como</button>
            <div id="solucoes_justica" style="display:none;">
                <p>A justiça social é um pilar essencial para a construção de uma sociedade equilibrada...</p>
                <p><strong>Possíveis soluções:</strong> Reformas no sistema judiciário, combate à corrupção, e políticas de igualdade de direitos.</p>
            </div>
        </section>

        <section>
            <h2>8. Mudanças Climáticas: Combatendo o Aquecimento Global</h2>
            <button id="btn_mudancas_climaticas" class="btn" onclick="mostrarSolucoes('solucoes_mudancas_climaticas')">Veja como</button>
            <div id="solucoes_mudancas_climaticas" style="display:none;">
                <p>As mudanças climáticas são uma ameaça global que afeta o equilíbrio do nosso planeta...</p>
                <p><strong>Possíveis soluções:</strong> Redução de emissões de gases do efeito estufa, uso de energias limpas e adoção de práticas agrícolas sustentáveis.</p>
            </div>
        </section>

        <section>
            <h2>9. Violência: Combatendo a Violência em Todas as Formas</h2>
            <button id="btn_violencia" class="btn" onclick="mostrarSolucoes('solucoes_violencia')">Veja como</button>
            <div id="solucoes_violencia" style="display:none;">
                <p>A violência é uma das maiores ameaças à paz e ao bem-estar das pessoas...</p>
                <p><strong>Possíveis soluções:</strong> Investimentos em educação para a paz, programas de reabilitação de infratores, e promoção de diálogo intercultural.</p>
            </div>
        </section>

        <section>
            <h2>10. Desemprego: Criando Oportunidades para Todos</h2>
            <button id="btn_desemprego" class="btn" onclick="mostrarSolucoes('solucoes_desemprego')">Veja como</button>
            <div id="solucoes_desemprego" style="display:none;">
                <p>O desemprego afeta milhões de pessoas ao redor do mundo, criando um ciclo de dificuldades...</p>
                <p><strong>Possíveis soluções:</strong> Incentivo à criação de novas empresas, apoio a pequenas e médias empresas, e programas de qualificação profissional.</p>
            </div>
        </section>

        <section>
            <h2>11. Corrupção: Como Combater a Corrupção Global</h2>
            <button id="btn_corrupcao" class="btn" onclick="mostrarSolucoes('solucoes_corrupcao')">Veja como</button>
            <div id="solucoes_corrupcao" style="display:none;">
                <p>A corrupção continua sendo um dos maiores obstáculos para o desenvolvimento...</p>
                <p><strong>Possíveis soluções:</strong> Fortalecimento das instituições democráticas, transparência no governo e maior responsabilização dos líderes políticos.</p>
            </div>
        </section>

        <section>
            <h2>12. Acesso à Água: Garantindo Água Potável para Todos</h2>
            <button id="btn_agua" class="btn" onclick="mostrarSolucoes('solucoes_agua')">Veja como</button>
            <div id="solucoes_agua" style="display:none;">
                <p>A água potável é um direito fundamental que ainda não está disponível para todos...</p>
                <p><strong>Possíveis soluções:</strong> Investimentos em infraestrutura hídrica, despoluição de rios e aumento do acesso à água limpa em comunidades carentes.</p>
            </div>
        </section>

        <section>
            <h2>13. Direitos Humanos: Respeitando e Garantindo os Direitos de Todos</h2>
            <button id="btn_direitos_humanos" class="btn" onclick="mostrarSolucoes('solucoes_direitos_humanos')">Veja como</button>
            <div id="solucoes_direitos_humanos" style="display:none;">
                <p>Os direitos humanos são essenciais para garantir a dignidade e a liberdade de todos...</p>
                <p><strong>Possíveis soluções:</strong> Ações afirmativas, promoção de direitos civis, e políticas que combatam a discriminação de qualquer tipo.</p>
            </div>
        </section>

        <section>
            <h2>14. Proteção da Fauna e Flora: Preservando a Vida Selvagem</h2>
            <button id="btn_fauna_florа" class="btn" onclick="mostrarSolucoes('solucoes_fauna_florа')">Veja como</button>
            <div id="solucoes_fauna_florа" style="display:none;">
                <p>A preservação da fauna e da flora é vital para manter o equilíbrio dos ecossistemas...</p>
                <p><strong>Possíveis soluções:</strong> Combate ao desmatamento, criação de reservas naturais e leis mais rigorosas contra caça ilegal.</p>
            </div>
        </section>

        <section>
            <h2>15. Tecnologia: Inovando para um Mundo Melhor</h2>
            <button id="btn_tecnologia" class="btn" onclick="mostrarSolucoes('solucoes_tecnologia')">Veja como</button>
            <div id="solucoes_tecnologia" style="display:none;">
                <p>A tecnologia é uma ferramenta poderosa que pode transformar a sociedade...</p>
                <p><strong>Possíveis soluções:</strong> Desenvolvimento de novas tecnologias para a saúde, educação e energia renovável.</p>
            </div>
        </section>

        <section>
            <h2 style="font-family: 'Playfair Display', serif; color: white;">Estoicismo: A Relação com a Natureza</h2>
            <p style="font-family: 'Serif', sans-serif; color: white;">O Estoicismo nos ensina a viver em harmonia com a natureza, aceitando o que não podemos mudar e nos concentrando no que temos controle...</p>
        </section>

        <footer>
            <h3 style="font-family: 'Playfair Display', serif; font-weight: bold; color: white;">"Nós podemos mudar o mundo e a forma como o vemos, dando mais valor às coisas que realmente merecem."</h3>
        </footer>

    </body>
    </html>
    """
    return html
