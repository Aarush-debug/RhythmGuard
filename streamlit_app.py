import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Set the page configuration to wide layout
st.set_page_config(layout="wide")


#I like to eat cheese


sns.set_theme()


# Custom CSS for background and general styling
st.markdown("""
    <style>
        /* Global Body Styles */
        body {
            background-color: #f7f7f7;  
            font-family: 'Arial', sans-serif;
            color: #333;
            margin: 0;
            padding: 0;
        }
       
        /* Header Styles */
        h1 {
            color: #ffffff;
            text-align: center;
            padding: 50px 0;
            background-color: #a83232;
            border-radius: 10px;
            font-size: 50px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }


        h2 {
            text-align: center;
            font-size: 28px;
            color: #5e0e0e;
            text-shadow: 3px 3px 6px rgba(255, 255, 255, 0.3);
            padding-bottom: 30px;
        }


        /* Sidebar Styles */
        .sidebar .sidebar-content {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
        }


        .sidebar h1 {
            font-size: 24px;
            color: #a83232;
            margin-bottom: 15px;
        }


        .sidebar p {
            font-size: 18px;
            line-height: 1.6;
        }


        /* Button Styles */
        .stButton>button {
            font-size: 30px;
            padding: 10px 30px;
            border-radius: 20px;
            background-color: #a83232;
            color: white;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
            display: block;
            margin: 0 auto;
            font-weight: bold;
        }


        /* Column Layout Styles */


        .stColumn {
            width: 100%;
            padding: 75px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
            text-align: center;
            align_items: center;
        }


        .stColumn h3 {
            color: #a83232;
            font-size: 24px;
            text-align: center;
        }


        .stColumn p {
            font-size: 20px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)


# Main content
st.markdown("<h1>Rhythm Guard</h1>", unsafe_allow_html=True)
st.markdown("<h2>A Smarter Beat: Real-Time Heart Monitoring with Machine Learning</h2>", unsafe_allow_html=True)


# Sidebar content
st.sidebar.markdown("<div class='sidebar'>", unsafe_allow_html=True)
st.sidebar.markdown("<h1>What is the problem?</h1>", unsafe_allow_html=True)
st.sidebar.write(" ")
st.sidebar.markdown("<p>Cardiovascular diseases (CVDs) are the leading cause of mortality globally, responsible for millions of deaths annually. Early and accurate monitoring of heart health can prevent severe cardiac events and improve long-term outcomes. Traditional heart monitoring devices are often expensive, bulky, and not designed for continuous use at home.</p>", unsafe_allow_html=True)


st.sidebar.markdown("<h1>What does our Innovation do?</h1>", unsafe_allow_html=True)
st.sidebar.write(" ")
st.sidebar.markdown("<p>Our innovation is a portable and real-time heart monitoring system that is both accessible and cost-effective. Using machine learning (LSTM-RL model) and math algorithms, we can accurately predict heart rate variability and identify potential cardiac abnormalities. By deploying ECG leads (Lead II, V6, and aVL), we can monitor key aspects of heart function, including overall rhythm and left ventricular activity.</p>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)


# Columns with icons or descriptions
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='stColumn'><h3>Early Detection</h3><p>Real-time monitoring helps catch potential heart issues early.</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='stColumn'><h3>Personalized Insights</h3><p>Tailored feedback helps users make informed health decisions.</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='stColumn'><h3>Targeted Monitoring</h3><p>Focuses on the left ventricle for precise and relevant insights.</p></div>", unsafe_allow_html=True)


col4, col5, col6 = st.columns(3)
with col4:
    st.markdown("<div class='stColumn'><h3>Variable Detection</h3><p>Detects conditions like Ventricular Fibrillation, Ventricular Tachycardia, Atrial Fibrillation, and Atrial Tachycardia, ensuring timely care to prevent worsening</p></div>", unsafe_allow_html=True)
with col5:
    st.markdown("<div class='stColumn'><h3>Enhanced Communication</h3><p>Detailed reports that improve discussions with healthcare providers to help provide the best care for the patient.</p></div>", unsafe_allow_html=True)
with col6:
    st.markdown("<div class='stColumn'><h3>Personalized Insights</h3><p>Since Focuses on the left ventricle for precise and relevant insights.</p></div>", unsafe_allow_html=True)


st.markdown("<h2>Choose EKG file to upload here:</h2>", unsafe_allow_html= True)


data = st.file_uploader(" ", type=["csv", "mat"])


# Add statistics here:


num_r_waves = 10000


heart_rate = num_r_waves/60


heart_rate_variability = 10


if data is not None:


    df = pd.read_csv(data)
       
    # Ensure the data has a 'Time' column
    if 't' in df.columns:
        # List available columns for the leads (excluding 'Time')
        lead_columns = [col for col in df.columns if col != 't']
           
        # Dropdown menu to select a lead (column)
        selected_lead = st.selectbox("Select the Lead to Plot", lead_columns)
           
        # Plot the selected lead against time
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['t'], df[selected_lead], color = "red", label=selected_lead)
           
        ax.set_title(f"ECG: {selected_lead} Over Time")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Voltage (V)")
        ax.legend(title="Lead")
        ax.grid(True)
        ax.set_autoscale_on(True)
           
        st.markdown(
            """
            <style>
                .matplotlib-plot {
                    width: 80%;  /* Adjust the width of the plot */
                    height: 400px;  /* Adjust the height of the plot */
                    margin-left: auto;
                    margin-right: auto;
                }
            </style>
            """, unsafe_allow_html=True
        )
        # Display the plot in Streamlit
        st.pyplot(fig)
           
        # Option to select multiple leads and plot them together
        selected_leads = st.multiselect("Select Leads to Plot", lead_columns, default=lead_columns[:2])
        if selected_leads:
            fig, ax = plt.subplots(figsize=(10, 6))
            for lead in selected_leads:
                ax.plot(df['t'], df[lead], color = "red", label=lead)
            ax.set_title("ECG Leads Over Time")
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Voltage (V)")
            ax.legend(title="Leads")
            ax.grid(True)
            ax.set_autoscale_on(True)


            st.markdown(
            """
            <style>
                .matplotlib-plot {
                    width: 80%;  /* Adjust the width of the plot */
                    height: 400px;  /* Adjust the height of the plot */
                    margin-left: auto;
                    margin-right: auto;
                }
            </style>
            """, unsafe_allow_html=True
            )


            st.pyplot(fig)
           
        # Time range selection using slider
        time_range = st.slider("Select Time Range", min_value=float(df['t'].min()), max_value=float(df['t'].max()), value=(float(df['t'].min()), float(df['t'].max())))
        filtered_df = df[(df['t'] >= time_range[0]) & (df['t'] <= time_range[1])]
           
        st.write(f"Displaying df from {time_range[0]} to {time_range[1]} seconds.")
           
        # Plot filtered df
        fig, ax = plt.subplots(figsize=(10, 6))
        for lead in selected_leads:
            ax.plot(filtered_df['t'], filtered_df[lead], color = "red", label=lead)
        ax.set_title(f"Filtered ECG Leads from {time_range[0]}s to {time_range[1]}s")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Voltage (V)")
        ax.legend(title="Leads")
        ax.grid(True)
        ax.set_autoscale_on(True)
           
        st.markdown(
            """
            <style>
                .matplotlib-plot {
                    width: 50;  /* Adjust the width of the plot */
                    height: 400px;  /* Adjust the height of the plot */
                    margin-left: auto;
                    margin-right: auto;
                }
            </style>
            """, unsafe_allow_html=True
        )
        st.pyplot(fig)

