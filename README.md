# ONET-Data-Collector

## Introduction
ONET-Data-Collector is the data ingestion and normalization layer of a larger AI-powered career intelligence pipeline. It programmatically interfaces with the O*NET Web Services API to collect occupation-level labor and skills data, resolve keyword-based career queries, retrieve detailed job metadata, and transform semi-structured API responses into clean machine-readable artifacts for downstream analytics and ML workflows.

This repository is designed like a lightweight ETL system for career data. It handles occupation discovery, API extraction, schema flattening, and export to structured formats such as JSON and CSV. In practice, it turns raw O*NET responses into a reusable feature layer that can feed recommendation engines, semantic search systems, career matching models, LLM workflows, and labor market analytics tools.

Rather than treating O*NET as a static reference database, this project treats it as a queryable knowledge source that can be operationalized into real software. The result is a modular backend component for building AI-native career products.

## Features
- Keyword-based occupation discovery using the O*NET API
- Automated retrieval of detailed occupation metadata and job descriptions
- Structured data extraction from semi-structured API responses
- JSON and CSV export for downstream analytics and modeling
- Schema flattening and normalization for easier feature engineering
- Reusable data collection pipeline for career recommendation systems
- Clean separation between search, fetch, and export steps
- Supports building downstream systems such as:
- - semantic career search
- - skill-to-role matching
- - career recommendation engines
- - LLM-powered career assistants
- - labor market analytics dashboards

## Installation
To install ONET-Data-Collector, clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/ONET-Data-Collector.git
cd ONET-Data-Collector
pip install -r requirements.txt
