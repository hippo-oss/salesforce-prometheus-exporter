from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    "click~=8.0.3",
    "click-plugins>=1.1.1",
    "prometheus-client==0.13.1",
    "SalesforcePy==2.0.0",
    "Flask==2.0.3",
]

setup(
    name="salesforce-prometheus-exporter",
    version="0.0.1",
    author="Hippo Engineering",
    author_email="infrabot@hippo.com",
    description="Fetches logs from Salesforce & creates a custom exporter, which can be scraped by prometheus.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hippo-oss/salesforce-prometheus-exporter",
    install_requires=install_requires,
    entry_points={"console_scripts": ["salesforce-exporter=cli.main:main"]},
    project_urls={
        "Bug Tracker": "https://github.com/hippo-oss/salesforce-prometheus-exporter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
