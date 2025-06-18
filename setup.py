from setuptools import find_packages,setup

setup(name="RALF-TRADING-AGENTIC-SYSTEM",
      version="0.01",
      author="adarsh",
      author_email="adarshsmenon28@gmail.com",
      packages=find_packages(),
      install_requires=['lancedb','langchain','langgraph','tavily-python','polygon'],
    )