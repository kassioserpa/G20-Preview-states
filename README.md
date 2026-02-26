🌐 G20 Preview States — Inteligência Geoestratégica 2026

🔗Veja online: https://kassioserpa.github.io/G20-Preview-states/

O G20 Preview States é um dashboard de inteligência preditiva e visualização geoestratégica desenvolvido para consolidar dados macroeconómicos e institucionais das maiores economias do mundo. Este projeto é uma aplicação prática de conceitos avançados de engenharia de software, visualização de dados 3D e integração de ecossistemas de APIs globais.

🚀 Visão Geral e Propósito

Este projeto nasceu do desafio de converter teoria económica e política em visualização tática imersiva. Ao contrário de dashboards tradicionais de BI, o G20 Preview States utiliza uma interface "Cinematic Hologram" para facilitar a análise de 9 dimensões críticas de risco e oportunidade para investidores e analistas em 2026.

🎯 Diferenciais Estratégicos

Matriz de 9 Dimensões: Análise granular que cobre desde Estabilidade Política e Segurança Jurídica até Vulnerabilidade Externa e Infraestrutura.

Projeção 2026: Dados configurados para refletir cenários futuros (ex: Friedrich Merz como Chanceler na Alemanha).

Experiência Imersiva: Mapa 3D renderizado via WebGL para análise territorial tática.

🛠 Tech Stack & Arquitetura

A escolha das tecnologias foi pautada por performance e escalabilidade:

Backend: Python 3.10 com Flask atuando como camada de orquestração e serviço de API.

Frontend 3D: Three.js para renderização de malhas geográficas extrudadas e animações orbitais.

Estilização: Tailwind CSS com foco em Glassmorphism e responsividade mobile-first.

Data Ingestion: Integração direta com as APIs do World Bank (Macroeconomia) e RestCountries (Geografia).

Padrões de Design Aplicados

Data Mapper Pattern: Normalização de payloads complexos de APIs externas para uma estrutura interna limpa.

LRU Caching: Implementado no backend Python para minimizar o overhead de rede e latência em requisições repetitivas.

Holographic UI Design: Interface baseada em princípios de HUD (Heads-up Display) para reduzir a carga cognitiva.

📊 Dimensões de Análise

O dashboard segmenta a inteligência em três pilares fundamentais:

Pilar

Dimensões Incluídas

I. Institucional

Estabilidade Política, Risco País, Ambiente Jurídico

II. Económico

Performance PIB, Inflação, Mercado Consumidor

III. Estrutural

Infraestrutura/Logística, Comércio Externo, Riscos Globais

🔧 Configuração e Instalação

Pré-requisitos

Python 3.10 ou superior

Pip (Gerenciador de pacotes)

Passo a Passo

# 1. Clonar o repositório
git clone [https://github.com/kassioserpa/G20-Preview-states.git](https://github.com/kassioserpa/G20-Preview-states.git)

# 2. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar o servidor
python app.py


Aceda a http://127.0.0.1:5000 no seu navegador.

📈 Roadmap de Evolução

[ ] Implementação de persistência em base de dados (PostgreSQL) para dossiês personalizados.

[ ] Integração de Web Workers para processamento de geometria 3D em thread separada.

[ ] Feed de notícias em tempo real via Reuters/Bloomberg API integrado ao Ticker.
