import os
import sys
from datetime import datetime
from crew import NewsReporter

def run():
    """
    Run the NewsReporter crew.
    """
    inputs = {
        "topic": "Deloitte Insights on AI"
    }
    result = NewsReporter().run(inputs=inputs)

    # Create the report directory if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    # Get the current date and time for the file name
    current_datetime = datetime.now().strftime("%B_%Y")
    formatted_datetime = datetime.now().strftime("%d%m%Y_%H-%M")
    formatted_topic = inputs['topic'].replace(" ", "_").lower()
    report_file_path = f"reports/{formatted_topic}_{formatted_datetime}.md"

    # Convert result to string if necessary (adjust this based on how you want to format the output)
    report_content = str(result)  # Replace this with the actual content extraction from result

    print("Current Working Directory:", os.getcwd())
    print("Report Path:", report_file_path)

    # Write the generated report to the file
    with open(report_file_path, 'w') as file:
        file.write(report_content)

    print("News Report Generated:", report_file_path)

if __name__ == "__main__":
    run()