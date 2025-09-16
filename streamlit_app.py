import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("📊 CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers (metadata.csv).")

@st.cache_data
def load_data():
    df = pd.read_csv("./data/metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))
    return df

df = load_data()



# Sidebar filters
st.sidebar.header("Filters")
year_range = st.sidebar.slider("Select Year Range", 2015, 2025, (2019, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write(f"### Showing {len(filtered)} papers between {year_range[0]} and {year_range[1]}")

# Visualization 1: Publications by Year
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, color="skyblue")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Visualization 2: Top Journals
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, color="coral")
ax.set_xlabel("Number of Papers")
st.pyplot(fig)

# Visualization 3: Word Cloud
st.subheader("Word Cloud of Paper Titles")
text = " ".join(filtered['title'].dropna().astype(str))
wc = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Show raw data
st.subheader("Sample Data")
st.dataframe(filtered[['title', 'authors', 'journal', 'publish_time']].head(20))
