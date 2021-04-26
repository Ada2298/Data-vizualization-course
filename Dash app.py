import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

# -------------------------------------------------------------------------------------------------------------- 

#											PART 1: DESIGN PARAMETERS

# --------------------------------------------------------------------------------------------------------------
# Here we will set the colors, margins, DIV height&weight and other parameters

colors = {
		'full-background': 	'#DCDCDC',
		'block-borders': 	'#0d0d0d ' 
}

margins = {
		'block-margins': '10px 10px 10px 10px',
		'block-margins': '4px 4px 4px  4px'
}

sizes = {
		'subblock-heights': '300'}  


# -------------------------------------------------------------------------------------------------------------- 

#											PART 2: ACTUAL LAYOUT

# --------------------------------------------------------------------------------------------------------------
# Here we will set the DIV-s and other parts of our layout
# We need too have a 2x2 grid
# I have also included 1 more grid on top of others, where we will show the title of the app



# -------------------------------------------------------------------------------------- DIV for TITLE
div_title = html.Div(children =	html.H1('Chess game dataset exploration'),
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'text-align': 'center'
							}
					)

# -------------------------------------------------------------------------------------- DIV for first raw (1.1 and 1.2)
df = pd.read_csv (r'C:\Users\Ada\Downloads\games.csv')
df
winner = go.Figure([go.Histogram(x=df['winner'],marker = dict(color = ['sandybrown','sienna', 'olivedrab']))])

winner.update_xaxes(
        title = "Winners")

winner.update_yaxes(
        title = 'Number of winners') 

div_1_1 = dcc.Graph (id = 'histogram-of-winners',
					figure = winner,
					style ={
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width':  '49%',
							'height': sizes['subblock-heights'], 
					}
					)

vic_status = go.Figure([go.Histogram(x=df['victory_status'], marker = dict(color = 'tomato'))])
winner.update_xaxes(
        title = "Winners")
vic_status.update_xaxes(
        title = "Victory status")
vic_status.update_yaxes(
        title = 'Count') 

div_1_2 = dcc.Graph (id = 'histogram-of-victory_status',
					figure = vic_status,
					style ={
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width':  '49%',
							'height': sizes['subblock-heights'],  
					}
					)


# Collecting DIV 1.1 and 1.2 into the DIV of first raw.
# Pay attention to the 'display' and 'flex-flaw' attributes.
# With this configuration you are able to let the DIV-s 1.1 and 1.2 be side-by-side to each other.
# If you skip them, the DIV-s 1.1 and 1.2 will be ordered as separate rows.
# Pay also attention to the 'width' attributes, which specifiy what percentage of full row will each DIV cover.
div_raw1 = html.Div (children =	[div_1_1, div_1_2],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'display': 'flex',
							'flex-flaw': 'row-wrap'
							})


# -------------------------------------------------------------------------------------- DIV for second raw (2.1 and 2.2)
 
fig = px.histogram(df, x="victory_status", y="turns", color="winner",
                  title="Victory statuses colored by winner",color_discrete_map={'white': 'sandybrown', 
                                                   'black': 'sienna', 'draw': 'olivedrab'})

div_2_1 = dcc.Graph (id = 'histogram-of-victory_status_winner',
					figure = fig,
					style ={
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width':  '49%',
							'height': sizes['subblock-heights'],  
					}
					)


violins = go.Figure()
violins.add_trace(go.Violin(x = df['victory_status'][ df['winner'] == 'white' ],
		                        y = df['turns'][ df['winner'] == 'white' ],
		                        legendgroup = 'white', scalegroup = 'white', name = 'white',
		                        side = 'negative',
		                        line_color = 'sandybrown'
		                    )
             )
violins.add_trace(go.Violin(x = df['victory_status'][ df['winner'] == 'black' ],
		                        y = df['turns'][ df['winner'] == 'black' ],
		                        legendgroup = 'black', scalegroup = 'black', name = 'black',
		                        side = 'positive',
		                        line_color = 'sienna'
		                     )
             )
violins.add_trace(go.Violin(x = df['victory_status'][ df['winner'] == 'draw' ],
		                        y = df['turns'][ df['winner'] == 'draw' ],
		                        legendgroup = 'draw', scalegroup = 'draw', name = 'draw',
		                        side = 'positive',
		                        line_color = 'olivedrab'
		                     )
             )
violins.update_traces(box_visible = True, meanline_visible = True, points = 'all', jitter = 0.05)
violins.update_xaxes(
        title = "Victory_status")
violins.update_yaxes(
        title = 'Turns')
div_2_2 = dcc.Graph(id = 'violins',
					figure = violins,
					style = {
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width': '49%',
							'height': sizes['subblock-heights'],	
					}
				)	
div_raw2 = html.Div (children =	[div_2_1, div_2_2
								
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'display': 'flex',
							'flex-flaw': 'row-wrap'
							}) 

# -------------------------------------------------------------------------------------- Collecting all DIV-s in the final layout
# Here we collect all DIV-s into a final layout DIV

app.layout = html.Div(children = [
						div_title,
						div_raw1,
						div_raw2
						],
						style = {
							'backgroundColor': '#DCDCDC'
						}
					)




# -------------------------------------------------------------------------------------------------------------- 

#											PART 3: RUNNING THE APP

# --------------------------------------------------------------------------------------------------------------
# >> use __ debug=True __ in order to be able to see the changes after refreshing the browser tab,
#			 don't forget to save this file before refreshing
# >> use __ port = 8081 __ or other number to be able to run several apps simultaneously
app.run_server(debug=True,port = 8081) 