import requests
from flask import Flask, render_template, request

app = Flask('PXscrapingnews')

## noticiais mais recentes:
## https://hn.algolia.com/api/v1/search_by_date?tags=story

## noticiais populares:
## https://hn.algolia.com/api/v1/search?tags=story


## Consulta noticia especifia - por iD
## http://hn.algolia.com/api/v1/items/{id}


        # PAGINA HOME ('/')

@app.route('/')
def home():
  
                        # 1 - RECEBE DADOS
    
  order_by = request.args.get("order_by")
  #print(order_by)
  if order_by == 'news':
    url = 'https://hn.algolia.com/api/v1/search_by_date?tags=story'
  else:
    url = 'https://hn.algolia.com/api/v1/search?tags=story'
  
                        # 2 - MANIPULA DADOS

  conteudo_html = requests.get(url)
  converteu_json_pra_python = conteudo_html.json()["hits"]
  
  #resultados = requests.get(url).json()["hits"]
  

                        # 3 - RETORNA DADOS
  
  return render_template('index.html', dic_noticias = converteu_json_pra_python, order_by = order_by)


    
    # 2 - PAGINA NOTICIA CLICADA
    
@app.route('/<id>')
def by_id(id):
  url = f"http://hn.algolia.com/api/v1/items/{id}"
  resultados = requests.get(url).json()
  return render_template('id.html', resultados=resultados)

app.run(host='0.0.0.0')

