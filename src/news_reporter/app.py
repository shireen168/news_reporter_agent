import streamlit as st
import os
from datetime import datetime
from crew import NewsReporter

def generate_report(topic):
    inputs = {"topic": topic}
    result = NewsReporter().run(inputs=inputs)
    report_content = str(result)  # Replace this with the actual content extraction from result
    return report_content

st.title("News Research")
# Input field for topic
user_topic = st.text_input("Enter the topic for the report:", placeholder="Enter the topic here")

# Button to generate report
if st.button("Generate Report"):
    report = generate_report(user_topic)
    st.markdown(report)  # Display the report content in Markdown format
    report_filename = f"{user_topic.replace(' ', '_').lower()}_{datetime.now().strftime('%d%m%Y_%H-%M')}.md"
    report_path = os.path.join('reports', report_filename)
    os.makedirs("reports", exist_ok=True)
    with open(report_path, 'w') as file:
        file.write(report)
    st.success(f"Report generated: {report_filename}")
    st.download_button("Save Report", report, file_name=report_filename, mime="text/markdown")
