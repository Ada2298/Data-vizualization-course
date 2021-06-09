
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import dash_table
#import  dash_design_kit as ddk
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pprint import pprint
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
df= pd.read_csv('armenian_pubs.csv')
df = df.fillna(0)

color_choices = {
	'light-blue': '#7FAB8',
	'light-grey': '#F7EFED',
	'light-red':  '#F1485B',
	'dark-blue':  '#33546D',
	'middle-blue': '#61D4E2'
}


colors = {
		'full-background':		color_choices['light-grey'],
		'chart-background':		color_choices['light-grey'],
		'histogram-color-1':	color_choices['dark-blue'],
		'histogram-color-2':	color_choices['light-red'],
		'block-borders':		color_choices['dark-blue']
}

margins = {
		'block-margins': '10px 10px 10px 10px',
		'block-margins': '4px 4px 4px 4px'
}

sizes = {
		'subblock-heights': '250px'
}

div_1_title = html.Div(children =	html.H1('Armenian Pubs'),
					style ={ 
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'text-align': 'center'
							

							}
					)

div_table = dash_table.DataTable(
       id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
   )


tabs_styles = {
    'height': '20px',
    'align-items': 'center'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'border-radius': '15px',
    'background-color': '#F2F2F2',
    'box-shadow': '4px 4px 4px 4px lightgrey',
 
}
 
tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px',
    'border-radius': '15px',
}

div_row1 = html.Div(children =	[
								div_table
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							# 'display': 'flex',
							# 'flex-flaw': 'row-wrap'
							})
div_tab1 = dcc.Tabs(id='tabs-example1', value='tab-1',  children=[
        dcc.Tab(label='Tab one', value='tab-1',style=tab_style,selected_style = tab_selected_style),
        dcc.Tab(label='Tab two', value='tab-2')],
           )
div_graph_1 = dcc.Graph(
				id = 'tabgraph1',style = {'display': 'inline-block', 'width': '48%','height':'250px'}
			            )
div_tab2 = dcc.Tabs(id='tabs-example2', value='tab-1',  children=[
        dcc.Tab(label='Tab one', value='tab-1',style=tab_style,selected_style = tab_selected_style),
        dcc.Tab(label='Tab two', value='tab-2')],
           )
div_graph_2 = dcc.Graph(
				id = 'tabgraph2',style = {'display': 'inline-block', 'width': '48%','height':'250px'}
			            )


div_row2 = html.Div (children =	[div_tab2,div_graph_2],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							#'display': 'flex',
							'flex-flaw': 'row-wrap', 'height': '450px'
							})
div_row3 = html.Div (children =	[div_tab1,div_graph_1],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							#'display': 'flex',
							'flex-flaw': 'row-wrap', 'height': '450px'
							})

occ = px.bar(df, x=" Occupation", y="Income ", color="Gender ", barmode="group", 
	title = 'The relationship between Income and occupation type colored by gender')
occ.update_xaxes(
        title = "Occupation")

occ.update_yaxes(
        title = 'Income') 

div_1_1_hist = dcc.Graph (id = 'histogram1',
					figure = occ,
					style ={
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width':  '50%'
							
					}
					)
occ2 = px.bar(df, x=" Occupation", y="WTS", color="Gender ", barmode="group",
	title = 'The relations between WTS and occupation colored by gender')

div_1_2_hist = dcc.Graph (id = 'histogram2',
					figure = occ2,
					style ={
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width':  '50%'
							
					}
					)
div_row4 = html.Div (children =	[div_1_1_hist,div_1_2_hist],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							#'display': 'flex',
							'flex-flaw': 'row-wrap'
							})
scatter = px.scatter(df, x = 'Income ', y = 'WTS', title = ' The link between income and wts')
div_2_1_scat = dcc.Graph (id = 'scatter1',
					figure = scatter,
					style ={
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width':  '50%'
							
					}
					)


div_row5 = html.Div (children =	[div_2_1_scat],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							#'display': 'flex',
							'flex-flaw': 'row-wrap'
							})
scatter2 = px.scatter(df, x="Age ", y="Income ", size="WTS", color="Fav_Pub",
           log_x=True, size_max=60, title = 'The relations between Income and Age separated for pubs')
div_2_2_scat = dcc.Graph (id = 'scatter2',
					figure = scatter2,
					style ={
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width':  '50%'
							
					}
					)
div_row6 = html.Div (children =	[div_2_2_scat],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							#'display': 'flex',
							'flex-flaw': 'row-wrap'
							})
div_1_check=dcc.Checklist(
	     id='gender',
         options=[{'label': gender, 'value': gender} 
					            		for gender in np.unique(df['Gender '])

		        ],
		        value = ['Male', 'Female'],
    labelStyle={'display': 'inline-block'}
   

    )
div_1_toggle= html.Div(
					children = daq.ToggleSwitch(
						        id='Gender_toggle',
						        value=False,
						        color = color_choices['middle-blue']
						        ),
					#style = {'width': '25%'
							#}
			    )
div_1_1_radio = html.Div(
					children = dcc.RadioItems(
							id = 'bar-line-radioitems',
						    options=[
						        {'label': 'BarPlot', 'value': 'BarPlot'},
						        {'label': 'LinePlot', 'value': 'LinePlot'}
						    ],
						    value='BarPlot',
						    labelStyle={'display': 'inline-block'}
						)  
			    )
div_mix = html.Div(children = [div_1_check,
	                                   div_1_toggle,
	                                   div_1_1_radio])
div_1_graph = dcc.Graph(
						id = 'lineplot',style = {'margin-right': 20, 'margin-left': 0, 'height': '445px'}
						)

div_1_1_filters = html.Div(children = [div_mix,div_1_graph
	                                   ],
							style ={
							'display': 'flex',
							'flex-flaw': 'row-wrap',
							'width': '60%',
							'height': sizes['subblock-heights']
							}	
								)
div_1_2_check=dcc.Checklist(
	     id='occupation',
         options=[{'label': occupation, 'value': occupation} 
					            		for occupation in np.unique(df[' Occupation'])
		        ],
		        value = ['Student','Student + working'],
    labelStyle={'display': 'block'}
   

    )
div_1_2_graph = dcc.Graph(
						id = 'lineplot2',style = {'margin-right': 35, 'margin-left': 0, 'height': '500px'}
						)




div_1_2_filters = html.Div(children = [div_1_2_check,
	                                   div_1_2_graph],
							style ={
							'display': 'flex',
							'flex-flaw': 'row-wrap',
							'width': '30%'
							}	
								)

div_row7 = html.Div(children =	[
							    div_1_1_filters,
							    div_1_2_filters
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							 'display': 'flex',
							 'flex-flaw': 'row-wrap'
							})

div_2_1_check=dcc.Checklist(
	     id='favpub',
         options=[{'label': favpub, 'value': favpub} 
					            		for favpub in np.unique(df['Fav_Pub'])

		        ],
		        value = ['Station','Calumet'],
    labelStyle={'display': 'inline-block'}
    )
div_2_2_check=dcc.Checklist(
	     id='lifestyle',
         options=[{'label': lifestyle, 'value': lifestyle} 
					            		for lifestyle in np.unique(df['Lifestyle'])

		        ],
		        value = ['Nightlife','Adventure/traveling/exploring'],
    labelStyle={'display': 'inline-block'}
    )
div_mix2 = html.Div(children = [div_2_1_check,
	                                   div_2_2_check])
div_2_graph = dcc.Graph(
				id = 'chart2'
			            )

div_row8 = html.Div(children =	[div_mix2,
								div_2_graph
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							# 'display': 'flex',
							# 'flex-flaw': 'row-wrap'
							})
div_3_1_check=dcc.Checklist(
	     id='favpub1',
         options=[{'label': favpub, 'value': favpub} 
					            		for favpub in np.unique(df['Fav_Pub'])

		        ],
		        value = ['Station','Calumet'],
    labelStyle={'display': 'inline-block'}
    )
div_1_2_radio = html.Div(
					children = dcc.RadioItems(
							id = 'bar-line-radioitems2',
						    options=[
						        {'label': 'BarPlot', 'value': 'BarPlot'},
						        {'label': 'LinePlot', 'value': 'LinePlot'}
						    ],
						    value='BarPlot',
						    labelStyle={'display': 'inline-block'}
						)  
			    )

div_3_1_graph = dcc.Graph(id = 'freq-wts')

div_row9 = html.Div(children =	[
								div_3_1_check,
								div_1_2_radio,
								div_3_1_graph
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							# 'display': 'flex',
							# 'flex-flaw': 'row-wrap'
							})
incomes = df['Income '].unique()
incomes.sort()
div_1_1_slider = dcc.RangeSlider(
        id='income-slider',
        min=incomes.min(),
        max=incomes.max(),
        step=2, 
        marks= {int(income): ({'label':str(income), 'style': {'color': '#f50'}}) 
        		for income in incomes}, 
        value=[incomes.min(),incomes.max()]
    )
div_4 = dcc.Graph(id = 'income1',
					
					style = {'margin-right': 40, 'margin-left': 0, 'height': '500px'}
					)
div_1_1_button = dcc.Checklist(
				id = 'checklist1',
		        options=[
		        	{'label': favpub, 'value': favpub} for favpub in np.unique(df['Fav_Pub'])
		        ],
		        value=['Station'],
		        labelStyle={'display': 'inline-block'}
			)
div_row10 = html.Div(children =	[
								div_1_1_slider,
								div_4,
								div_1_1_button
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							# 'display': 'flex',
							# 'flex-flaw': 'row-wrap'
							})
div_1_2_slider = dcc.RangeSlider(
        id='income-slider2',
        min=incomes.min(),
        max=incomes.max(),
        step=2, 
        marks= {int(income): ({'label':str(income), 'style': {'color': '#f50'}}) 
        		for income in incomes}, 
        value=[incomes.min(),incomes.max()]
    )
div_5 = dcc.Graph(id = 'income2',
					
					style = {'margin-right': 40, 'margin-left': 0, 'height': '400px'}
					)
div_1_2_button = dcc.Checklist(
				id = 'checklist2',
		        options=[
		        	{'label': favpub, 'value': favpub} for favpub in np.unique(df['Fav_Pub'])
		        ],
		        value=['Station'],
		        labelStyle={'display': 'inline-block'}
			)

div_row11 = html.Div(children =	[
								div_1_2_slider,
								div_5,
								div_1_2_button
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'], 'width':'75%'
							# 'display': 'flex',
							# 'flex-flaw': 'row-wrap'
							})
wtss = df['WTS'].unique()
wtss.sort()
div_1_3_slider = dcc.RangeSlider(
        id='income-slider3',
        min=wtss.min(),
        max=wtss.max(),
        step=2, 
        marks= {int(wts): ({'label':str(wts), 'style': {'color': '#f50'}}) 
        		for wts in wtss}, 
        value=[wtss.min(),wtss.max()]
    )
div_6 = dcc.Graph(id = 'income3',
					
					style = {'margin-right': 40, 'margin-left': 0, 'height': '600px'}
					)
div_1_3_button = dcc.Checklist(
				id = 'checklist3',
		        options=[
		        	{'label': favpub, 'value': favpub} for favpub in np.unique(df['Fav_Pub'])
		        ],
		        value=['Station'],
		        labelStyle={'display': 'inline-block'}
			)
div_mix1 = html.Div(children = [div_1_3_slider,
	                                   div_1_3_button
	                                   ])
	
div_row12 = html.Div(children =	[div_mix1,
								div_6,
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							# 'display': 'flex',
							# 'flex-flaw': 'row-wrap'
							})
scatter3 = px.scatter(df, x="Income ", y="WTS",  color=" Occupation", 
             title = 'The relation between Income and WTS separated for pubs')
div_3_1_scat = dcc.Graph (id = 'scatter3',
					figure = scatter3,
					style ={
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width':  '50%'
							
					}
					)

div_row13 = html.Div(children =	[
								div_3_1_scat
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							# 'display': 'flex',
							# 'flex-flaw': 'row-wrap'
							})

# div_row14 = html.Div([
#         html.P('THANK YOU'),style : {'color': 'blue', 'fontSize': 24}])
div_row14 = html.Div(children =html.H1('THANK YOU'),
					style ={ 
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'text-align': 'center'
							

							}
					)
# div_drop1 = dcc.Dropdown( id = 'drop',
#     options=[
#         {'label': favpub, 'value': favpub} for favpub in np.unique(df['Fav_Pub'])
#     ],value = ['Station'],
#     searchable=True,placeholder="Select a Pub",
# )

# div_7_graph = dcc.Graph(
# 				id = 'dropgraph'
# 			            )
# div_row14 = html.Div(children =	[
# 								div_drop1,
# 								div_7_graph
# 								],
# 					style ={
# 							'border': '3px {} solid'.format(colors['block-borders']),
# 							'margin': margins['block-margins'],
# 							# 'display': 'flex',
# 							# 'flex-flaw': 'row-wrap'
# 							})
app.layout = html.Div(	[
						div_1_title,
						div_row1,
						div_row2,
						div_row3,div_row4,div_row5,
						div_row6,div_row7,
						div_row8,div_row9,
						div_row10,
						div_row11,div_row12,div_row13,div_row14
					     ],
						style = {
							'backgroundColor': colors['full-background']
						}
					)



#####################Callbacks#################################################################################

@app.callback(Output('tabgraph1', 'figure'),
              Input('tabs-example1', 'value'))
def tabgraph1(tab1):
	traces = []
	if tab1 == 'tab-1':
		traces.append(go.Histogram(x=df[' Occupation'],marker_color='rgb(55, 83, 109)'))
	elif tab1 == 'tab-2':
		traces.append(go.Histogram(x=df['Stratum'])
)
	return{
        'data': traces,
        'layout': dict(
        	barmode='stack',
            xaxis={'title' :'Income',
   					'showgrid':  False
   					},
            yaxis={'title' :'', 
            		'showgrid': False,
            		'showticklabels': True
            		},
             autosize=False,
           	paper_bgcolor = colors['chart-background'],
           	plot_bgcolor = colors['chart-background'],
             margin={'l' :40, 'b': 40, 't' :10, 'r': 10},
            # legend={'x' 0, 'y' 1},
			title = '',
			height = 250
			 )
    }	
@app.callback(Output('tabgraph2', 'figure'),
              Input('tabs-example2', 'value'))
def tabgraph1(tab2):
	traces = []
	if tab2 == 'tab-1':
		traces.append(go.Histogram(x=df['Prim_Imp'],marker_color='rgb(55, 83, 109)'))
	elif tab2 == 'tab-2':
		traces.append(go.Histogram(x=df['Sec_Imp'])
)
	return{
        'data': traces,
        'layout': dict(
        	barmode='stack',
            xaxis={'title' :'Income',
   					'showgrid':  False
   					},
            yaxis={'title' :'', 
            		'showgrid': False,
            		'showticklabels': True
            		},
             autosize=False,
           	paper_bgcolor = colors['chart-background'],
           	plot_bgcolor = colors['chart-background'],
             margin={'l' :40, 'b': 40, 't' :10, 'r': 10},
            # legend={'x' 0, 'y' 1},
			title = '',
			height = 250
			 )
    }	
@app.callback(
    Output(component_id='lineplot', component_property='figure'),
    [Input(component_id='bar-line-radioitems', component_property='value')],
    [Input(component_id = 'gender', component_property = 'value')],
    [Input(component_id = 'Gender_toggle', component_property = 'value')]

)



def plot(chart_type,gender, toggle):
	traces = []

	#df = df[df['Gender '].isin(gender)]
	if chart_type == 'BarPlot':
		if toggle == False:
			#df = df.groupby(by='Age ')[['Income ']].sum()
				traces.append(go.Bar(x = df['Age '], y = df['Income ']))
		else:
			for gender in gender:
					traces.append(go.Bar(x = df['Age '], y = df['Income ']))
	else:
		if toggle == True:
			traces.append(go.Scatter(x = df['Age '], y= df['Income '],mode='markers'))
		else:
			for gender in gender:
				traces.append(go.Scatter(x = df['Age '], y= df['Income '],mode='markers'))

	return{
        'data': traces,
        'layout': dict(
        	barmode='stack',
            xaxis={'title' :'Income ',
   					'showgrid':  False
   					},
            yaxis={'title' :'Age ', 
            		'showgrid': False,
            		'showticklabels': True
            		},
             autosize=True,
           	paper_bgcolor = colors['chart-background'],
           	plot_bgcolor = colors['chart-background'],
            # margin={'l' 40, 'b' 40, 't' 10, 'r' 10},
            # legend={'x' 0, 'y' 1},
			title = 'The relation between Income and Age',
			height = 550
			 )
    }
@app.callback(
    Output(component_id='lineplot2', component_property='figure'),
    [Input(component_id = 'occupation', component_property = 'value')]
)
def plot2(occupations):
	for occupation in occupations:
		# print(traces)
		traces = []
		traces.append(go.Bar(x = df[df[' Occupation'] == occupation]['Age '], y = df[df[' Occupation'] == occupation]['Income ']))
	return{
        'data': traces,
        'layout': dict(
        	barmode='stack',
            xaxis={'title' :'Income',
   					'showgrid':  False
   					},
            yaxis={'title' :'', 
            		'showgrid': False,
            		'showticklabels': True
            		},
             autosize=False,
           	paper_bgcolor = colors['chart-background'],
           	plot_bgcolor = colors['chart-background'],
             margin={'l' :40, 'b': 40, 't' :10, 'r': 10},
            # legend={'x' 0, 'y' 1},
			title = 'Income and age separated by occupation type',
			height = 500
			 )
    }	


@app.callback(
    Output(component_id='chart2', component_property='figure'),
    [Input(component_id = 'favpub', component_property = 'value')],
    [Input(component_id = 'lifestyle', component_property = 'value')]

)
def plot2(favpubs, lifestyles):
	traces = []
	df_new = df[(df['Fav_Pub'].isin(favpubs)) & (df['Lifestyle'].isin(lifestyles))]
	traces.append(go.Bar(x = df_new['WTS'], y = df_new['Income ']))

	return{
        'data': traces,
        'layout': dict(
        	barmode='group',
            xaxis={'title' :'WTS',
   					'showgrid':  False
   					},
            yaxis={'title' :'', 
            		'showgrid': False,
            		'showticklabels': True
            		},
             autosize=False,
           	paper_bgcolor = colors['chart-background'],
           	plot_bgcolor = colors['chart-background'],
             margin={'l' :40, 'b': 40, 't' :10, 'r': 10},
            # legend={'x' 0, 'y' 1},
			title = 'The relation between wts and income for pubs and lifestyles',
			height = 500
			 )
    }		


@app.callback(
    Output(component_id='freq-wts', component_property='figure'),
    [Input(component_id = 'favpub1', component_property = 'value')],
    [Input(component_id = 'bar-line-radioitems2',component_property = 'value')]
)
def plot3(favpubs,chart_type1):
	traces = []
	for favpub in favpubs:
		if chart_type1 == 'BarPlot':
			traces.append(go.Bar(x = df[df['Fav_Pub'] == favpub]['Freq'], y = df[df['Fav_Pub'] == favpub]['WTS']))
		else:
			traces.append(go.Scatter(x = df[df['Fav_Pub'] == favpub]['Freq'], y = df[df['Fav_Pub'] == favpub]['WTS']))
			


	return{
        'data': traces,
        'layout': dict(
        	barmode='group',
            xaxis={'title' :'Freq',
   					'showgrid':  False
   					},
            yaxis={'title' :'', 
            		'showgrid': False,
            		'showticklabels': True
            		},
             autosize=False,
           	paper_bgcolor = colors['chart-background'],
           	plot_bgcolor = colors['chart-background'],
             margin={'l' :40, 'b': 40, 't' :10, 'r': 10},
            # legend={'x' 0, 'y' 1},
			title = 'Frequencies of attending pubs',
			height = 500
			 )
    }	
@app.callback(
	Output(component_id='income1', component_property='figure'),
    [Input(component_id='income-slider', component_property='value')],
    [Input(component_id = 'checklist1', component_property = 'value')]
)
def line_plot(income_range, favpubs):
    traces = []
    df1 = df[(df['Income '] >=income_range[0]) & (df['Income '] <= income_range[1])]
    df1 = df1[df1['Fav_Pub'].isin(favpubs)]
    for favpub in favpubs:
    	traces.append(go.Bar(x = df1[df1['Fav_Pub'] == favpub]['Prim_Imp'], y = df1[df1['Fav_Pub'] == favpub]['WTS']))
    return{
        'data': traces,
        'layout': dict(
        	barmode='group',
            xaxis={'title' :'Prim.Imp',
   					'showgrid':  False
   					},
            yaxis={'title' :'', 
            		'showgrid': False,
            		'showticklabels': True
            		},
             autosize=False,
           	paper_bgcolor = colors['chart-background'],
           	plot_bgcolor = colors['chart-background'],
             margin={'l' :40, 'b': 40, 't' :10, 'r': 10},
            # legend={'x' 0, 'y' 1},
			title = 'WTS-primary importance',
			height = '250px'
			 )
    }		
@app.callback(
	Output(component_id='income2', component_property='figure'),
    [Input(component_id='income-slider2', component_property='value')],
    [Input(component_id = 'checklist2', component_property = 'value')]
)
def line_plot(income_range, favpubs):
    traces = []
    df1 = df[(df['Income '] >=income_range[0]) & (df['Income '] <= income_range[1])]
    df1 = df1[df1['Fav_Pub'].isin(favpubs)]
    for favpub in favpubs:
    	traces.append(go.Bar(x = df1[df1['Fav_Pub'] == favpub]['Sec_Imp'], y = df1[df1['Fav_Pub'] == favpub]['WTS']))
    return{
        'data': traces,
        'layout': dict(
        	barmode='group',
            xaxis={'title' :'Sec.Imp',
   					'showgrid':  False
   					},
            yaxis={'title' :'', 
            		'showgrid': False,
            		'showticklabels': True
            		},
            autosize=False,
           	paper_bgcolor = colors['chart-background'],
           	plot_bgcolor = colors['chart-background'],
            margin={'l' :40, 'b': 40, 't' :10, 'r': 10},
            legend={'x': 0, 'y': 1},
			title = 'WTS-secondary importance',
			height = '250px'
			 )
    }		
@app.callback(
	Output(component_id='income3', component_property='figure'),
    [Input(component_id='income-slider3', component_property='value')],
    [Input(component_id = 'checklist3', component_property = 'value')]
)
def line_plot(wts_range, favpubs):
    traces = []
    df1 = df[(df['WTS'] >=wts_range[0]) & (df['WTS'] <= wts_range[1])]
    df1 = df1[df1['Fav_Pub'].isin(favpubs)]
    for favpub in favpubs:
    	traces.append(go.Bar(x = df1[df1['Fav_Pub'] == favpub]['Occasions'], y = df1[df1['Fav_Pub'] == favpub]['WTS']))
    return{
        'data': traces,
        'layout': dict(
        	barmode='group',
            xaxis={'title' :'Occasions',
   					'showgrid':  False
   					},
            yaxis={'title' :'', 
            		'showgrid': False,
            		'showticklabels': True
            		},
            autosize=True,
           	paper_bgcolor = colors['chart-background'],
           	plot_bgcolor = colors['chart-background'],
             margin={'l' :40, 'b': 40, 't' :10, 'r': 10},
            # legend={'x' 0, 'y' 1},
			title = 'WTS-Occasions',
			height = '150px'
			 )
    }		

# @app.callback(Output('tabgraph', 'figure'),
#               Input('tabs-example', 'value'))
# def tabgraph(tab):
# 	traces = []
# 	if tab == 'tab-1':
# 		traces.append(go.Scatter(x = df['Age '], y= df['Income ']))
# 	elif tab == 'tab-2':
# 		traces.append(go.Bar(x = df['Age '], y = df['Income ']))
# 	return{
#         'data': traces,
#         'layout': dict(
#         	barmode='stack',
#             xaxis={'title' :'Income',
#    					'showgrid':  False
#    					},
#             yaxis={'title' :'', 
#             		'showgrid': False,
#             		'showticklabels': True
#             		},
#              autosize=False,
#            	paper_bgcolor = colors['chart-background'],
#            	plot_bgcolor = colors['chart-background'],
#              margin={'l' :40, 'b': 40, 't' :10, 'r': 10},
#             # legend={'x' 0, 'y' 1},
# 			title = 'Income and age',
# 			height = 250
# 			 )
#     }	

# @app.callback(Output('dropgraph', 'figure'),
#               Input('drop', 'value'))
# def plot2(favpubs):
# 	traces = []
# 	df = df[df['Fav_Pub'].isin(favpubs)]
# 		# print(traces)
	
# 	traces.append(go.Bar(x = df['Freq'], y = df['Occasions'],
# 			name = favpub))
# 	return{
#         'data': traces,
#         'layout': dict(
#         	barmode='stack',
#             xaxis={'title' :'Income',
#    					'showgrid':  False
#    					},
#             yaxis={'title' :'', 
#             		'showgrid': False,
#             		'showticklabels': True
#             		},
#              autosize=False,
#            	paper_bgcolor = colors['chart-background'],
#            	plot_bgcolor = colors['chart-background'],
#              margin={'l' :40, 'b': 40, 't' :10, 'r': 10},
#             # legend={'x' 0, 'y' 1},
# 			title = 'Income and age',
# 			height = 500
# 			 )
#     }	



if __name__ == '__main__':
	app.run_server(debug=True, port = 8085) #host = '0.0.0.0')
