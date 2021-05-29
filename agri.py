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

f=[['ARHAR', 'Uttar Pradesh', 9794.05, 23076.74, 1941.55, 9.83],
       ['ARHAR', 'Karnataka', 10593.15, 16528.68, 2172.46, 7.47],
       ['ARHAR', 'Gujarat', 13468.82, 19551.9, 1898.3, 9.59],
       ['ARHAR', 'Andhra Pradesh', 17051.66, 24171.65, 3670.54, 6.42],
       ['ARHAR', 'Maharashtra', 17130.55, 25270.26, 2775.8, 8.72],
       ['COTTON', 'Maharashtra', 23711.44, 33116.82, 2539.47, 12.69],
       ['COTTON', 'Punjab', 29047.1, 50828.83, 2003.76, 24.39],
       ['COTTON', 'Andhra Pradesh', 29140.77, 44756.72, 2509.99, 17.83],
       ['COTTON', 'Gujarat', 29616.09, 42070.44, 2179.26, 19.05],
       ['COTTON', 'Haryana', 29918.97, 44018.18, 2127.35, 19.9],
       ['GRAM', 'Rajasthan', 8552.69, 12610.85, 1691.66, 6.83],
       ['GRAM', 'Madhya Pradesh', 9803.89, 16873.17, 1551.94, 10.29],
       ['GRAM', 'Uttar Pradesh', 12833.04, 21618.43, 1882.68, 10.93],
       ['GRAM', 'Maharashtra', 12985.95, 18679.33, 2277.68, 8.05],
       ['GRAM', 'Andhra Pradesh', 14421.98, 26762.09, 1559.04, 16.69],
       ['GROUNDNUT', 'Karnataka', 13647.1, 17314.2, 3484.01, 4.71],
       ['GROUNDNUT', 'Andhra Pradesh', 21229.01, 30434.61, 2554.91,
        11.97],
       ['GROUNDNUT', 'Tamil Nadu', 22507.86, 30393.66, 2358.0, 11.98],
       ['GROUNDNUT', 'Gujarat', 22951.28, 30114.45, 1918.92, 13.45],
       ['GROUNDNUT', 'Maharashtra', 26078.66, 32683.46, 3207.35, 9.33],
       ['MAIZE', 'Bihar', 13513.92, 19857.7, 404.43, 42.95],
       ['MAIZE', 'Karnataka', 13792.85, 20671.54, 581.69, 31.1],
       ['MAIZE', 'Rajasthan', 14421.46, 19810.29, 658.77, 23.56],
       ['MAIZE', 'Uttar Pradesh', 15635.43, 21045.11, 1387.36, 13.7],
       ['MAIZE', 'Andhra Pradesh', 25687.09, 37801.85, 840.58, 42.68],
       ['MOONG', 'Orissa', 5483.54, 8266.98, 2614.14, 3.01],
       ['MOONG', 'Rajasthan', 6204.23, 9165.59, 2068.67, 4.05],
       ['MOONG', 'Karnataka', 6440.64, 7868.64, 5777.48, 1.32],
       ['MOONG', 'Andhra Pradesh', 6684.18, 13209.32, 2228.97, 5.9],
       ['MOONG', 'Maharashtra', 10780.76, 15371.45, 2261.24, 6.7],
       ['PADDY', 'Uttar Pradesh', 17022.0, 28144.5, 732.62, 36.61],
       ['PADDY', 'Orissa', 17478.05, 25909.05, 715.04, 32.42],
       ['PADDY', 'West Bengal', 24731.06, 33046.12, 731.25, 39.04],
       ['PADDY', 'Punjab', 25154.75, 45291.24, 669.86, 67.41],
       ['PADDY', 'Andhra Pradesh', 29664.84, 46450.2, 789.9, 56.0],
       ['RAPESEED AND MUSTARD', 'Madhya Pradesh', 8686.43, 17705.93,
        1279.6, 12.94],
       ['RAPESEED AND MUSTARD', 'Rajasthan', 11385.7, 19259.84, 1341.29,
        13.54],
       ['RAPESEED AND MUSTARD', 'Uttar Pradesh', 12774.41, 22560.3,
        1595.56, 13.57],
       ['RAPESEED AND MUSTARD', 'Gujarat', 13740.64, 19083.55, 1610.4,
        11.61],
       ['RAPESEED AND MUSTARD', 'Haryana', 14715.27, 27507.54, 1251.12,
        19.94],
       ['SUGARCANE', 'Uttar Pradesh', 24538.32, 45239.51, 93.64, 448.89],
       ['SUGARCANE', 'Karnataka', 55655.44, 86765.77, 86.53, 986.21],
       ['SUGARCANE', 'Andhra Pradesh', 56621.16, 91442.63, 119.72,
        757.92],
       ['SUGARCANE', 'Maharashtra', 57673.6, 85801.95, 107.56, 744.01],
       ['SUGARCANE', 'Tamil Nadu', 66335.06, 89025.27, 85.79, 1015.45],
       ['WHEAT', 'Madhya Pradesh', 12464.4, 22489.75, 810.25, 23.59],
       ['WHEAT', 'Punjab', 17945.58, 35423.48, 804.8, 39.83],
       ['WHEAT', 'Uttar Pradesh', 18979.38, 31902.74, 769.84, 34.99],
       ['WHEAT', 'Rajasthan', 19119.08, 29876.36, 683.58, 37.19]]
crops_prod_data = crops=pd.DataFrame(f, columns = ['Crop','State','CC1','CC','CP','Yield'])
crops_prod_data = crops_prod_data.dropna()
r=[['Tamil Nadu', 'Arecanut', 233.0, 4.30472103, 926.5],
 ['Kerala', 'Arecanut', 5207.0, 1.228154408, 3489.6],
 ['Kerala', 'Arecanut', 7279.0, 0.7404863309999999, 3420.6],
 ['Kerala', 'Arecanut', 10584.0, 1.4724111869999998, 2507.4],
 ['Tamil Nadu', 'Arecanut', 42.0, 1.2619047620000001, 741.9],
 ['Kerala', 'Arecanut', 4783.0, 1.16328664, 2524.5],
 ['Tamil Nadu', 'Arecanut', 2.0, 2.5, 926.5],
 ['Kerala', 'Arecanut', 7069.0, 0.66303579, 3489.6],
 ['Kerala', 'Arecanut', 4674.0, 1.097560976, 2810.6],
 ['Tamil Nadu', 'Arecanut', 367.0, 2.207084469, 741.9],
 ['Tamil Nadu', 'Arecanut', 126.0, 1.301587302, 741.9],
 ['Kerala', 'Arecanut', 11189.0, 1.1466618999999998, 2931.1],
 ['Tamil Nadu', 'Arecanut', 7.0, 2.4285714290000002, 926.5],
 ['Kerala', 'Arecanut', 4549.93, 1.074719831, 3131.8],
 ['Kerala', 'Arecanut', 8116.0, 1.313578117, 3031.1],
 ['Kerala', 'Arecanut', 7055.17, 0.666283024, 3035.1],
 ['Tamil Nadu', 'Arecanut', 2.0, 0.5, 1365.3],
 ['Kerala', 'Arecanut', 1650.0, 0.650909091, 2151.1],
 ['Tamil Nadu', 'Arecanut', 4.0, 2.0, 928.5],
 ['Kerala', 'Arecanut', 4054.0, 1.0732609770000001, 2886.1],
 ['Kerala', 'Arecanut', 4456.0, 0.33168761199999997, 3151.5],
 ['Bihar', 'Wheat', 58778.0, 1.215812039, 1353.9],
 ['Odisha', 'Wheat', 22.0, 1.413636364, 1097.2],
 ['Punjab', 'Wheat', 85000.0, 5.047058824, 594.8],
 ['Punjab', 'Wheat', 354000.0, 4.426553672, 588.6],
 ['Punjab', 'Wheat', 85000.0, 4.094117647, 647.7],
 ['Punjab', 'Wheat', 383000.0, 4.336814621, 441.0],
 ['Bihar', 'Wheat', 31503.0, 2.794305304, 1197.7],
 ['Bihar', 'Wheat', 55379.0, 1.941024576, 1353.9],
 ['Bihar', 'Wheat', 61504.0, 2.335002601, 629.2],
 ['Bihar', 'Wheat', 76219.0, 3.0100368669999997, 1069.9],
 ['Bihar', 'Wheat', 67961.0, 2.87248569, 1069.9],
 ['Bihar', 'Wheat', 59857.0, 1.859047396, 1147.8],
 ['Bihar', 'Wheat', 27786.0, 1.36054128, 1332.5],
 ['Punjab', 'Wheat', 386000.0, 4.1424870469999995, 351.7],
 ['Punjab', 'Wheat', 258000.0, 5.170542636, 405.3],
 ['Bihar', 'Wheat', 61360.0, 2.65374837, 1207.0],
 ['Bihar', 'Wheat', 61704.0, 2.099831453, 1402.7],
 ['Uttarakhand', 'Wheat', 9644.0, 1.489319784, 1564.7],
 ['Bihar', 'Wheat', 24063.0, 1.501101276, 1303.7],
 ['Bihar', 'Wheat', 71387.0, 2.609956995, 1402.7],
 ['Odisha', 'Wheat', 40.0, 1.8575, 1648.2],
 ['Bihar', 'Wheat', 60663.0, 2.813263439, 1069.9],
 ['Odisha', 'Wheat', 5.0, 2.44, 1290.4],
 ['Punjab', 'Wheat', 374000.0, 4.647058824, 364.4],
 ['Bihar', 'Wheat', 98681.0, 2.017997386, 1052.8],
 ['Bihar', 'Wheat', 24050.0, 3.039168399, 1097.1]]
crop_data=pd.DataFrame(r, columns = ['State_Name','Crop','Area','Production','Rainfall'])
#crops_prod_data1 = pd.read_csv(r"C:\Users\Benny Antony\Desktop\agri\datafile.csv")
#crops_prod_data1 = crops_prod_data1.dropna()
p=[['2004-05', 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
 ['2005-06', 101, 101, 107, 108, 109, 99, 97, 102, 86, 96, 92, 99],
 ['2006-07', 99, 112, 110, 134, 103, 99, 98, 101, 85, 91, 91, 101],
 ['2007-08', 105, 115, 115, 124, 118, 98, 98, 100, 97, 87, 96, 104],
 ['2008-09', 112, 117, 113, 124, 113, 102, 98, 99, 104, 80, 109, 106],
 ['2009-10', 121, 127, 123, 146, 124, 104, 112, 116, 103, 81, 107, 115],
 ['2010-11', 117, 120, 122, 137, 128, 114, 123, 133, 99, 109, 138, 123],
 ['2011-12', 110, 108, 136, 129, 115, 119, 124, 137, 102, 107, 140, 122]]
crops_prod_data2 = pd.DataFrame(p, columns = ['Crop','Rice','Wheat','Coarse Cereals','Pulses','Vegetables','Fruits','Milk','Eggs, Fish and Meat','Oilseeds','Sugarcane','Fibers','All Agriculture'])
x=[['UP', 16.9, 79081],
 ['Maharashtra', 8.7, 40672],
 ['Rajasthan', 8.5, 40055],
 ['AP', 7.1, 33421],
 ['West Bengal', 7.0, 32787],
 ['Karanataka', 7.0, 32775],
 ['Bihar', 6.4, 30156],
 ['MP', 5.9, 27414],
 ['Odhisa', 5.5, 25830],
 ['Telengana', 4.8, 22628],
 ['Punjab', 1.6, 7499],
 ['TN', 20.5, 96163]]

loan=pd.DataFrame(x, columns = ['State','Percent_agri_loan','Numberof agri'])
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
    st.write(crop_data)
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
        st.write(sns.heatmap(df3.corr(), annot=True,linewidths=0.5))
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
co=[[1981.0, 60.64, 40.93, 20.41],
 [1990.0, 125.46, 90.45, 27.58],
 [2000.0, 167.02, 147.04, 20.91],
 [2010.0, 281.22, 163.8, 123.63],
 [2011.0, 277.9, 166.27, 130.02],
 [2012.0, 255.36, 160.24, 86.98],
 [2013.0, 244.82, 163.38, 67.31],
 [2014.0, 255.76, 165.15, 91.35],
 [2015.0, 267.53, 178.1, 100.09],
 [2016.0, 259.49, 179.49, 78.35]]
cons = pd.DataFrame(co, columns = ['Year','Consumption','Production','Imports'])
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

c=[[2005, 82, 62],
 [2006, 91, 70],
 [2007, 108, 82],
 [2008, 149, 95],
 [2009, 183, 115],
 [2010, 214, 134],
 [2011, 229, 158],
 [2012, 268, 178],
 [2013, 281, 200],
 [2014, 290, 218],
 [2015, 300, 233]]
lab=pd.DataFrame(c, columns = ['Year','Male','Female'])
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
