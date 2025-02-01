import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def makeTreemap(labels,parents):
    data = go.Treemap(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="darkgrey"
    )

    fig = go.Figure(data)
    return fig

def makeIcicle(labels,parents):
    data = go.Icicle(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color="lightgrey")

    fig = go.Figure(data)
    return fig

def makeSunburst(labels,parents):
    data = go.Sunburst(
        ids=labels,
        labels=labels,
        parents=parents,
        insidetextorientation='horizontal')

    fig = go.Figure(data)
    return fig

def makeSankey(labels, parents):
    data = go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=[list(labels).index(x) for x in labels],
            target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
            label=labels,
            value=list(range(1, len(labels)))))

    fig = go.Figure(data)
    return fig

st.title("Hierarchical Data Charts")

df = pd.read_csv("data/employees.csv", header=0).convert_dtypes()

labels, parents = df[df.columns[0]] , df[df.columns[1]]

with st.expander("Treemap"):
    fig = makeTreemap(labels,parents)
    st.plotly_chart(fig,use_container_width=True)

with st.expander("Icicle"):
    fig = makeIcicle(labels,parents)
    st.plotly_chart(fig,use_container_width=True)

with st.expander("Sunburst"):
    fig = makeSunburst(labels,parents)
    st.plotly_chart(fig,use_container_width=True)

#with st.expander("Sankey"):
 #   fig = makeSankey(labels,parents)
  #  st.plotly_chart(fig,use_container_width=True)


tabs = st.tabs(["Treemap","Icicle","Sunburst","Sankey"])

# with tabs[0]:
#     fig = makeTreemap(labels,parents)
#     st.plotly_chart(fig,use_container_width=True)

# with tabs[1]:
#     fig = makeIcicle(labels,parents)
#     st.plotly_chart(fig,use_container_width=True)

# with tabs[2]:
#     fig = makeSunburst(labels,parents)
#     st.plotly_chart(fig,use_container_width=True)

with tabs[3]:
    fig = makeSankey(labels,parents)
    st.plotly_chart(fig,use_container_width=True)
