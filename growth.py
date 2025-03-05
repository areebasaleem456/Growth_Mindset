
# import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

# st.set_page_config(page_title="Data Sweeper", layout="wide")

# # Custom CSS
# st.markdown(
#     """
#     <style>
#     .stApp{
#         background-color: black;
#         color:white;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Title and Description
# st.title("Data Sweeper By Areeba Saleem")
# st.write("Transform your data into a clean and structured format with Data Sweeper. Upload your data and get it cleaned in seconds.")

# # Upload File
# uploaded_files = st.file_uploader("Upload files (accepts CSV or Excel)", type=["csv", "xlsx"], accept_multiple_files=True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_ext = os.path.splitext(file.name)[-1].lower()

#         # Handle file based on its extension
#         if file_ext == ".csv":
#             df = pd.read_csv(file)
#         elif file_ext == ".xlsx":
#             df = pd.read_excel(file)
#         else:
#             st.error(f"{file_ext} file type is not supported")
#             continue

#         # File details
#         st.write(f"Preview of Data from file: {file.name}")
#         st.dataframe(df.head())

#         # Data Cleaning
#         st.subheader("Data Cleaning")
#         if st.checkbox(f"Clean Data for {file.name}"):
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button(f"Remove Duplicates from {file.name}"):
#                     df.drop_duplicates(inplace=True)
#                     st.write("Duplicates Removed")
#             with col2:
#                 if st.button(f"Fill Missing Values for {file.name}"):
#                     numeric_columns = df.select_dtypes(include=["number"]).columns
#                     df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
#                     st.write("Missing Values Filled")

#         st.subheader("Select Columns to Clean")  
#         columns = st.multiselect(f"Select Columns to Clean for {file.name}", df.columns, default=df.columns)
#         df = df[columns]

#         # Data Visualization
#         st.subheader("Data Visualization")           
#         if st.checkbox(f"Visualize Data for {file.name}"):
#             st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

#         # Conversion options
#         st.subheader("Conversion Options")
#         conversion_type = st.radio(f"Convert {file.name} to", ["CSV", "Excel"], key=file.name)
#         if st.button(f"Convert {file.name}"):
#             buffer = BytesIO()
#             if conversion_type == "CSV":
#                 df.to_csv(buffer, index=False)
#                 file_name = file.name.replace(file_ext, ".csv")
#                 mime_type = "text/csv"
#             elif conversion_type == "Excel":
#                 df.to_excel(buffer, index=False)
#                 file_name = file.name.replace(file_ext, ".xlsx")
#                 mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            
#             buffer.seek(0)

#             st.download_button(
#                 label=f"Download {file_name} as {conversion_type}",
#                 data=buffer,
#                 file_name=file_name,
#                 mime=mime_type,
#             )

# st.success("All files processed successfully! 🎉")



import pandas as pd
import streamlit as st
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    .stApp{
        background-color: black;
        color:white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.title("Data Sweeper By Areeba Saleem")
st.write("Transform your data into a clean and structured format with Data Sweeper. Upload your data and get it cleaned in seconds.")

# Upload File
uploaded_files = st.file_uploader("Upload files (accepts CSV, Excel, or TSX)", type=["csv", "xlsx", "tsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Handle file based on its extension
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            elif file_ext == ".tsx":
                st.warning(f"Handling {file.name} as a regular CSV. You may need custom logic for TSX.")
                df = pd.read_csv(file)  # Assume TSX is similar to CSV for now. Replace with actual logic if needed.
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue  # Skip processing this file if it's unsupported
        except Exception as e:
            st.error(f"Error loading file {file.name}: {str(e)}")
            continue

        # File details
        st.write(f"Preview of Data from file: {file.name}")
        st.dataframe(df.head())

        # Data Cleaning
        st.subheader("Data Cleaning")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed")
            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_columns = df.select_dtypes(include=["number"]).columns
                    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
                    st.write("Missing Values Filled")

        st.subheader("Select Columns to Clean")
        columns = st.multiselect(f"Select Columns to Clean for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Data Visualization
        st.subheader("Data Visualization")
        if st.checkbox(f"Visualize Data for {file.name}"):
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # Conversion options
        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            
            buffer.seek(0)

            st.download_button(
                label=f"Download {file_name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type,
            )

st.success("All files processed successfully! 🎉")
