import streamlit as st 

st.title("Hierarchical Data Viewer")
st.header("This is a Header")
st.subheader("subheader")
st.caption("caption")

st.write("this is a write")
st.text("fixed text")
st.code("v = variable()\nanother_call()","python")
st.markdown("**BOLD**")

st.error("this is an error")
st.info("this is info")
st.warning("this is a warning")
st.success("this is success")

st.balloons()
st.snow()