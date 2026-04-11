# ONET-Data-Collector

## Overview

ONET-Data-Collector is the ingestion, extraction, and normalization layer of a larger AI-powered career intelligence pipeline built on top of O*NET Web Services. The repository is designed to programmatically convert raw O*NET occupational data into structured, machine-readable artifacts that can serve as the foundation for recommendation systems, semantic career search, LLM-powered career assistants, skill-to-role matching engines, and broader labor-market intelligence workflows.

At a high level, this repository behaves like a lightweight ETL system for occupational data. It handles authenticated API interaction, keyword-based occupation discovery, full occupation-detail retrieval, raw JSON preservation, schema flattening, and export into stable analytics tables. Instead of treating O*NET as a static government dataset that must be inspected manually, this project treats it as a programmable knowledge source that can be turned into reusable software infrastructure.

The repository is especially useful for building AI-native education or workforce software because most downstream AI systems do not operate well on raw nested API responses. They need normalized, structured, and retrieval-friendly data. ONET-Data-Collector provides that transformation layer.

---

## Why This Repository Exists

Raw O*NET data is rich, but it is not directly optimized for modern AI or product workflows.

O*NET responses are often:
- nested and semi-structured
- difficult to query efficiently across many occupations
- awkward to feed into ranking or recommendation logic
- poorly suited for direct use in retrieval pipelines or LLM context construction
- inconsistent with the flattened tabular formats preferred in data science and product analytics

This repository solves that problem by turning raw O*NET API responses into reusable occupational intelligence artifacts.

That means the output of this repository can be used as:
- a career feature store
- a structured backend for career search
- a source of occupational metadata for recommendation engines
- a retrieval corpus for LLM and RAG-style career systems
- a canonical occupational dataset for downstream analytics and model development

---

## Core System Role

This repository is the **data ingestion and normalization layer** of the broader O*NET career intelligence stack.

Its primary responsibilities are:

1. **Occupation discovery**
   - Query the O*NET API using keywords
   - Identify matching occupations and extract occupation identifiers
   - Build a seed index of roles for downstream expansion

2. **Full occupation retrieval**
   - Pull detailed occupational records for each discovered O*NET code
   - Preserve raw responses for traceability and reproducibility
   - Maintain a lossless raw JSON layer that can be reprocessed later

3. **Schema flattening and normalization**
   - Convert nested O*NET structures into analytics-friendly tables
   - Standardize fields across occupations
   - Create clean, downstream-ready CSV/JSON outputs

4. **Foundation for AI and recommendation workflows**
   - Produce stable structured data that can be consumed by search, matching, clustering, and LLM pipelines
   - Reduce friction between public labor data and product-grade AI workflows

---

## Technical Architecture

The pipeline is structured as a staged data workflow rather than a single monolithic script.

### Stage 1: Authenticated O*NET API Access
The system interfaces with O*NET Web Services using authenticated HTTP requests. A lightweight API wrapper standardizes request construction, authentication, endpoint calls, response parsing, and error handling so that the rest of the pipeline remains data-driven and modular.

This wrapper makes it easier to:
- construct valid endpoint requests
- encode and send credentials
- parse JSON responses consistently
- surface structured O*NET API errors
- isolate transport logic from data transformation logic

### Stage 2: Keyword-Driven Occupation Discovery
The first practical data collection step is occupation discovery. The system submits keyword-driven search queries to O*NET endpoints and returns candidate occupations, typically including identifiers such as occupation code and title.

These search results are consolidated into a seed dataset that acts as the starting point for downstream collection. This stage is especially important because it bridges user-facing language such as “data scientist,” “designer,” or “healthcare” into formal O*NET occupation records that can later be analyzed or recommended.

### Stage 3: Full Occupation Record Pulls
After a seed set of occupation codes is collected, the pipeline retrieves detailed O*NET documents for each occupation. These raw records contain the richer occupational information needed for real intelligence systems, including structured descriptors and deeper domain-specific metadata.

This stage is intentionally designed to preserve the raw response layer. Raw JSON is stored as an audit and reproducibility artifact so that:
- transformations can be revisited without recollecting data
- schemas can evolve over time
- downstream tables can be regenerated from source records
- debugging is easier because raw and processed views can be compared directly

### Stage 4: Schema Condensation and Flattening
Raw O*NET documents are information-rich but not convenient for analytics or AI systems. The pipeline therefore condenses nested structures into flattened outputs keyed by occupation.

Depending on the fields retrieved, this flattening process can pull and standardize information such as:
- occupation identifiers and titles
- descriptions and summaries
- tasks
- skills
- abilities
- knowledge areas
- work activities
- technology/tool references
- job zone and preparation characteristics
- education-related descriptors
- interests, work styles, and work values
- related occupations and role adjacency information

The result is a stable structured dataset that behaves much more like a machine-readable feature table than an API dump.

---

## AI / LLM Relevance

This repository's real value is that it creates a structured knowledge layer that AI systems can actually use.

The outputs are well suited for:
- **career recommendation engines** that score or rank occupations based on interest, skills, or query context
- **semantic search systems** that map natural-language student queries onto relevant occupations
- **LLM context enrichment** where structured occupational profiles are inserted into prompts or retrieval results
- **RAG pipelines** where O*NET records become a curated retrieval source for model-grounded responses
- **agentic education software** that needs normalized career entities and descriptors rather than raw web content
- **explainable matching systems** where recommended occupations can be justified using explicit skills, descriptors, and related features

In other words, this repository turns O*NET from a reference API into an AI-ready occupational data backbone.

---

## Repository Outputs

The repository is designed to produce stable artifacts that can be used in other systems without re-hitting the API every time.

Typical outputs include:
- keyword search result tables
- raw occupation-detail JSON
- condensed occupation-detail CSV tables
- processed machine-readable role datasets for downstream analytics or product integration

These outputs support both experimentation and operational reuse.

---

## Representative Workflow

A typical end-to-end run looks like this:

1. Submit keyword queries to O*NET
2. Extract matching occupation codes and titles
3. Build a seed occupation index
4. Retrieve full detailed records for each occupation
5. Preserve the raw JSON layer
6. Flatten and normalize nested fields
7. Export final CSV/JSON artifacts for downstream use

This structure makes the system easy to reason about, extend, and repurpose for new product needs.

---

## Use Cases

ONET-Data-Collector can serve as the backend data layer for:
- K–12 career exploration platforms
- EdTech career recommendation products
- labor-market analytics tools
- role similarity and skill-matching systems
- LLM-powered career advisors
- occupational retrieval and ranking pipelines
- internal feature services for workforce intelligence products

---

## Project Role in the Larger Stack

This repository is the first half of a broader two-repository system:

- **ONET-Data-Collector** = ingestion, extraction, normalization, and structured output generation
- **data-science-onet** = analytics, feature inspection, clustering, and recommendation-oriented intelligence generation

Together, the two repositories form a modular O*NET career intelligence pipeline that transforms public labor-market data into AI-ready infrastructure for education software.
