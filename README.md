Live app: https://nep5t.herokuapp.com/

Dash app with information on the NEO blockchain and NEP-5 tokens, based on the Dash Vanguard Report (https://dash-gallery.plotly.host/dash-vanguard-report/).

This is a prototype that serves as a sample interactive business intelligence report.  

It adds the following chart types, from Plotly: <b>OHCL, horizontal bar, filled area, Candlestick</b>

It also adds the following chart components: <b>Bollinger bands, Moving Average (MA), Volume, dropdown menus</b>

Most of the text that was authored in HTML has been replaced by text that uses Dash's <b>dcc.Markdown</b> component, which generally provides better options for text formatting.

The structure of the app, and some of its CSS, has been modified to fit the report's length and branding style.

The charts were created from data pulled in by an API and wranged in Pandas in JupyterLab.  The Dash app was then built in Atom and deployed via Heroku.

