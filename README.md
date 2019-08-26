Live app: https://nep5t.herokuapp.com/

Dash app with information on the NEO blockchain and NEP-5 tokens, based on the Dash Vanguard Report (https://github.com/plotly/dash-vanguard-report).

This is a prototype that serves as a sample interactive business intelligence report.  

It adds the following chart types, from Plotly: OHCL, horizontal bar, filled area, Candlestick

It also adds the following chart features: Bollinger bands, Moving Average (MA), Volume, dropdown menus 

Much of the text that was authored in HTML has been replaced by text that uses the dcc.Markdown component, which provides better options overall for text formatting.

The structure of the app, and some of its CSS, has been modified to fit the report's length and branding style.

The charts were created from data pulled in by an API and wranged in Pandas in JupyterLab.  The Dash app was then built in Atom and deployed via Heroku.

