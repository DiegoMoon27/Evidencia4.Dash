import pandas as pd
import dash
from dash import dcc # Dash Core Components
from dash import html # Hyper Text Markup Language
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc
import datetime

### Bases de datos

df_entidad= pd.read_csv("downloads/Ors_entidad.csv", low_memory=False)

df_emision= pd.read_csv("downloads/Emision.csv", low_memory=False)

df_comisiones= pd.read_csv("downloads/Comisiones.csv", low_memory=False)

df_siniestros= pd.read_csv("downloads/Siniestros.csv", low_memory=False)

### Regex

df_emision["NUMERO DE ASEGURADOS"]= pd.to_numeric(df_emision["NUMERO DE ASEGURADOS"].replace("[^0-9\.-]",'', regex=True ))
df_emision["EDAD"]= pd.to_numeric(df_emision["EDAD"].replace("[^0-9\.-]",'', regex=True ))
df_emision["PRIMA EMITIDA"]= pd.to_numeric(df_emision["PRIMA EMITIDA"].replace("[^0-9\.-]",'', regex=True ))
df_emision["SUMA ASEGURADA"]= pd.to_numeric(df_emision["SUMA ASEGURADA"].replace("[^0-9\.-]",'', regex=True ))

df_comisiones["NUMERO DE ASEGURADOS"]= pd.to_numeric(df_emision["NUMERO DE ASEGURADOS"].replace("[^0-9\.-]",'', regex=True ))
df_comisiones["EDAD"]= pd.to_numeric(df_emision["EDAD"].replace("[^0-9\.-]",'', regex=True ))
df_comisiones["PRIMA EMITIDA"]= pd.to_numeric(df_emision["PRIMA EMITIDA"].replace("[^0-9\.-]",'', regex=True ))
df_comisiones["SUMA ASEGURADA"]= pd.to_numeric(df_emision["SUMA ASEGURADA"].replace("[^0-9\.-]",'', regex=True ))

df_siniestros["NUMERO DE ASEGURADOS"]= pd.to_numeric(df_emision["NUMERO DE ASEGURADOS"].replace("[^0-9\.-]",'', regex=True ))
df_siniestros["EDAD"]= pd.to_numeric(df_emision["EDAD"].replace("[^0-9\.-]",'', regex=True ))
df_siniestros["PRIMA EMITIDA"]= pd.to_numeric(df_emision["PRIMA EMITIDA"].replace("[^0-9\.-]",'', regex=True ))
df_siniestros["SUMA ASEGURADA"]= pd.to_numeric(df_emision["SUMA ASEGURADA"].replace("[^0-9\.-]",'', regex=True ))

df_entidad["NUMERO DE ASEGURADOS"]= pd.to_numeric(df_emision["NUMERO DE ASEGURADOS"].replace("[^0-9\.-]",'', regex=True ))
df_entidad["EDAD"]= pd.to_numeric(df_emision["EDAD"].replace("[^0-9\.-]",'', regex=True ))
df_entidad["PRIMA EMITIDA"]= pd.to_numeric(df_emision["PRIMA EMITIDA"].replace("[^0-9\.-]",'', regex=True ))
df_entidad["SUMA ASEGURADA"]= pd.to_numeric(df_emision["SUMA ASEGURADA"].replace("[^0-9\.-]",'', regex=True ))

### Cambiar valores mal escritos

def cambiar_datos(df, columna, valor_antiguo, valor_nuevo, inplace=False):
    if inplace:
        df[columna].replace(valor_antiguo, valor_nuevo, inplace=True)
    else:
        df = df.copy()
        df[columna] = df[columna].replace(valor_antiguo, valor_nuevo)
    return df

df_comisiones = cambiar_datos(df_comisiones, 'ENTIDAD', 'QuerŽtaro', 'Querétaro', inplace=True)
df_comisiones = cambiar_datos(df_comisiones, 'ENTIDAD', 'Ciudad de MŽxico', 'Ciudad de México', inplace=True)
df_comisiones = cambiar_datos(df_comisiones, 'ENTIDAD', 'Michoac‡n', 'Michoacán', inplace=True)
df_comisiones = cambiar_datos(df_comisiones, 'ENTIDAD', 'San Luis Potos’', 'San Luis Potosí', inplace=True)
df_comisiones = cambiar_datos(df_comisiones, 'ENTIDAD', 'Yucat‡n', 'Yucatán', inplace=True)
df_comisiones = cambiar_datos(df_comisiones, 'FORMA DE VENTA', 'Agentes Persona F’sica', 'Agentes persona física', inplace=True)
df_comisiones = cambiar_datos(df_comisiones, 'FORMA DE VENTA', 'Descuento por N—mina', 'Descuento por nómina', inplace=True)
df_comisiones = cambiar_datos(df_comisiones, 'FORMA DE VENTA', 'M—dulos de Venta', 'Módulos de venta', inplace=True)

df_siniestros = cambiar_datos(df_siniestros, 'ENTIDAD', 'QuerŽtaro', 'Querétaro', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'ENTIDAD', 'Ciudad de MŽxico', 'Ciudad de México', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'ENTIDAD', 'Michoac‡n', 'Michoacán', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'ENTIDAD', 'San Luis Potos’', 'San Luis Potosí', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'ENTIDAD', 'Yucat‡n', 'Yucatán', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'COBERTURA', 'Exenci—n de pago de prima', 'Exhibición de pago de prima', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'COBERTURA', 'Ahorro / inversi—n', 'Ahorro/Inversión', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'COBERTURA', 'Muerte accidental (Doble indemnizaci—n)', 'Muerte accidental (Doble indemnización)', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'COBERTURA', 'Muerte colectiva (Triple indemnizaci—n)', 'Muerte colectiva (Triple indemnización)', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'COBERTURA', 'Devoluci—n de prima', 'Devolución de prima', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'COBERTURA', 'PŽrdidas Org‡nicas', 'Pérdidas orgánicas', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'CAUSA DEL SINIESTRO', 'DIABETES MELLITUS ASOCIADA CON DESNUTRICIîN, CON CETOACIDOSIS', 'DIABETES MELLITUS ASOCIADA CON DESNUTRICIÓN, CON CETOACIDOSIS', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'CAUSA DEL SINIESTRO', 'ESTADO DE MAL EPILƒPTICO DE TIPO NO ESPECIFICADO', 'ESTADO DE MAL EPILÉPTICO DE TIPO NO ESPECIFICADO', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'CAUSA DEL SINIESTRO', 'EVENTO NO ESPECIFICADO, DE INTENCIîN NO DETERMINADA, VIVIENDA', 'EVENTO NO ESPECIFICADO, DE INTENCIÓN NO DETERMINADA, VIVIENDA', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'CAUSA DEL SINIESTRO', 'HIPERTENSIîN ESENCIAL (PRIMARIA)', 'HIPERTENSIÓN ESENCIAL (PRIMARIA)', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'CAUSA DEL SINIESTRO', 'NEUMONêA, NO ESPECIFICADA', 'NEUMONÍA, NO ESPECIFICADA', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'CAUSA DEL SINIESTRO', 'BRONCONEUMONêA, NO ESPECIFICADA', 'BRONCONEUMONÍA, NO ESPECIFICADA', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'CAUSA DEL SINIESTRO', 'CHOQUE CARDIOGƒNICO', 'CHOQUE CARDIOGÓNICO', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'CAUSA DEL SINIESTRO', 'ADENOVIRUS COMO CAUSA DE ENFERMEDADES CLASIFICADAS EN OTROS CAPêTULOS', 'ADENOVIRUS', inplace=True)

df_emision = cambiar_datos(df_emision, 'COBERTURA', 'Exenci—n de pago de prima', 'Exhibición de pago de prima', inplace=True)
df_emision = cambiar_datos(df_emision, 'COBERTURA', 'Ahorro / inversi—n', 'Ahorro/Inversión', inplace=True)
df_emision = cambiar_datos(df_emision, 'COBERTURA', 'Muerte accidental (Doble indemnizaci—n)', 'Muerte accidental (Doble indemnización)', inplace=True)
df_emision = cambiar_datos(df_emision, 'COBERTURA', 'Muerte colectiva (Triple indemnizaci—n)', 'Muerte colectiva (Triple indemnización)', inplace=True)
df_emision = cambiar_datos(df_emision, 'COBERTURA', 'PŽrdidas Org‡nicas', 'Pérdidas orgánicas', inplace=True)
df_emision = cambiar_datos(df_emision, 'COBERTURA', 'Devoluci—n de prima', 'Devolución de prima', inplace=True)
df_emision = cambiar_datos(df_emision, 'FORMA DE VENTA', 'Agentes Persona F’sica', 'Agentes persona física', inplace=True)
df_emision = cambiar_datos(df_emision, 'FORMA DE VENTA', 'Descuento por N—mina', 'Descuento por nómina', inplace=True)
df_emision = cambiar_datos(df_emision, 'FORMA DE VENTA', 'M—dulos de Venta', 'Módulos de venta', inplace=True)

df_entidad = cambiar_datos(df_entidad, 'ENTIDAD', 'QuerÃ©taro', 'Querétaro', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'ENTIDAD', 'Estado de MÃ©xico', 'Estado de México', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'ENTIDAD', 'MichoacÃ¡n', 'Michoacán', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'ENTIDAD', 'San Luis PotosÃ', 'San Luis Potosí', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'ENTIDAD', 'YucatÃ¡n', 'Yucatán', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'ENTIDAD', 'Nuevo LeÃ³n', 'Nuevo León', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'RAMO', 'Diversos MiscelÃ¡neos', 'Diversos miscelaneos', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'RAMO', 'Diversos Ramos TÃ©cnicos', 'Diversos ramos técnicos', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'RAMO', 'FenÃ³menos HidrometeorolÃ³gicos', 'Fenómenos hidrometerológicos', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'RAMO', 'AutomÃ³viles', 'Automóviles', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'RAMO', 'Gastos MÃ©dicos', 'Gastos médicos', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'RAMO', 'AgrÃ­cola', 'Agrícola', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'RAMO', 'CrÃ©dito', 'Crédito', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'RAMO', 'CrÃ©dito a la Vivienda', 'Crédito a la vivienda', inplace=True)
df_entidad = cambiar_datos(df_entidad, 'RAMO', 'GarantÃ­a Financiera', 'Garantía financiera', inplace=True)

### Piramide poblacional

df_grouped = df_emision.groupby(['EDAD', 'SEXO']).size().reset_index(name='POBLACION')

fig1 = px.bar(df_grouped, x='EDAD', y='POBLACION', color='SEXO', barmode='relative', 
             category_orders={'EDAD': sorted(df_grouped['EDAD'].unique())[::-1]})
fig1.update_layout(title='Pirámide poblacional de edad y sexo', xaxis_title='Edad', yaxis_title='Población')

### Distribución por Entidad Federativa
fig2 = px.histogram(df_comisiones, x="ENTIDAD", title="Usuarios por Entidad Federativa", color="ENTIDAD")

fig2.update_yaxes(title_text='Usuarios')
fig2.update_layout(yaxis=dict(title='Usuarios'))


### Top 15 de siniestros 
causas_count = df_siniestros["CAUSA DEL SINIESTRO"].value_counts().nlargest(15)
df_causas = pd.DataFrame({'Causa': causas_count.index, 'Count': causas_count.values})
fig3 = px.bar(df_causas, x='Causa', y='Count', color='Causa', title="Top 15 siniestros")
fig3.update_xaxes(showticklabels=False)

### Distribución por cobertura
fig4 = px.histogram(df_siniestros, x="COBERTURA", title="Distribución de tipos de cobertura",
                    color="COBERTURA")

### Histórico prima emitida
df_entidad['FECHA DE CORTE'] = pd.to_datetime(df_entidad['FECHA DE CORTE'], format='%d/%m/%Y')
def create_prima_emitida_graph(start_date, end_date):
    filtered_df = df_entidad[(df_entidad['FECHA DE CORTE'] >= start_date) & (df_entidad['FECHA DE CORTE'] <= end_date)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['FECHA DE CORTE'], y=filtered_df['PRIMA EMITIDA'], mode='lines', name='Prima Emitida'))
    fig.update_layout(title='Histórico de Prima Emitida', xaxis_title='Fecha de Corte', yaxis_title='Prima Emitida')
    return fig

### Modalidad de póliza
modalidades = df_comisiones["MODALIDAD DE LA POLIZA"].value_counts()
fig5 = px.pie(names=modalidades.index, values=modalidades, title="Distribución de Modalidades de Póliza")

### Tipos de cobertura más solicitados por cada entidad federativa
df_counts = df_siniestros.groupby(['ENTIDAD', 'COBERTURA']).size().reset_index(name='COUNT')


fig6 = px.bar(df_counts, x='ENTIDAD', y='COUNT', color='COBERTURA',
             title='Usuarios por Entidad Federativa y Cobertura',
             labels={'COUNT': 'Usuarios', 'ENTIDAD': 'Entidad Federativa'})


fig6.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(label=cobertura, method='update',
                     args=[{'visible': df_counts['COBERTURA'] == cobertura},
                           {'title': f'Usuarios por Entidad Federativa y Cobertura ({cobertura})'}])
                for cobertura in df_counts['COBERTURA'].unique()
            ],
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0.1,
            xanchor='left',
            y=1.1,
            yanchor='top'
        ),
        dict(
            buttons=[
                dict(label=entidad, method='update',
                     args=[{'visible': df_counts['ENTIDAD'] == entidad},
                           {'title': f'Usuarios por Entidad Federativa y Cobertura ({entidad})'}])
                for entidad in df_counts['ENTIDAD'].unique()
            ],
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0.4,
            xanchor='left',
            y=1.1,
            yanchor='top'
        )
    ]
)

### Siniestros por Entidad
df_causas = df_siniestros['CAUSA DEL SINIESTRO'].value_counts().reset_index()
df_causas.columns = ['CAUSA DEL SINIESTRO', 'COUNT']
top_15_causas = df_causas.nlargest(15, 'COUNT')

# Filtrar los datos solo para las 15 causas de siniestro más repetidas
df_filtered = df_siniestros[df_siniestros['CAUSA DEL SINIESTRO'].isin(top_15_causas['CAUSA DEL SINIESTRO'])]

# Gráfico de barras para las 15 causas de siniestro más repetidas y su comparación con la columna ENTIDAD
fig7 = px.histogram(df_filtered, x='ENTIDAD', color='CAUSA DEL SINIESTRO',
                    title='15 Causas de Siniestro más repetidas y su Comparación con la Entidad',
                    labels={'count': 'Usuarios', 'CAUSA DEL SINIESTRO': 'ENTIDAD'})


### Dash
app = dash.Dash(__name__)
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '10px',
    'fontWeight': 'bold',
    'backgroundColor': '#E6AA10',
    'color': 'white'
}

selected_tab_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#E6AA10',
    'color': 'white',
    'padding': '10px'
}

app = dash.Dash(__name__)
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '10px',
    'fontWeight': 'bold',
    'backgroundColor': '#E6AA10',
    'color': 'white'
}

selected_tab_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#E6AA10',
    'color': 'white',
    'padding': '10px'
}

app.layout = html.Div(
    style={'backgroundColor': '#F5A365', 'padding': '20px'},
    children=[
        html.H1("Dash CNSF", style={'textAlign': 'center', 'color': '#794AD9', 'font-family': 'Helvetica'}),
        html.Hr(),
        dcc.Tabs(
            children=[
                dcc.Tab(label='Pirámide poblacional', style=tab_style, selected_style=selected_tab_style, children=[
                    html.H3("Equipo 2"),
                    html.P("A continuación mostraremos tres gráficos que consinten el avance corresponidente a la Evidencia 4."),
                    html.P("Empezamos con una gráfica en la que mostramos la población que hay por edad y por sexo:"),
                    dcc.Graph(
                        id='graph_1',
                        figure=fig1
                    )
                ]),
                dcc.Tab(label='Entidades Federativas', style=tab_style, selected_style=selected_tab_style, children=[
                    html.P("Seguimos con una gráfica de distribución para ver las Entidades Federativas con mayor cantidad de asegurados, así como su cantidad:"),
                    dcc.Dropdown(
                        id='entidades-dropdown',
                        options=[
                            {'label': 'Todas las entidades', 'value': 'all'},
                            {'label': 'Morelos', 'value': 'Morelos'},
                            {'label': 'Veracruz', 'value': 'Veracruz'},
                            {'label': 'Chihuahua', 'value': 'Chihuahua'},
                            {'label': 'Ciudad de México', 'value': 'Ciudad de México'},
                            {'label': 'Guanajuato', 'value': 'Guanajuato'},
                            {'label': 'Tamaulipas', 'value': 'Tamaulipas'},
                            {'label': 'Mexico', 'value': 'Mexico'},
                            {'label': 'Jalisco', 'value': 'Jalisco'},
                            {'label': 'Michoacán', 'value': 'Michoacán'},
                            {'label': 'Nuevo León', 'value': 'Nuevo Leon'},
                            {'label': 'Quintana Roo', 'value': 'Quintana Roo'},
                            {'label': 'San Luis Potosí', 'value': 'San Luis Potosí'},
                            {'label': 'Tabasco', 'value': 'Tabasco'},
                            {'label': 'Aguascalientes', 'value': 'Aguascalientes'},
                            {'label': 'Coahuila', 'value': 'Coahuila'},
                            {'label': 'Durango', 'value': 'Durango'},
                            {'label': 'Puebla', 'value': 'Puebla'},
                            {'label': 'Querétaro', 'value': 'Querétaro'},
                            {'label': 'Sinaloa', 'value': 'Sinaloa'},
                            {'label': 'Sonora', 'value': 'Sonora'},
                            {'label': 'Yucatán', 'value': 'Yucatán'},
                            {'label': 'Hidalgo', 'value': 'Hidalgo'},
                            {'label': 'Baja California', 'value': 'Baja California'},
                            {'label': 'Campeche', 'value': 'Campeche'},
                            {'label': 'Colima', 'value': 'Colima'},
                            {'label': 'Chiapas', 'value': 'Chiapas'},
                            {'label': 'Nayarit', 'value': 'Nayarit'},
                            {'label': 'Oaxaca', 'value': 'Oaxaca'},
                            {'label': 'Baja California Sur', 'value': 'Baja California Sur'},
                            {'label': 'Guerrero', 'value': 'Guerrero'},
                            {'label': 'Tlaxcala', 'value': 'Tlaxcala'},
                            {'label': 'Zacatecas', 'value': 'Zacatecas'},
                            {'label': 'Sin domicilio fijo', 'value': 'Sin domicilio fijo'},
                            {'label': 'En el Extranjero', 'value': 'En el Extranjero'},
                            {'label': 'No aplica', 'value': 'No aplica'}
                        ],
                        value=['all'],
                        multi=True
                    ),
                    dcc.Graph(
                        id="graph_2_1",
                        figure=fig2
                    )
                ]),
                dcc.Tab(label='Top 15 siniestros', style=tab_style, selected_style=selected_tab_style, children=[
                    html.P("De igual forma mostramos los 15 siniestros más comúnes, se puede usar los filtros para poder visualizar uno o más siniestros en específico"),
                    dcc.Dropdown(
                        id='siniestros-dropdown',
                        options=[
                            {'label': 'Todos los siniestros', 'value': 'all'},
                            {'label': 'NO ENFERMO O NO ACCIDENTADO (SANO)', 'value': 'NO ENFERMO O NO ACCIDENTADO (SANO)'},
                            {'label': 'COVID-19, VIRUS IDENTIFICADO', 'value': 'COVID-19, VIRUS IDENTIFICADO'},
                            {'label': 'INFARTO AGUDO DEL MIOCARDIO', 'value': 'INFARTO AGUDO DEL MIOCARDIO'},
                            {'label': 'COVID-19, VIRUS NO IDENTIFICADO', 'value': 'COVID-19, VIRUS NO IDENTIFICADO'},
                            {'label': 'INFARTO TRANSMURAL AGUDO DEL MIOCARDIO DE LA PARED ANTERIOR', 'value': 'INFARTO TRANSMURAL AGUDO DEL MIOCARDIO DE LA PARED ANTERIOR'},
                            {'label': 'EVENTO NO ESPECIFICADO, DE INTENCION NO DETERMINADA', 'value': 'EVENTO NO ESPECIFICADO, DE INTENCION NO DETERMINADA'},
                            {'label': 'INSUFICIENCIA RESPIRATORIA, NO ESPECIFICADA', 'value': 'INSUFICIENCIA RESPIRATORIA, NO ESPECIFICADA'},
                            {'label': 'USO EMERGENTE DE U07', 'value': 'USO EMERGENTE DE U07'},
                            {'label': 'TRASTORNO RELACIONADO CON EL VAPEO (VAPING)', 'value': 'TRASTORNO RELACIONADO CON EL VAPEO (VAPING)'},
                            {'label': 'HIPERTENSIÓN ESENCIAL (PRIMARIA)', 'value': 'HIPERTENSIÓN ESENCIAL (PRIMARIA)'},
                            {'label': 'NEUMONÍA, NO ESPECIFICADA', 'value': 'NEUMONÍA, NO ESPECIFICADA'},
                            {'label': 'BRONCONEUMONÍA, NO ESPECIFICADA', 'value': 'BRONCONEUMONÍA, NO ESPECIFICADA'},
                            {'label': 'ENFERMEDAD RENAL CRONICA', 'value': 'ENFERMEDAD RENAL CRONICA'},
                            {'label': 'CHOQUE CARDIOGÓNICO', 'value': 'CHOQUE CARDIOGÓNICO'}
                        ],
                        value=['all'],  # Valor inicial seleccionado (todos los siniestros)
                        multi=True  # Permite selección múltiple
                    ),
                    dcc.Graph(
                        id="graph_3",
                        figure=fig3
                    )
                ]),
                dcc.Tab(label='Tipos de cobertura', style=tab_style, selected_style=selected_tab_style, children=[
                    html.P("Aquí se muestran los diferentes tipos de cobertura que los asegurados contratan"),
                    dcc.Dropdown(
                        id='cobertura-dropdown',
                        options=[
                            {'label': 'Todas las coberturas', 'value': 'all'},
                            {'label': 'Invalidez total y permanente', 'value': 'Invalidez total y permanente'},
                            {'label': 'Asistencias', 'value': 'Asistencias'},
                            {'label': 'Fallecimiento', 'value': 'Fallecimiento'},
                            {'label': 'Gastos funerarios', 'value': 'Gastos funerarios'},
                            {'label': 'Otros', 'value': 'Otros'},
                            {'label': 'Exhibición de pago de prima', 'value': 'Exhibición de pago de prima'},
                            {'label': 'Enfermedades graves', 'value': 'Enfermedades graves'},
                            {'label': 'Ahorro/Inversión', 'value': 'Ahorro/Inversión'},
                            {'label': 'Muerte accidental (Doble indemnización)', 'value': 'Muerte accidental (Doble indemnización)'},
                            {'label': 'Muerte colectiva (Triple indemnización)', 'value': 'Muerte colectiva (Triple indemnización)'},
                            {'label': 'Sobrevivencia', 'value': 'Sobrevivencia'},
                            {'label': 'Devolución de prima', 'value': 'Devolución de prima'},
                            {'label': 'Desempleo/Incapacidad temporal', 'value': 'Desempleo/Incapacidad temporal'},
                            {'label': 'Pérdidas orgánicas', 'value': 'Pérdidas orgánicas'},
                            {'label': 'Dotales corto plazo', 'value': 'Dotales corto plazo'}
                        ],
                        value=["all"],
                        multi=True
                    ),
                    dcc.Graph(
                        id="graph_4",
                        figure=fig4
                    )
                ]),
                dcc.Tab(label='Histórico de Prima Emitida', style=tab_style, selected_style=selected_tab_style, children=[
                    html.P("Selecciona un rango de fechas para visualizar el histórico de prima emitida:"),
                    dcc.DatePickerRange(
                        id='date-range',
                        min_date_allowed=df_entidad['FECHA DE CORTE'].min(),
                        max_date_allowed=df_entidad['FECHA DE CORTE'].max(),
                        initial_visible_month=df_entidad['FECHA DE CORTE'].max(),
                        start_date=df_entidad['FECHA DE CORTE'].min(),
                        end_date=df_entidad['FECHA DE CORTE'].max()
                    ),
                    dcc.Graph(id='prima-emitida-graph')
                ]),
                dcc.Tab(label='Modalidad de póliza', style=tab_style, selected_style=selected_tab_style, children=[
                    html.P("Aquí se muestra una gráfica de pastel mostrando la distribución de las modalidades de pólizas."),
                    dcc.Graph(
                        id="graph_5",
                        figure=fig5
                    )
                ]),
                dcc.Tab(label="Tipos de cobertura por Entidad Federativa", style=tab_style, selected_style=selected_tab_style, children=[
                    html.P("Aquí mostramos los tipos de cobertura más solicitados por cada Entidad Federativa"),
                    dcc.Graph(
                        id="graph_6",
                        figure=fig6
                    )  
                ]),
                dcc.Tab(label="Siniestros por Entidad Federativa", style=tab_style, selected_style=selected_tab_style, children=[
                    html.P("Aquí mostramos los siniestros más ocurridos por cada Entidad Federativa"),
                    dcc.Graph(
                        id="graph_7",
                        figure=fig7
                    )
                ])               
            ],
            style={'fontFamily': 'Helvetica', 'fontSize': '18px', 'width': '50%', 'margin': 'auto'}
        )
    ]
)

# Callback para actualizar la figura de la distribución de entidades federativas
@app.callback(
    Output('graph_2_1', 'figure'),
    Input('entidades-dropdown', 'value')
)
def update_graph(selected_entidades):
    if 'all' in selected_entidades:  # Si se selecciona "Todas las entidades"
        filtered_data = df_comisiones  # Usar todos los datos sin filtrar
    else:
        filtered_data = df_comisiones[df_comisiones['ENTIDAD'].isin(selected_entidades)]  # Filtrar por entidades seleccionadas

    fig = px.histogram(filtered_data, x="ENTIDAD", title="Distribución de Entidad Federativa", color="ENTIDAD")
    return fig

# Callback siniestros
@app.callback(
    Output('graph_3', 'figure'),
    Input('siniestros-dropdown', 'value')
)
def update_graph(selected_siniestros):
    if 'all' in selected_siniestros:  # Si se selecciona "Todos los siniestros"
        filtered_data = df_siniestros  # Usar todos los datos sin filtrar
    else:
        filtered_data = df_siniestros[df_siniestros['CAUSA DEL SINIESTRO'].isin(selected_siniestros)]  # Filtrar por siniestros seleccionados

    causas_count = filtered_data["CAUSA DEL SINIESTRO"].value_counts().nlargest(15)
    df_causas = pd.DataFrame({'Causa': causas_count.index, 'Count': causas_count.values})
    fig = px.bar(df_causas, x='Causa', y='Count', color='Causa', title="Top 15 siniestros")
    return fig

# Callback cobertura

@app.callback(
    Output('graph_4', 'figure'),
    Input('cobertura-dropdown', 'value')
)
def update_graph(selected_cobertura):
    if 'all' in selected_cobertura: 
        filtered_data = df_siniestros  # Usar todos los datos sin filtrar
    else:
        filtered_data = df_siniestros[df_siniestros['COBERTURA'].isin(selected_cobertura)]  # Filtrar por entidades seleccionadas

    fig = px.histogram(filtered_data, x="COBERTURA", title="Distribución de tipos de cobertura", color="COBERTURA")
    return fig

# Callback prima

@app.callback(
    Output('prima-emitida-graph', 'figure'),
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_prima_emitida_graph(start_date, end_date):
    start_date = datetime.datetime.strptime(start_date.split('T')[0], '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date.split('T')[0], '%Y-%m-%d')
    return create_prima_emitida_graph(start_date, end_date)

if __name__ == '__main__':
    app.run_server(debug=True)

