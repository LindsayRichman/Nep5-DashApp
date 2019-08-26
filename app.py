# coding: utf-8

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import os



app = dash.Dash(__name__)
server = app.server

# read data for tables (one df per table)
neo = pd.read_csv('https://raw.githubusercontent.com/LindsayRichman/cryptocurrency/master/neo.csv')
dbc = pd.read_csv('https://raw.githubusercontent.com/LindsayRichman/cryptocurrency/master/dbc.csv')
acat = pd.read_csv('https://raw.githubusercontent.com/LindsayRichman/cryptocurrency/master/acat.csv')
tky = pd.read_csv('https://raw.githubusercontent.com/LindsayRichman/cryptocurrency/master/tky.csv')
tnc = pd.read_csv('https://raw.githubusercontent.com/LindsayRichman/cryptocurrency/master/tnc.csv')
ont = pd.read_csv('https://raw.githubusercontent.com/LindsayRichman/cryptocurrency/master/ont.csv')
algo= pd.read_csv('https://raw.githubusercontent.com/LindsayRichman/cryptocurrency/master/algo.csv')
variables=pd.read_csv("https://raw.githubusercontent.com/LindsayRichman/cryptocurrency/master/variables.csv")


df_graph = pd.read_csv("https://plot.ly/~bdun9/2804.csv")

# reusable componenets
def make_dash_table(df):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def print_button():
    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

# includes page/full view
def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://blog.buyucoin.com/wp-content/uploads/2017/08/NEO.jpg', height='100', width='160')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'NEO and NEP-5 Token Overview')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('NEO Overview   ', href='/neo-overview', className="tab first"),

        dcc.Link('NEP-5 Tokens   ', href='/nep5-tokens', className="tab"),

        dcc.Link('Volume & Spread   ', href='/volume', className="tab"),

        dcc.Link('Forecasting Approach  ', href='/svm', className="tab"),

        dcc.Link('Summary & Actions   ', href='/recommendations', className="tab")

    ], className="row ")
    return menu



## Page layouts
overview = html.Div([  # page 1

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 3

            html.Div([

                html.Div([
                    html.H6('NEO Blockchain Summary',
                            className="gs-header gs-text-header padded"),

                    html.Br([]),

                    dcc.Markdown("This report provides an overview of the **NEO blockchain** and its native and partner tokens, which follow **NEP-5 protocol**.  NEO's blockchain has several unique features that interest technologists, including: "),

                    dcc.Markdown("+ **a Delegated Byzantine Fault Tolerance algorithm**, rather than a traditional Proof-of-Work or Proof-of-Stake"),
                    dcc.Markdown("+ **a lattice-based cryptographic mechanism, NEOQ**, which creates problems that cannot be solved by quantum computers, rendering NEO quantum-resistant"),

                ], className="six columns"),

                html.Div([
                    html.H6(["NEO Token"],
                            className="gs-header gs-table-header padded"),
                    html.Br([]),

                    dcc.Markdown("NEO's native token, **NEO**, has several defining characteristics:"),
dcc.Markdown('+ it pays a **dividend in GAS** everytime a block is mined; GAS is used to pay for service fees like smart contract deployment'),
dcc.Markdown('+ it grants the holder **voting rights in consensus nodes**, which generate blocks and make decisions for the blockchain '),
dcc.Markdown("**NEO** reached a high of **over $195 in mid-January of 2018**.  As of **late August 2018**, it's price is around **$17-$18**.  This decline in valuable is comparable to that of other cryptocurriences."),

                ], className="six columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6('NEO Historical Price Data: June-August 2018 ',
                            className="gs-header gs-text-header padded"),
                    html.Br([]),
                    dcc.Graph(
                        id = "graph-1",
                        figure={
                            'data': [
                                go.Ohlc(
                                    x=neo['timestamp'],
                                    open=neo['open'],
                                    high=neo['high'],
                                    low=neo['low'],
                                    close=neo['close'],
                                    name='NEO',
                                    hoverinfo= 'all',

                                    ),


                            ],
                            'layout': go.Layout(
                                autosize = True,
                                 height = 400,
                                 width = 725,
                                title = "<b>NEO Historical OHLC Data",
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                xaxis= {
                                "type": "date",
                                "rangeslider": {
      "autorange": True,
    },

                                "rangeselector": {"buttons": [
                                    {
                                      "count": 1,
                                      "label": "1M",
                                      "step": "month",
                                      "stepmode": "backward"
                                    },
                                    {
                                      "count": 3,
                                      "label": "3M",
                                      "step": "month",
                                      "stepmode": "backward"
                                    },
                                    {
                                      "count": 6,
                                      "label": "6M",
                                      "step": "month"
                                    },
                                    {
                                      "label": "All",
                                      "step": "all"
                                    }
                                  ]},

                                "showline": True,
                                "type": "date",
                                "zeroline": False
                              },
                              yaxis= {
    "autorange": True,
    "range": [11.2022222222, 60.7577777778],
    "type": "linear"
  },



                                ),

                        },

                    )
                ], className="twelve columns"),



            ], className="row"),

            # Row 5

            html.Div([



                html.Div([
                    html.H6("",
                            className="gs-header gs-table-header padded"),
                    ], className="twelve columns"),

            ], className="row ")

        ], className="subpage")

    ], className="page")


nep5 = html.Div([  # page 2

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row ``

            html.Div([

                html.Div([
                    html.H6(["NEP-5 Token Overview"],
                            className="gs-header gs-table-header padded"),
                            html.Br([]),
                            dcc.Markdown("Other **NEP-5 tokens** are used by **third-party organizations** that run on NEO's blockchain.  This section introduces **four NEP-5 tokens** that are representative of **typical blockchain-based services**: "),
                            html.Br([]),
                            dcc.Markdown("1. **Alphacat** (Symbol: **ACAT**) is a robo trading and financial advisory platform"),
                            dcc.Markdown("2. **Deep Brain Chain** (Symbol: **DBC**) supports a decentralized, low-cost computing platform that's powered by Artificial Intelligence (AI)"),
                            dcc.Markdown("3. **Ontology** (Symbol: **ONT**) provides an off-chain scaling solution for NEO's blockchain"),
                            dcc.Markdown("4. **Trinity** (Symbol: **TNC**) is a distributed trust network that provides services like identity verification and secure data exchange"),
                            dcc.Markdown('[Click here for more information on these tokens, including whitepapers and Initial Coin Offering (ICO) data. ](https://neoguide.io/nep-5-tokens-2/)'),



                ], className="twelve columns"),


            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.H6(["NEP-5 Daily Price History"],
                            className="gs-header gs-table-header padded"),
                            html.Br([]),
                            html.P("Use the chart below to explore historical high and low pricing data for NEP-5 tokens."),
                    dcc.Graph(
                        id='graph-4',
                        figure={
                            'data': [
                            go.Scatter(
                                x = acat['timestamp'],
                                y = acat['high'],
                                line = {"color": "rgb(255,73,28)"},
                                mode = "lines",
                                name = "Alphacat High"
                            ),
                            go.Scatter(
                                x = acat['timestamp'],
                                y = acat['low'],
                                line = {"color": "rgb(74,188,173)"},
                                mode = "lines",
                                name = "Alphacat Low"
                            ),
                                go.Scatter(
                                    x = dbc['timestamp'],
                                    y = dbc['high'],
                                    line = {"color": "rgb(39,135,167)"},
                                    mode = "lines",
                                    name = "Deep Brain <br /> Chain High"
                                ),
                                go.Scatter(
                                    x = dbc['timestamp'],
                                    y = dbc['low'],
                                    line = {"color": "rgb(224,85,93)"},
                                    mode = "lines",
                                    name = "Deep Brain <br /> Chain Low"
                                ),
                                go.Scatter(
                                    x = ont['timestamp'],
                                    y = ont['high'],
                                    line = {"color": "rgb(87,193,176)"},
                                    mode = "lines",
                                    name = "Ontology High"
                                ),
                                go.Scatter(
                                    x = ont['timestamp'],
                                    y = ont['low'],
                                    line = {"color": "rgb(154,32,62)"},
                                    mode = "lines",
                                    name = "Ontology Low"
                                ),
                                go.Scatter(
                                    x = tnc['timestamp'],
                                    y = tnc['high'],
                                    line = {"color": "rgb(133,78,170)"},
                                    mode = "lines",
                                    name = "Trinity High"
                                ),
                                go.Scatter(
                                    x = tnc['timestamp'],
                                    y = tnc['low'],
                                    line = {"color": "rgb(232,210,71)"},
                                    mode = "lines",
                                    name = "Trinity Low"
                                ),

                            ],
                            'layout': go.Layout(
                                autosize = False,
                                width = 720,
                                height = 320,
                                font = {
                                    "family": "Raleway",
                                    "size": 10
                                  },
                                 margin = {
                                    "r": 40,
                                    "t": 40,
                                    "b": 30,
                                    "l": 10
                                  },
                                  showlegend = True,
                                  titlefont = {
                                    "family": "Raleway",
                                    "size": 10
                                  },
                                  updatemenus= [
    {
      "x": -0.07,
      "y": 1,
      "buttons": [
        {
          "args": ["visible", [True, True, True, True, True, True, True, True]],
          "label": "All",
          "method": "restyle"
        },
        {
          "args": ["visible", [True, True, False, False, False, False, False, False, False, False]],
          "label": "ACAT",
          "method": "restyle"
        },
        {
          "args": ["visible", [False, False, True, True, False, False, False, False]],
          "label": "DBC",
          "method": "restyle"
        },
        {
          "args": ["visible", [False, False, False, False, True, True, False, False]],
          "label": "ONT",
          "method": "restyle"
        },
        {
          "args": ["visible", [False, False, False, False, False, False, True, True]],
          "label": "TNC",
          "method": "restyle"
        }
      ],
      "yanchor": "top"
    }
  ],
                                  xaxis = {
                                    "autorange": True,
                                    "rangeselector": {"buttons": [
                                        {
                                          "count": 1,
                                          "label": "1M",
                                          "step": "month",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "count": 3,
                                          "label": "3M",
                                          "step": "month",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "count": 6,
                                          "label": "6M",
                                          "step": "month"
                                        },
                                        {
                                          "label": "All",
                                          "step": "all"
                                        }
                                      ]},
                                    "showline": True,
                                    "type": "date",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": True,
                                    "showline": True,
                                    "type": "linear",
                                    "zeroline": False
                                  }
                            ),
                        },

                        config={
                            'displayModeBar': True
                        }
                    )
                ], className="twelve columns")

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6([""],
                            className="gs-header gs-table-header padded"),


                ], className="twelve columns"),


            ], className="row "),



        ], className="subpage")

    ], className="page")


volume = html.Div([ # page 3

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Volume & Fluctuation"],
                            className="gs-header gs-table-header padded"),
                    html.Br([]),

                ], className="twelve columns"),

            ], className="row "),

            # Row 2



            # Row 3

            html.Br([]),

            html.Div([

                html.Div([
                    html.H6(["Volume"], className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id='graph-4',
                        figure={
                            'data': [
                            go.Scatter(
                                x = acat['timestamp'],
                                y = acat['volumeto'],
                                line = {"color": "rgb(255,73,28)"},
                                mode = "lines",
                                name = "Alphacat",
                                fill='tonexty',
                            ),
                                go.Scatter(
                                    x = dbc['timestamp'],
                                    y = dbc['volumeto'],
                                    line = {"color": "rgb(39,135,167)"},
                                    mode = "lines",
                                    name = "Deep Brain <br /> Chain",
                                    fill='tonexty',
                                ),

                                go.Scatter(
                                    x = ont['timestamp'],
                                    y = ont['volumeto'],
                                    line = {"color": "rgb(87,193,176)"},
                                    mode = "lines",
                                    name = "Ontology",
                                    fill='tonexty',
                                ),

                                go.Scatter(
                                    x = tnc['timestamp'],
                                    y = tnc['volumeto'],
                                    line = {"color": "rgb(133,78,170)"},
                                    mode = "lines",
                                    name = "Trinity",
                                    fill='tonexty',
                                ),

                            ],
                            'layout': go.Layout(
                                autosize = False,
                                width = 720,
                                height = 250,
                                font = {
                                    "family": "Raleway",
                                    "size": 10
                                  },
                                 margin = {
                                    "r": 40,
                                    "t": 40,
                                    "b": 30,
                                    "l": 10
                                  },
                                  showlegend = True,
                                  titlefont = {
                                    "family": "Raleway",
                                    "size": 10
                                  },
                                  updatemenus= [
    {
      "x": -0.07,
      "y": 1,
      "buttons": [
        {
          "args": ["visible", [True, True, True, True]],
          "label": "All",
          "method": "restyle"
        },
        {
          "args": ["visible", [True, False, False, False]],
          "label": "ACAT",
          "method": "restyle"
        },
        {
          "args": ["visible", [False, True, False, False]],
          "label": "DBC",
          "method": "restyle"
        },
        {
          "args": ["visible", [False, False, True, False]],
          "label": "ONT",
          "method": "restyle"
        },
        {
          "args": ["visible", [False, False, False, True]],
          "label": "TNC",
          "method": "restyle"
        }
      ],
      "yanchor": "top"
    }
  ],
                                  xaxis = {
                                    "autorange": True,
                                    "rangeselector": {"buttons": [
                                        {
                                          "count": 1,
                                          "label": "1M",
                                          "step": "month",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "count": 3,
                                          "label": "3M",
                                          "step": "month",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "count": 6,
                                          "label": "6M",
                                          "step": "month"
                                        },
                                        {
                                          "label": "All",
                                          "step": "all"
                                        }
                                      ]},
                                    "showline": True,
                                    "type": "date",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": True,
                                    "showline": True,
                                    "type": "linear",
                                    "zeroline": False
                                  }
                            ),
                        },

                        config={
                            'displayModeBar': True
                        }
                    )
                ], className="twelve columns")

            ], className="row "),


            # Row 4

            html.Div([

                html.Div([
                    html.H6(["Daily Fluctuation"], className="gs-header gs-table-header padded"),

            dcc.Graph(
                id='graph-5',
                figure={
                    'data': [
                        go.Scatter(
                            x = acat['timestamp'],
                            y = acat['volumeto'],
                            line = {"color": "rgb(255,73,28)"},
                            mode = "lines",
                            name = "Alphacat",

                        ),
                            go.Scatter(
                                x = dbc['timestamp'],
                                y = dbc['volumeto'],
                                line = {"color": "rgb(39,135,167)"},
                                mode = "lines",
                                name = "Deep Brain <br /> Chain",

                            ),

                            go.Scatter(
                                x = ont['timestamp'],
                                y = ont['volumeto'],
                                line = {"color": "rgb(87,193,176)"},
                                mode = "lines",
                                name = "Ontology",

                            ),

                            go.Scatter(
                                x = tnc['timestamp'],
                                y = tnc['volumeto'],
                                line = {"color": "rgb(133,78,170)"},
                                mode = "lines",
                                name = "Trinity",

                            ),


                    ],
                    'layout': go.Layout(
                        autosize = False,
                        width = 720,
                        height = 250,
                        font = {
                            "family": "Raleway",
                            "size": 10
                          },
                         margin = {
                            "r": 40,
                            "t": 40,
                            "b": 30,
                            "l": 10
                          },
                          showlegend = True,
                          titlefont = {
                            "family": "Raleway",
                            "size": 10
                          },
                          updatemenus= [
{
"x": -0.07,
"y": 1,
"buttons": [
{
  "args": ["visible", [True, True, True, True]],
  "label": "All",
  "method": "restyle"
},
{
  "args": ["visible", [True, False, False, False]],
  "label": "ACAT",
  "method": "restyle"
},
{
  "args": ["visible", [False, True, False, False]],
  "label": "DBC",
  "method": "restyle"
},
{
  "args": ["visible", [False, False, True, False]],
  "label": "ONT",
  "method": "restyle"
},
{
  "args": ["visible", [False, False, False, True]],
  "label": "TNC",
  "method": "restyle"
}
],
"yanchor": "top"
}
],
                          xaxis = {
                            "autorange": True,
                            "rangeselector": {"buttons": [
                                {
                                  "count": 1,
                                  "label": "1M",
                                  "step": "month",
                                  "stepmode": "backward"
                                },
                                {
                                  "count": 3,
                                  "label": "3M",
                                  "step": "month",
                                  "stepmode": "backward"
                                },
                                {
                                  "count": 6,
                                  "label": "6M",
                                  "step": "month"
                                },
                                {
                                  "label": "All",
                                  "step": "all"
                                }
                              ]},
                            "showline": True,
                            "type": "date",
                            "zeroline": False
                          },
                          yaxis = {
                            "autorange": True,
                            "showline": True,
                            "type": "linear",
                            "zeroline": False
                          }
                    ),
                },

                config={
                    'displayModeBar': True
                }
            )
        ], className="twelve columns")

    ], className="row "),


        ], className="subpage")

    ], className="page")



svm = html.Div([ # page 4

            print_button(),

            html.Div([

                # Header

                get_logo(),
                get_header(),
                html.Br([]),
                get_menu(),

                # Row 1

                html.Div([

                    html.Div([
                        html.H6(["Forecasting Approach"],
                                className="gs-header gs-table-header padded"),
                        html.Br([]),
                        dcc.Markdown("**Support Vector Machine (SVM)** was used in conjunction time series forecasting methods to determine variable weights."),
                        html.P("SVM is usually a non-linear regression in high dimensional space where a kernel is used rather than the data points.  The use of kernel reduces the effect of noise.  In thie case, a linear kernel was used."),
                    ], className="twelve columns"),

                ], className="row "),

                # Row 2



                # Row 3

                html.Br([]),

                html.Div([

                    html.Div([
                        html.H6(["Data"], className="gs-header gs-table-header padded"),
                        html.Table(make_dash_table(algo)),
                    ], className=" twelve columns"),

                ], className="row "),

               html.Div([

                html.Div([
                html.Br([]),
                    html.H6(["Variable Weights"], className="gs-header gs-table-header padded"),

                        dcc.Graph(
                            id='graph-5',
                            figure={
                                'data': [
                                go.Bar(
                                    y = ['close', 'open', 'low'],
                                    x = [0.77, .35, 0.6],
                                    orientation= "h",
                                    marker={"color":'rgb(29,166,151)'},
                                    name='ACAT SMO Weights',
                                    hoverinfo="all",
                                ),
                                go.Bar(
                                    y = ['close', 'open', 'low'],
                                    x = [0.83, 0.18, 0.17],
                                    orientation= "h",
                                    marker={"color": 'rgb(224,85,93)'},
                                    name='ONT SMO Weights',
                                    hoverinfo="all",
                                ),


                                ],
                                'layout': go.Layout(
                                    autosize = False,
                                    width = 720,
                                    height = 250,
                                    font = {
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                     margin = {
                                        "r": 40,
                                        "t": 40,
                                        "b": 30,
                                        "l": 40
                                      },
                                      showlegend = True,
                                      titlefont = {
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      updatemenus= [
            {
            "x": -0.25,
            "y": 1,
            "buttons": [
            {
              "args": ["visible", [True, True]],
              "label": "All",
              "method": "restyle"
            },
            {
              "args": ["visible", [True, False]],
              "label": "ACAT",
              "method": "restyle"
            },
            {
              "args": ["visible", [False, True]],
              "label": "ONT",
              "method": "restyle"
            },

            ],
            "yanchor": "top"
            }
            ],
                                      xaxis = {
                                        "showline": True,
                                        "zeroline": False,
                                        "range": (0,1),
                                      },
                                      yaxis = {
                                        "showline": True,
                                        "zeroline": False
                                      }
                                ),
                            },

                            config={
                                'displayModeBar': True
                            }
                        )
                    ], className="twelve columns")

                ], className="row "),


                # Row 4


            ], className="subpage")

        ], className="page")



recommendations = html.Div([  # page 5

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6('Summary',
                            className="gs-header gs-text-header padded"),
                    html.Br([]),
                    dcc.Markdown("+ Currently, **NEP-5 token prices** are **highly volatile and speculative**"),
                    dcc.Markdown("+ Daily high prices **are correlated** with the previous day's closing prices"),
                    dcc.Markdown("+ Daily trading volume **is low** in comparison **to more established tokens** like Bitcoin (BTC) and Ethereum (ETH)"),
                    dcc.Markdown("+ The daily spread between high and low **can be significant, which is an attractive condition for trading**"),
                    dcc.Markdown("+ Large swings in prices often occur rapidly, sometimes within **an hour or less**.  It can be difficult for **humans** to react in a timely fashion and capitalize on the volatility."),
                    dcc.Markdown('Note: Similar findings regarding token closing prices have been published on [**_Towards Data Science_** ](https://towardsdatascience.com/a-foray-into-time-series-forecasting-using-ethereum-closing-prices-5ca69dbbd76a)'),
                ], className="six columns"),

                html.Div([
                    html.H6("Actions",
                            className="gs-header gs-table-header padded"),
                    html.Br([]),
                    dcc.Markdown("+ **A trading bot** might provide an opportunity to capitalize on NEP-5 token price volatility"),
                    dcc.Markdown("+ **A number of open-source repositories** provide boilerplate code for trading bots.  Additionally, some have large communities on forums like Slack, who **crowdsource technical support** and **enhance the code base** with bug fixes and new features."),

                ], className="six columns"),

            ], className="row "),

            html.Div([

                html.Div([
                    html.H6('NEO Quarterly Price Boundaries ',
                            className="gs-header gs-text-header padded"),
                    html.Br([]),
                    dcc.Graph(
                        id = "graph-5",
                        figure={
                            'data': [
                                go.Box(
                                    y=neo['high'],
                                    marker = {"color":'rgb(0, 128, 128)'},
                                    name='NEO',

                                    ),
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                 height = 270,
                                 width = 700,
                                title = "<b>NEO Price Boundaries: Q2",
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                xaxis= {


                              },
                              yaxis= {
                              "autorange": True,
                              "type": "linear",
  },

                        ),

                        },

                    )
                ], className="twelve columns"),

            ], className="row"),

        ], className="subpage")

    ], className="page")

noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")



# Describe the layout, or the UI, of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update page
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/neo-overview':
        return overview
    elif pathname == '/nep5-tokens':
        return nep5
    elif pathname == '/volume':
        return volume
    elif pathname == '/svm':
        return svm
    elif pathname == '/recommendations':
        return recommendations
    elif pathname == '/full-view':
        return overview,nep5, volume, svm,recommendations
    else:
        return noPage


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/lindsayrichman/pen/MqYegV.css",
                 "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
                ]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True, port=8095)
