import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


@st.cache_data
def load_data():
    file_path = "species-filter-results(1).csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)

df = load_data()




# categories (sorted in asc order)
rl_category_mapping = {
    "LC": "Least Concern (LC)",
    "NT": "Near Threatened (NT)",
    "VU": "Vulnerable (VU)",
    "EN": "Endangered (EN)",
    "CR": "Critically Endangered (CR)",
    "EW": "Extinct in the Wild (EW)",
    "EX": "Extinct (EX)"
}
sorted_rl_categories = ["Least Concern (LC)", "Near Threatened (NT)", "Vulnerable (VU)", "Endangered (EN)", "Critically Endangered (CR)", "Extinct in the Wild (EW)", "Extinct (EX)"]
df["RL Category Full"] = df["RL Category"].map(rl_category_mapping)

st.sidebar.header("Filter Data")





# filters on side
family_filter = st.sidebar.multiselect("Select Family", df["Family"].unique())
rl_category_filter = st.sidebar.multiselect("Select RL Category (Red List Category)", sorted_rl_categories)
common_name_filter = st.sidebar.text_input("Search by Common Name")
scientific_name_filter = st.sidebar.text_input("Search by Scientific Name")

filtered_df = df





if family_filter:
    filtered_df = filtered_df[filtered_df["Family"].isin(family_filter)]
if rl_category_filter:
    selected_rl_values = [key for key, value in rl_category_mapping.items() if value in rl_category_filter]
    filtered_df = filtered_df[filtered_df["RL Category"].isin(selected_rl_values)]
if common_name_filter:
    filtered_df = filtered_df[filtered_df["Common name"].str.contains(common_name_filter, case=False, na=False)]
if scientific_name_filter:
    filtered_df = filtered_df[filtered_df["Scientific name"].str.contains(scientific_name_filter, case=False, na=False)]
# main title
st.title("Biodiversity Data Analysis")
# display data table
st.subheader("Filtered Species Data")
st.dataframe(filtered_df)
st.caption("Source: https://datazone.birdlife.org/search")
image_url = "https://raw.githubusercontent.com/thefakestsailent542/refactored/main/red_list_categories.png"
st.image(image_url, caption="What each Red List Category means.", use_container_width=True)
st.caption("Source: https://datazone.birdlife.org/about-our-science/the-iucn-red-list#categories-and-criteria")

st.subheader("Species Distribution by RL Category")
rl_counts = df["RL Category"].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=rl_counts.index, y=rl_counts.values, ax=ax)
ax.set_xlabel("Red List Category")
ax.set_ylabel("Count")
ax.set_title("Species Count by RL Category")
st.pyplot(fig)



# Pie Chart
st.subheader("Ecosystem Distribution")
eco_counts = {
    "Terrestrial": df["Ecosystem - Terrestrial"].sum(),
    "Freshwater": df["Ecosystem - Freshwater"].sum(),
    "Marine": df["Ecosystem - Marine"].sum()
}
fig, ax = plt.subplots()
ax.pie(eco_counts.values(), labels=eco_counts.keys(), autopct='%1.1f%%', startangle=90, colors=["#ff9999", "#66b3ff", "#99ff99"])
ax.set_title("Ecosystem Distribution")
st.pyplot(fig)


# to display families that are 100% and 0% endangered
fully_endangered_families = []
zero_endangered_families = []
endangered_categories = ["VU", "EN", "CR"]
family_counts = df["Family"].value_counts().to_dict()
endangered_counts = df[df["RL Category"].isin(endangered_categories)]["Family"].value_counts().to_dict()

for family, total_count in family_counts.items():
    endangered_count = endangered_counts.get(family, 0)
    percentage = (endangered_count / total_count) * 100
    if percentage == 100:
        fully_endangered_families.append(family)
    if percentage == 0:
        zero_endangered_families.append(family)

st.header("Endangered Species Summary:")
st.write("There are way too many 0% endangered species. Hence, we have hidden it for better readability. :)")

if fully_endangered_families:
    st.subheader("Families that are 100% Endangered:")
    st.write(", ".join(fully_endangered_families))

st.subheader("Families that are 0% Endangered:")
st.write(", ".join(zero_endangered_families))

show_zero_endangered = st.checkbox("Show Families that are 0% Endangered and Their Graphs")

st.markdown("---")  # vis divider bfr grpahs
# to display the uploaded PNG image from GitHub below the endangered species summary (similar to the one at the top)
st.header("Threats Impacting Globally Threatened Species")
st.subheader("These are the potential factors that led to the dwindling population. From the image below, it is evident that agriculture and aquaculture a.k.a farming and fishing are the primary threats to globally threatened species.")
# VS code provided that last sentence for me (SOMEHOW???)
image_url = "https://raw.githubusercontent.com/thefakestsailent542/refactored/main/Globally-threatened-species-impacted-by-each-threat.png"
st.image(image_url, caption="Globally threatened species impacted by each threat", use_container_width=True)
st.caption("Source: https://datazone.birdlife.org/search")



# % of endangered species by family
st.subheader("Percentage of Endangered Species by Family")

family_endangered_percentage = []
zero_endangered_data = []
for family, total_count in family_counts.items():
    endangered_count = endangered_counts.get(family, 0)
    percentage = (endangered_count / total_count) * 100
    if percentage > 0:
        family_endangered_percentage.append((family, percentage))
    else:
        zero_endangered_data.append((family, percentage))
# convert to dataframe
family_endangered_df = pd.DataFrame(family_endangered_percentage, columns=["Family", "Endangered Percentage"])
family_endangered_df = family_endangered_df.sort_values("Endangered Percentage", ascending=False)

zero_endangered_df = pd.DataFrame(zero_endangered_data, columns=["Family", "Endangered Percentage"])
zero_endangered_df = zero_endangered_df.sort_values("Endangered Percentage", ascending=False)
# split into multiple smaller graphs (it had like 300+ families on the x-axis and was unreadaable)
batch_size = 15
num_batches = (len(family_endangered_df) + batch_size - 1) // batch_size
for i in range(0, num_batches, 2):
    fig, axes = plt.subplots(1, min(2, num_batches - i), figsize=(16, 5))

    if num_batches - i == 1:
        axes = [axes]

    for j in range(len(axes)):
        batch_index = i + j
        subset_df = family_endangered_df.iloc[batch_index * batch_size: (batch_index + 1) * batch_size]

        if not subset_df.empty:
            ax = axes[j]
            sns.barplot(data=subset_df, x="Family", y="Endangered Percentage", ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            ax.set_xlabel("Family")
            ax.set_ylabel("% of Endangered Species")
            ax.set_ylim(0, 100)
            ax.set_title(f"Endangered Species Percentage (Batch {batch_index+1})")

    st.pyplot(fig)

if show_zero_endangered and not zero_endangered_df.empty:
    num_batches_zero = (len(zero_endangered_df) + batch_size - 1) // batch_size
    for i in range(0, num_batches_zero, 2):
        fig, axes = plt.subplots(1, min(2, num_batches_zero - i), figsize=(16, 5))
        if num_batches_zero - i == 1:
            axes = [axes]
        for j, ax in enumerate(axes):
            batch_index = i + j
            subset_df = zero_endangered_df.iloc[batch_index * batch_size: (batch_index + 1) * batch_size]
            if not subset_df.empty:
                sns.barplot(data=subset_df, x="Family", y="Endangered Percentage", ax=ax)
                ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
                ax.set_xlabel("Family")
                ax.set_ylabel("% of Endangered Species")
                ax.set_ylim(0, 100)
                ax.set_title(f"Non-Endangered Species Percentage (Batch {batch_index+1})")
        st.pyplot(fig)

