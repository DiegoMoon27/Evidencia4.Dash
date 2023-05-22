from dash import html, dcc, Dash
import dash_bootstrap_components as dbc 

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container([
    dbc.Alert("Hello, Bootstrap!", className="m-5"),
    dbc.Tabs([
    dbc.Tab(
        [
            html.H2("Contenido de mi primer Tab"),
            html.Hr(),
            dcc.Graph(id="graph_1")
        ],
        label= "Siniestros"),
    dbc.Tab([html.H2("Información especial")],label="Pólizas")
    ])
])

if __name__ == "__main__":
    app.run_server()