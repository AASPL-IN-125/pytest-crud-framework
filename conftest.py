import pytest
import os
import logging
from datetime import datetime

def pytest_configure(config):
    report_dir = r"D:\API_auto_project\API_CURD\reports"
    os.makedirs(report_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = os.path.join(report_dir, f"report_{timestamp}.html")

    config.option.htmlpath = report_file
    config.option.self_contained_html = True

    # configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )