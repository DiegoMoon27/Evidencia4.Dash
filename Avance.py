import pandas as pd
import dash
from dash import dcc # Dash Core Components
from dash import html # Hyper Text Markup Language
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc

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
df_siniestros = cambiar_datos(df_siniestros, 'COBERTURA', 'Muerte accidental (Doble indemnizaci-n)', 'Muerte accidental (Doble indemnización)', inplace=True)
df_siniestros = cambiar_datos(df_siniestros, 'COBERTURA', 'Muerte colectiva (Triple indemnizaci-n)', 'Muerte colectiva (Triple indemnización)', inplace=True)
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
df_emision = cambiar_datos(df_emision, 'COBERTURA', 'PŽrdidas Org‡nicas', 'Muerte colectiva (Triple indemnización)', inplace=True)
df_emision = cambiar_datos(df_emision, 'COBERTURA', 'Devoluci—n de prima', 'Muerte colectiva (Triple indemnización)', inplace=True)
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
fig2 = px.histogram(df_comisiones, x="ENTIDAD", title="Distribución de Entidad Federativa",
                    color="ENTIDAD")

### To 15 de siniestros 
causas_count = df_siniestros["CAUSA DEL SINIESTRO"].value_counts().nlargest(15)
df_causas = pd.DataFrame({'Causa': causas_count.index, 'Count': causas_count.values})
fig3 = px.bar(df_causas, x='Causa', y='Count', color='Causa', title="Top 15 siniestros")

### Dash
import dash
import dash_core_components as dcc
import dash_html_components as html

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
                    dcc.Graph(
                        id="graph_2",
                        figure=fig2
                    )
                ]),
                dcc.Tab(label='Top 15 siniestros', style=tab_style, selected_style=selected_tab_style, children=[
                    html.P("Terminamos este avance con una gráfica en la que mostramos el top 15 de siniestros:"),
                    dcc.Graph(
                        id="graph_3",
                        figure=fig3
                    )
                ])
            ],
            style={'fontFamily': 'Helvetica', 'fontSize': '18px', 'width': '50%', 'margin': 'auto'}
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)