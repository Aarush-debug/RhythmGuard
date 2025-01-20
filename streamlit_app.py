import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Set the page configuration to wide layout
st.set_page_config(page_title="Rhythm Guard", page_icon = "🫀", layout="wide" )


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
            
        ab {
            text-align: center;
            font-size: 28px;
            color: #f54949;
            text-shadow: 3px 3px 6px rgba(255, 255, 255, 0.3);
        }
        
        norm {
            text-align: center;
            font-size: 28px;
            color: #46fa79;
            text-shadow: 3px 3px 6px rgba(255, 255, 255, 0.3);
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
st.sidebar.markdown("<p>Cardiovascular diseases (CVDs) are the leading cause of mortality globally, responsible for millions of deaths annually. Early and accurate monitoring of heart health can prevent severe cardiac events and improve long-term outcomes. Traditional monitering softwares are very unreliable and require subscriptions to give a detailed analysis. </p>", unsafe_allow_html=True)


st.sidebar.markdown("<h1>What does our Innovation do?</h1>", unsafe_allow_html=True)
st.sidebar.write(" ")
st.sidebar.markdown("<p>Our innovation is a heart monitering system that is both accessible and free to all users. Using a combination of machine learning (LSTM-RL model) and math algorithms, we can accurately predict heart rate variability and identify potential cardiac abnormalities. By deploying ECG leads (Lead II, V6, and aVL), we can monitor key aspects of heart function, including overall rhythm and left ventricular activity.</p>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)


# Columns with icons or descriptions
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='stColumn'><h3>Early Detection</h3><p>Effective monitoring helps catch potential heart issues early.</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='stColumn'><h3>Personalized Insights</h3><p>Tailored feedback helps users make informed health decisions.</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='stColumn'><h3>Targeted Monitoring</h3><p>Focuses on the left ventricle for precise and relevant insights.</p></div>", unsafe_allow_html=True)


col4, col5, col6 = st.columns(3)
with col4:
    st.markdown("<div class='stColumn'><h3>Variable Detection</h3><p>Detects conditions like Ventricular Fibrillation, Ventricular Tachycardia, Atrial Fibrillation, and Atrial Tachycardia, ensuring timely care to prevent it from worsening.</p></div>", unsafe_allow_html=True)
with col5:
    st.markdown("<div class='stColumn'><h3>Enhanced Communication</h3><p>Detailed reports that improve discussions with healthcare providers to help provide the best care for the patient.</p></div>", unsafe_allow_html=True)
with col6:
    st.markdown("<div class='stColumn'><h3>Comprehensive Review</h3><p>Uses heart measurements such as RMSSD and SDNN to ensure accurate analysis.</p></div>", unsafe_allow_html=True)


st.markdown("<h2>Choose EKG file to upload here:</h2>", unsafe_allow_html= True)


data = st.file_uploader(" ", type=["csv", "mat"])

# R-R Interval calculation
if data is not None:
    df = pd.read_csv(data)

    # Dropdown to select columns
    time_col = st.selectbox("Time column", df.columns[0])
    ecg_col = st.selectbox("ECG signal column", df.columns[1:])

    # Detect R-peaks
    st.markdown("<h2>Summary:</h2>", unsafe_allow_html = True)

    height_threshold = -49000

    distance = 200

    # Calculate R-R intervals
    peaks, _ = find_peaks(df[ecg_col], height=height_threshold, distance=distance)
    rr_intervals = np.array(np.diff(df[time_col].iloc[peaks]))  # Time differences between successive R-peaks
    #rr_intervals_ms = rr_intervals * 1000

    diff_rr_intervals = np.diff(rr_intervals)

    print(diff_rr_intervals)

    # Parasympathetic Tone
    rmssd = np.sqrt(np.mean(diff_rr_intervals**2))

    # Autonomic Tone
    #sdnn = np.std(rr_intervals)

    if (len(peaks)*2) > 100 or (len(peaks)*2) < 60:
        st.markdown(f"<ab>Heart Rate: {(len(peaks) * 2)} bpm (Normal Range is 60 - 100 bpm) </ab>", unsafe_allow_html= True)
        st.markdown(f"<ab>Number of R-peaks detected: {len(peaks)}</ab>", unsafe_allow_html= True)
    else :
        st.markdown(f"<norm>Heart Rate: {(len(peaks) * 2)} bpm (Normal Range is 60 - 100 bpm) </norm>", unsafe_allow_html= True)
        st.markdown(f"<norm>Number of R-peaks detected: {len(peaks)}</norm>", unsafe_allow_html= True)

    if (rmssd) > 89 or (rmssd) < 20:
        st.markdown(f"<ab>RMSSD(Root Mean Square of Successive Differences): {rmssd} ms (Normal Range is 20 - 89 ms) </ab>", unsafe_allow_html= True)
    else :
        st.markdown(f"<norm>RMSSD(Root Mean Square of Successive Differences): {rmssd} ms (Normal Range is 20 - 89 ms) </norm>", unsafe_allow_html= True)
    

    # Mark detected R-peaks
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df[time_col], df[ecg_col], label="ECG Signal", color="blue")
    ax.plot(df[time_col].iloc[peaks], df[ecg_col].iloc[peaks], "rx", label="R-Peaks")
    ax.set_title("R-Peak Detection")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Voltage (mV)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    
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

