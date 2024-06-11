



def graphs1(df_selection,values):
    #total_investment=int(df_selection["Investment"]).sum()
    #averageRating=int(round(df_selection["Rating"]).mean(),2) 
    #simple bar graph  investment by business type

    #---------------------|   |----------------------
    left,right,cen=st.columns(3)

    a1,a2,a3=left.columns(3)
    a1.metric("mean :",f"{values.mean():,.2f}")
    a2.metric("median:",f"{df_selection.median():,.2f}")
    a3.metric("mode :",f"{df_selection.mode().values[0]:,.2f}")


    a1,a2,a3=cen.columns(3)
    a1.metric("std :",f"{df_selection.std():,.2f}")
    a2.metric("min:",f"{df_selection.min():,.2f}")
    a3.metric("max :",f"{df_selection.max():,.2f}")

    am,a1,a3,a2,an=right.columns([1,4.5,1,4.5,1])
    a1.metric("sum :",f"{df_selection.sum():,.2f}")
    a2.metric("var:",f"{df_selection.var():,.2f}")
    #---------------------|  box  |----------------------
    box=px.box(
       
       df_selection,
       y=values,
       orientation="v", points="all"

    )
    box.update_xaxes(tickangle=90)
    box.update_layout(
            title={
                'text': 'boxplot',
                'y':0.9,
                'x':0.55,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

    #---------------------| hist  |----------------------
    histogram=px.histogram(
        df_selection,
        x=df_selection.name
        , nbins=20, text_auto=True,height=445)
        
    
    histogram.update_layout(bargap=0.2)
    histogram.update_layout(
            title={
                'text': 'histogram',
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )
    #---------------------| QQ  |----------------------

    qqplot_data = qqplot(df[feature_y], line='s').gca().lines
    fig = go.Figure()

    fig.add_trace({
        'type': 'scatter',
        'x': qqplot_data[0].get_xdata(),
        'y': qqplot_data[0].get_ydata(),
        'mode': 'markers',
        'marker': {
            'color': '#19d3f3'
        }
    })

    fig.add_trace({
        'type': 'scatter',
        'x': qqplot_data[1].get_xdata(),
        'y': qqplot_data[1].get_ydata(),
        'mode': 'lines',
        'line': {
            'color': 'red'
        }

    })


    fig['layout'].update({
  
        'xaxis': {
            'title': 'Theoritical Quantities',
            'zeroline': False
        },
        'yaxis': {
            'title': 'Sample Quantities'
        },
        'showlegend': False,

    })

    fig.update_layout(
            title={
                'text': 'Quantile-Quantile Plot',
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )

    #---------------------| QQ  |----------------------

    left.plotly_chart(box,use_container_width=True)
    right.plotly_chart(histogram,use_container_width=True)
    cen.plotly_chart(fig,use_container_width=True)



    





import streamlit as st
import statistics
import chart_studio.plotly as py
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
import time
from statsmodels.graphics.gofplots import qqplot
import plotly.graph_objects as go

from streamlit_extras.metric_cards import style_metric_cards
st.set_option('deprecation.showPyplotGlobalUse', False)
import plotly.graph_objs as go

st.set_page_config(page_title="Dashboard",page_icon="🌍",layout="wide")
st.header("ANALYTICAL PROCESSING, KPI, TRENDS & PREDICTIONS")

#all graphs we use custom css not streamlit 
theme_plotly = None 


# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

#uncomment these two lines if you fetch data from mysql
#result = view_all_data()
#df=pd.DataFrame(result,columns=["Policy","Expiry","Location","State","Region","Investment","Construction","BusinessType","Earthquake","Flood","Rating","id"])

#load excel file | comment this line when  you fetch data from mysql
df=pd.read_csv('penguins_size.csv')
df=df.dropna()
cari=df[df['sex']== '.']
df=df.drop(cari.index)

df_nums=df.select_dtypes(exclude='O')
df_obj=df.select_dtypes(include='O')
with st.expander("distribusi data"):
    feature_y = st.selectbox('Select feature for y Quantitative Data', df_nums.columns)
    print(feature_y)

    print(df[feature_y])

    graphs1(df[feature_y],df[feature_y].values)




with st.expander("text"):
    

        kat=st.selectbox("sasa",df_obj.columns)
        value_counts = df_obj[kat].value_counts().reset_index()
        sorted_df = df.sort_values(by=kat)
        df = df.sort_values(by=kat, ascending=True)
        
        value_counts.columns = ['category', 'count']
        print(value_counts)
        print(']]]]]')
        #Button
        print("aaaaaaaaa2asp",df[kat].unique())
        
        box=px.histogram(
            data_frame=df,
            x=kat,
            orientation="v",color=kat, text_auto=True,height=453
        )
        donat = px.pie(df,
               names=kat,  
               height=453, color=kat ,
               hole=0.2)
        


        col1,col2,c=st.columns([1.8,1.2,1])
        c.metric("banyak data",df[kat].count())
        c.metric("banyak data",len(df[kat].unique()))
        c.metric("banyak data",df[kat].max())
        c.metric("banyak data",max(df[kat].value_counts().values))
        donat.update_layout(
        title={
            'text': 'Dounat Plot',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        showlegend=True,
        margin=dict(t=80)  # Increase the top margin to push the chart down
        )
        box.update_layout(
            title={
                'text': 'Count Plot',
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )
        col1.plotly_chart(box,use_container_width=True)
        col2.plotly_chart(donat,use_container_width=True)


with st.expander("campur"):
    
        col1,col2=st.columns(2)
        num=col1.selectbox("data ",df_nums.columns)
        kat=col2.selectbox("data ",df_obj.columns)
        print(df[kat].unique())
        #Button
        box=px.box(
       
            df,
            y=num,x=kat,
            orientation="v", points="all",color=kat

        )
        a,col1,col2,col3,t1=st.columns([0.33,5,1,5,0.33])
        dat1,dat2=col2.columns(2)
        dat3,dat4=col2.columns(2)

        col1.plotly_chart(box,use_container_width=True)

        print("modeee",df[num].mode().values)
        style_metric_cards(background_color="#FFFFFF",border_left_color="#686664")

        histogram = px.histogram(df, x=num, color=kat,opacity=0.77,text_auto=True)
        histogram.update_layout(bargap=0.1)
        histogram.update_layout(
            title={
                'text': 'Van Gogh: 5 Most Prominent Colors Shown Proportionally',
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )
        col3.plotly_chart(histogram,use_container_width=True)



   


#theme
hide_st_style=""" 

<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""


print()

        

data = {
    'Kategori': ['A', 'A', 'A', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'A'],
    'Value': [4, 7, 2, 5, 8, 3, 6, 9, 1, 4, 3, 5]
}
# Membuat DataFrame
df = pd.DataFrame(data)

# Menghitung frekuensi kemunculan setiap kategori
kategori_counts = df['Kategori'].value_counts().reset_index()
kategori_counts.columns = ['Kategori', 'Count']

# Mengurutkan DataFrame berdasarkan jumlah kemunculan
kategori_counts = kategori_counts.sort_values(by='Count', ascending=False)

# Countplot menggunakan Plotly
countplot = px.bar(kategori_counts, x='Kategori', y='Count', title="Count Plot Kaerertegori (Diurutkan)",color='Kategori')
df = pd.DataFrame(data)



# Pie plot menggunakan Plotly
pieplot = px.pie(df, names='Kategori', title='Pie Plot Kategori')
st.plotly_chart(pieplot)
st.plotly_chart(countplot)
st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 20px;
}
</style>
""",
    unsafe_allow_html=True,
)