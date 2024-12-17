import sys
from crew import NewsReporter

def run():
    """
    Run the NewsReporter crew.
    """
    inputs = {
        "topic": "Latest AI News"  
    }
    result = NewsReporter().run(inputs=inputs)
    print("News Report Generated:", result)

if __name__ == "__main__":
    run()