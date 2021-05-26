import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import matplotlib.patches as mpatches
import seaborn as sns
import seaborn as sns
import altair as alt
import plotly.figure_factory as ff
import streamlit
from streamlit_agraph import agraph, Node, Edge, Config
import plotly.graph_objects as go
import squarify

nodes = []
edges = []
#nodes.append(Node(id="Yield", size=1000))  # ,
#nodes.append(Node(id="Cost Cultivation per hectare(CC)", size=400))
#nodes.append(Node(id="Profit per hectare(CC1)", size=400))
#nodes.append(Node(id="Cost Production per hectare", size=400))
#edges.append(Edge(source="Yield", target="Cost Cultivation per hectare(CC)", type="CURVE_SMOOTH"))
#edges.append(Edge(source="Yield", target="Profit per hectare(CC1)", type="CURVE_SMOOTH"))
#edges.append(Edge(source="Yield", target="Cost Production per hectare", type="CURVE_SMOOTH"))
#config = Config(width=500, height=500, directed=True)
#return_value = agraph(nodes=nodes, edges=edges, config=config)

st.set_option('deprecation.showPyplotGlobalUse', False)

crops_prod_data = pd.read_csv(r"C:\Users\Benny Antony\Desktop\agri\datafile (1).csv")
crops_prod_data = crops_prod_data.dropna()
crop_data=pd.read_csv(r"C:\Users\Benny Antony\rain.csv")
crops_prod_data1 = pd.read_csv(r"C:\Users\Benny Antony\Desktop\agri\datafile.csv")
crops_prod_data1 = crops_prod_data1.dropna()
crops_prod_data2 = pd.read_csv(r"C:\Users\Benny Antony\Desktop\agri\prod2.csv")
loan=pd.read_csv(r'C:\Users\Benny Antony\Desktop\agri\loan.csv')
co=[]
ctr=1
for col in crops_prod_data2:
    co.append(col)
df = pd.DataFrame(crops_prod_data2[:], columns =co)
df = df.melt('Crop', var_name='name', value_name='value')

if st.checkbox('Show dataframe of Cropwise value'):
    st.write(df)


chart = alt.Chart(df).mark_line().encode(
  x=alt.X('Crop:N'),
  y=alt.Y('value:Q'),
 color=alt.Color("name:N")
)
#st.altair_chart(chart, use_container_width=True)
df2 = pd.DataFrame(crops_prod_data2[:], columns =co)
#st.write(df2)
#st.line_chart(df2)
if st.button('Graphical output of Cropwise value'):
    st.altair_chart(chart, use_container_width=True)
    st.area_chart(df2)

#st.plotly_chart(fig_size)
#print(wheat_data)
#print(len(wheat_data))
#print(crops_prod_data['Yield (Quintal/ Hectare)'])
if st.checkbox('Show dataframe of Rainfall and crop'):
    st.write(crops_prod_data)
if st.button('Show distrubtion of rainfall with wheat'):
    wheat_data = crop_data[crop_data['Crop'] == 'Wheat']
    fig = px.scatter(
        x=wheat_data["Production"],
        y=wheat_data["Rainfall"],
    )
    fig.update_layout(
        xaxis_title="Production",
        yaxis_title="Rainfall",
    )


    st.write(fig)
    sns.violinplot(x='Production', y='Rainfall', palette="husl", data=wheat_data)
    st.pyplot()



if st.checkbox('Show dataframe of yield and cost per hectare'):
    st.write(crops_prod_data)

agree = st.button('Click to see distribution of yield')
if agree:
    st.bar_chart(crops_prod_data['Yield'])
    #sns.boxplot(x='class_name', y='column_name', palette="husl", data=crops_prod_data['Yield'])
    #st.pyplot()
    crops_prod_data['Yield'].hist()
    plt.show()
    st.pyplot()

df3 = pd.DataFrame(crops_prod_data[:], columns =['CC1','CC','CP','Yield'])
if st.button("Show Correlation Plot"):
        st.write("### Heatmap")
        fig, ax = plt.subplots(figsize=(10,10))
        #st.write(sns.heatmap(df3.corr(), annot=True,linewidths=0.5))
        st.pyplot()
        nodes.append(Node(id="Yield", size=1000))  # ,
        nodes.append(Node(id="Cost Cultivation per hectare(CC)", size=400))
        nodes.append(Node(id="Profit per hectare(CC1)", size=400))
        nodes.append(Node(id="Cost Production per hectare", size=400))
        edges.append(Edge(source="Yield", target="Cost Cultivation per hectare(CC)", type="CURVE_SMOOTH"))
        edges.append(Edge(source="Yield", target="Profit per hectare(CC1)", type="CURVE_SMOOTH"))
        edges.append(Edge(source="Yield", target="Cost Production per hectare", type="CURVE_SMOOTH"))
        config = Config(width=500, height=500, directed=True)
        return_value = agraph(nodes=nodes, edges=edges, config=config)
if st.button("Consumer and their consumption"):
    st.write('CC1-Profit per hectare  CC-Cost Cultivation per hectare')
    st.bar_chart(crops_prod_data['CC1'])
    st.bar_chart(crops_prod_data['CC'])
    hist_data = [crops_prod_data['CC'], crops_prod_data['CC1']]
    group_labels = ['CC', 'CC1']
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25])
    st.plotly_chart(fig, use_container_width=True)






data = pd.DataFrame({
    'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
    'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
})

# Adding code so we can have map default to the center of the data
f=[]
c=[]
for i in range(8,14):
    for j in range(75,80):
        c=[]
        c.append(i)
        c.append(j)
        f.append(c)
df = pd.DataFrame(
np.random.randn(10000, 2) / [4, 4] + [10.78, 79.13],
columns=['lat', 'lon'])
option = st.selectbox( 'Which option would you like ?',
('None','Highest Rice in south', 'Highest Rice in India', 'Highest wheat in India'))
if option=='None':
    st.write('')

if option == 'Highest Rice in south':
    st.write('Tamil Nadu Region of rice production')
    st.map(df)

dfwb = pd.DataFrame(
np.random.randn(10000, 2) / [4, 4] + [23.24, 87.85],
columns=['lat', 'lon'])
if option == 'Highest Rice in India':
    st.write('West Bengal Region of rice production')
    st.map(dfwb)
#st.map(dfwb)
dfub = pd.DataFrame(
np.random.randn(10000, 2) / [4, 4] + [28.40, 77.84],
columns=['lat', 'lon'])


#st.map(dfub)
if option == 'Highest wheat in India':
    st.write('Uttar Pradesh Region of wheat production')
    st.map(dfub)
#st.map(map_data)
cons = pd.read_csv(r'C:\Users\Benny Antony\Desktop\agri\cons.csv')
#select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
#if not st.sidebar.checkbox("Hide", True, key='1'):
    #if select == 'Pie chart':

if st.checkbox('Consumption of crops'):
    st.write(cons)
if st.button('Consumption of crops'):
    st.title("Consumption of food crops based on year")
    fig = px.pie(cons, values=cons['Consumption'][:], names=cons['Year'][:], title='Consumption')
    st.plotly_chart(fig)
    st.title('Production vs Consumption vs Imports')
    fig = go.Figure(data=[
        go.Bar(name='PRODUCTION', x=cons['Year'][:], y=cons['Production'][:]),
        go.Bar(name='Consumption', x=cons['Year'][:], y=cons['Consumption'][:]),
        go.Bar(name='Imports', x=cons['Year'][:], y=cons['Imports'][:])])
    st.plotly_chart(fig)



    #if select=='Bar plot':

#st.title("Selected Top 5 Cities")

lab=pd.read_csv(r"C:\Users\Benny Antony\Desktop\agri\wgaes.csv")
volume = [82,91,108,149,183,214,229,268,281,290,300]
labels = ['2005\n male: 82', '2006\n male: 91',
         '2007\n male: 108', '2008\n male: 149',
         '2009\n malee: 183','2010\n male:214','2011\n male:229','2012\n male:268','2013\n male:281','2014\n male:290','2015\n male:300']
color_list = ['#0f7216', '#b2790c', '#ffe9a3',
             '#f9d4d4', '#d35158', '#ea3033','blue','red','black','orange','white']





volume1 = [62,70,82,95,115,134,158,178,200,218,233]
labels1 = ['2005\n female:62', '2006\n female: 70',
         '2007\n female: 82', '2008\n female: 95',
         '2009\n female: 115','2010\n female:134','2011\n female:158','2012\n female:178','2013\n female:200','2014\n female:218','2015\n female:233']
color_list1 = ['#0f7216', '#b2790c', '#ffe9a3',
             '#f9d4d4', '#d35158', '#ea3033','blue','red','black','orange','white']





if st.checkbox('wages of agricultural labourers'):
    st.write(lab)
if st.button('Wages of agricultural labourers'):
    st.write('Men')
    plt.rc('font', size=14)
    squarify.plot(sizes=volume, label=labels,
                  color=color_list, alpha=0.7)
    plt.axis('off')
    st.write('Women')
    st.pyplot()
    plt.rc('font', size=14)
    squarify.plot(sizes=volume1, label=labels1,
                  color=color_list1, alpha=0.7)
    plt.axis('off')
    st.pyplot()


fig = px.scatter(loan,
                x='Percent_agri_loan',
                y='Numberof agri',
                color='State',
               # size='calories',
                #facet_row='shelf',
                #facet_col='type',
                #hover_name='name',
                #category_orders={'shelf': ['Top', 'Middle', 'Bottom']}
                 )


z = loan.values
sh_0, sh_1 = z.shape
x, y= np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
fig1 = go.Figure(data=[go.Surface(z=loan['State'], x=loan['Numberof agri'], y=loan['Percent_agri_loan'])])
fig1.update_layout(title='3d plot of number of agricultural loans with percentage with states', autosize=True,
                  width=800, height=800,
                  margin=dict(l=40, r=40, b=40, t=40))


if st.checkbox('Agricultural loans'):
    st.write(loan)
if st.button('Agricultural loans'):
    st.write('Loans of agriculture given by states')
    st.plotly_chart(fig)
    st.plotly_chart(fig1)