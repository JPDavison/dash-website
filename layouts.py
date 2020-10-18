import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from styles import *


def main_page(app, visible):
    main_page = html.Div([
        dbc.Row([
            dbc.Col([
                html.Div(
                    html.Img(src=app.get_asset_url("banner.webp"), style={
                             "max-width": "100%", "height": "auto"}),
                )
            ])
        ]),
        dbc.Row(
            dbc.Col(
                html.P("Lorem ipsum dolor sit amet, \
                    consectetur adipiscing elit. Sed ac fringilla tortor. \
                    Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; \
                    Duis lorem est, commodo quis molestie sed, \
                    cursus vel purus. Nunc eu urna eget neque sollicitudin ultrices. Ut libero tortor, \
                    pretium at tristique vitae, pretium vitae neque. Ut vestibulum mi sit amet odio vestibulum tristique. \
                    Maecenas accumsan aliquet lacus, ut dignissim mi gravida in. In at libero volutpat, iaculis tortor sed, \
                    dignissim felis. Pellentesque dictum molestie euismod. Mauris a efficitur justo. \
                    Vestibulum posuere fringilla sem sed gravida. ")
            ), className="m-3"
        ),
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H3("KPI"),
                        html.P(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
                        Aenean euismod euismod tempus. Proin lobortis, nunc auctor \
                        commodo sollicitudin, leo quam."),
                        dbc.Button("Go there", color="dark", id="button-kpi")
                    ])
                ], color="warning", outline=True)
            ),
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H3("Cluster"),
                        html.P(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
                        Aenean euismod euismod tempus. Proin lobortis, nunc auctor \
                        commodo sollicitudin, leo quam."),
                        dbc.Button("Go there", color="dark", id="button-cluster")
                    ]),
                ], color="warning", outline=True)
            ),
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H3("Resultado"),
                        html.P(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
                        Aenean euismod euismod tempus. Proin lobortis, nunc auctor \
                        commodo sollicitudin, leo quam."),
                        dbc.Button("Go there", color="dark", id="button-result")
                    ])
                ], color="warning", outline=True)
            ),
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H3("XXI"),
                        html.P(
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
                        Aenean euismod euismod tempus. Proin lobortis, nunc auctor \
                        commodo sollicitudin, leo quam."),
                        dbc.Button("Go there", color="dark", id="button-xxi")
                    ])
                ], color="warning", outline=True)
            ),
        ], className="m-4")
    ], style={"display": "block" if visible else "none"})

    return main_page


def sidebar(visible):
    SIDEBAR_STYLE["display"] = "block" if visible else "none"
    sidebar = html.Div(
        [
            html.H4("Menú", className="lead"),  # display-4
            html.Hr(),  # Esto es una línea horizontal que separa lo de arriba
            html.P(
                "Navegar al elemento deseado", className="lead"  # Esto es un elemento de párrafo
            ),
            dbc.Nav(
                [
                    dbc.Button("Main", id="link-hoja-main"),
                    dbc.Button("KPI's", id="link-hoja-1"),
                    dbc.Button("Clustering: definición", id="link-hoja-2"),
                    dbc.Button("Clustering: resultados", id="link-hoja-3"),
                ],
                vertical=True,  # Esto para qué?
                pills=True,  # Esto para qué?
            ),
        ], style=SIDEBAR_STYLE
    )
    return sidebar