from flask import Flask
from flask.templating import render_template
import pandas as pd

class Estado:
    def listar(self, ordem):
        data = pd.read_csv('vw_pib_percapita.csv',encoding='UTF-8',delimiter =',')

        data = data[['UF','PIB' ,'PIB_percapita', 'nome']]

        data=data.groupby(['UF']).sum()

        estados = pd.read_csv('estados.csv',encoding='UTF-8',delimiter =',')
        estados.sort_values(by='Estado')

        data['Capitais'] = list(estados['Capital'])
        data.sort_values(by='UF')

        # pobres = (data.sort_values(by='PIB', ascending=ordem).head())

        estados_ordenados = (data.sort_values(by='PIB', ascending=ordem).head())
        return estados_ordenados.to_json(orient='columns', force_ascii=False)
    
    def listarPobres(self):
        return render_template('exibirestados.html', dados_estados = self.listar(True))

    def listarRicos(self):
        return render_template('exibirestados.html', dados_estados = self.listar(False))