def gambar1(df_selection,values,feature_y):
    st.title("Analisis Data Numeric")
    #---------------------| columns  |----------------------
    left,right,cen=st.columns(3)

    a1,a2,a3=left.columns(3)
    a1.metric("mean :",f"{values.mean():,.3f}")
    a2.metric("median:",f"{df_selection.median():,.3f}")
    a3.metric("mode :",f"{df_selection.mode().values[0]:,.3f}")


    a1,a2,a3=cen.columns(3)
    Q1 = df_selection.quantile(0.25)
    Q3 = df_selection.quantile(0.75)
    IQR = Q3 - Q1
    a1.metric("IQR :",f"{IQR :,.3f}")
    a2.metric("min:",f"{df_selection.min():,.3f}")
    a3.metric("max :",f"{df_selection.max():,.3f}")

    a3,a1,a2=right.columns(3)
    a3.metric("skew:",f"{df_selection.skew():,.3f}")
    a1.metric("std :",f"{df_selection.std():,.3f}")
    a2.metric("var:",f"{df_selection.var():,.3f}")
    
    #---------------------|  box  |----------------------
    box=px.box(
       
       df_selection,
       y=values,
       orientation="v", points="all"

    )
    
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
        
    
    histogram.update_layout(bargap=0.01)
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
            'color': 'blue'
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
            'zeroline': True
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

    #---------------------| plot |----------------------

    left.plotly_chart(box,use_container_width=True)
    right.plotly_chart(histogram,use_container_width=True)
    cen.plotly_chart(fig,use_container_width=True)




def gambar2(df,df_obj,kat):
    st.title("Analisis Data Kategorical") 
    #---------------------| columns  |----------------------
    df = df.sort_values(by=kat, ascending=True)
    col1,col2,c=st.columns([1.8,1.2,.7])

    

    #---------------------| histogram  |----------------------
    
    count=px.histogram(
        data_frame=df,
        x=kat,
        orientation="v",color=kat, text_auto=True,height=453
    )
    count.update_layout(
        title={
            'text': 'Count Plot',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    #---------------------| donat |----------------------
    donat = px.pie(df,
            names=kat,  
            height=453, color=kat ,
            hole=0.5)
    donat.update_layout(
        title={
            'text': 'Donat Plot',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        showlegend=True,
        margin=dict(t=80)  # Increase the top margin to push the chart down
        )

    #---------------------| metric |----------------------
    c.metric("banyak data",df[kat].count())
    c.metric("banyak data unik",len(df[kat].unique()))
    c.metric("nama data teranyak",df_obj[kat].mode().iloc[0])
    c.metric("jumlah data terbanyak",max(df[kat].value_counts().values))
    
    

    #---------------------| plot |----------------------
    col1.plotly_chart(count,use_container_width=True)
    col2.plotly_chart(donat,use_container_width=True)

    
def gambar3(df,kats,nums):
    st.title("Analisis Data Kategorical dan Numeric")
    #---------------------| columns  |----------------------
    
    a,col1,col2,col3,t1=st.columns([0.33,5,1,5,0.33])



    #---------------------| box  |----------------------
    box=px.box(

        df,
        y=nums,x=kats,
        orientation="v", points="all",color=kats

    )
    box.update_layout(
        title={
            'text': 'all Box',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )
  

    
    #---------------------| histogram |----------------------
    histogram = px.histogram(df, x=nums, color=kats,opacity=0.7,text_auto=True)
    histogram.update_layout(bargap=0.01)
    histogram.update_layout(
        title={
            'text': 'Stack histogram',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )


    #---------------------| plot |----------------------
  


    col1.plotly_chart(box,use_container_width=True)
    col3.plotly_chart(histogram,use_container_width=True)







import streamlit as st
import pandas as pd
import plotly.express as px
from statsmodels.graphics.gofplots import qqplot
import plotly.graph_objects as go
from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objs as go


st.set_page_config(page_title="Dashboard analisis data matkul visual data",page_icon="🌍",layout="wide")




# load Style css
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
style_metric_cards(background_color="#FFFFFF",border_left_color="#686664")


df=pd.read_csv('penguins_size.csv')
df=df.dropna()
cari=df[df['sex']== '.']
df=df.drop(cari.index)

df_nums=df.select_dtypes(include=['int64', 'float64'])
df_obj=df.select_dtypes(include=['object', 'category'])



with st.sidebar:
    
    st.title("Analisis Data Numeric")
    feature_y =st.selectbox(
        "Pilih Data Numeric",
        options=df_nums.columns, key='num_selectbox'
    )
gambar1(df[feature_y],df[feature_y].values,feature_y)





with st.sidebar:
    st.title("")
    st.title("")
    st.title("Analisis Data Kategorical")
    kat =st.selectbox(
        "Pilih Data Numeric",
        options=df_obj.columns, key='kat_selectbox'
    )
gambar2(df,df_obj,kat)

#---------------------------------------------------------------------------------
with st.sidebar:
    st.title("")
    st.title("")
    st.title("Analisis Data Kategorical dan Numeric")
    kats = st.selectbox(
       
        "Pilih Data Kategorical",
        options=df_obj.columns
    )
    nums = st.selectbox(
        
        "Pilih Data Numeric",
        options=df_nums.columns
    )
gambar3(df,kats,nums)










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



#theme
hide_st_style=""" 
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""

