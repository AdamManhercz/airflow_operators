from setuptools import setup, find_packages

with open('./requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="airflow-github-operators",
    version="0.1.0",
    description="Custom GitHub operators for Airflow",
    author="Adam Manhercz",
    url="https://github.com/AdamManhercz/airflow_operators",
    python_requires='>=3.10',
    packages=find_packages(where="airflow_advanced"),
    package_dir={"": "src"},
    install_requires=requirements,
)
