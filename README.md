# AgriSaarthi: Agentic AI Advisor for Indian Agriculture

## Project Overview

**AgriSaarthi** is a multilingual, agentic AI-powered advisor designed to empower Indian farmers and agricultural stakeholders. It provides hyperlocal, timely, and context-sensitive advice by aggregating public datasets (weather, soil health, crop advisories, market prices, government schemes) and leveraging advanced AI frameworks. It is built to operate both online and offline, ensuring accessibility even in low-connectivity rural regions.

***

## Table of Contents

- Project Features
- Architecture
- Getting Started
- Usage
- Interface Channels
- No-Code Platform Implementation
- Analysis & Visualization
- Contributing
- License
- Contact

***

## Project Features

- **Agentic AI**: Autonomous, context-aware recommendations using retrieval-augmented generation and hybrid rule-based/LLM logic.
- **Multimodal Input**: Accepts queries in local languages via text or speech (ASR-supported), including code-switched and colloquial language.
- **Data Integration**: Seamlessly accesses and merges public agricultural APIs and datasets for weather, prices, crop cycles, and schemes.
- **Explainable Outputs**: All advice is accompanied by reasoning, source citations, and visualizations.
- **Edge Support**: Basic Q&A functionality available for offline users via cached or embedded datasets.
- **Scalable Accessibility**: Available via WhatsApp, web app, SMS, and IVR.
- **User-Centric Design**: Wireframed interfaces for diverse user demographics.
- **Continuous Learning**: User feedback for iterative model refinement.

***

## Architecture

```
[User Device]
      ↓
[Multimodal Input Handler (Text/ASR)]
      ↓
[Query Classifier]
      ↓
[Data Aggregator]
      ↓
[Knowledge Graph]
      ↓
[RAG Pipeline (LLM + Rules)]
      ↓
[Explainability/Visualization Module]
      ↓
[User Channel: WhatsApp/Web/SMS/IVR]
```

***

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/anushka369/AgriSaarthi.git
   cd AgriSaarthi
   ```

2. **Installation**

   - This project uses no-code platforms like n8n, Flowise, and Twilio.  
   - Refer to the `/docs/setup.md` for step-by-step setup on preferred platform.
   - For local deployment, ensure Docker is installed (for running services offline).

3. **Configuration**

   - Configure API keys for public agricultural data sources (weather, crop, prices).
   - Set up Twilio/WhatsApp credentials for chat integration.
   - Add language models and ASR API credentials for multimodal support.
   - Setup SQLite for local data caching.

***

## Usage

- Interface supports queries via WhatsApp, web chatbot, SMS, and IVR.
- Users can seek advice on crop selection, yield optimization, government schemes, pest control, and market rates.
- All answers are generated with contextual reasoning, source citations, and simple visualizations.

***

## Interface Channels

- **WhatsApp**: message AgriSaarthi, receive real-time advisories.
- **Web App**: user-friendly dashboard for submitting queries and reviewing visualizations.
- **SMS**: for regions with low smartphone penetration.
- **IVR**: voice-based support in local languages.

***

## No-Code Platform Implementation

- Workflows orchestrated using **n8n**: API integration, ML model calls, multi-channel responses.
- Document retrieval and semantic search handled by **Flowise** or **VectorShift**.
- WhatsApp and SMS powered by **Twilio**.
- Data visualization created using **Chart.js** or Python charting libraries for interfaces.

***

## Analysis & Visualization

- Crop yield trends and market prices visualized via dynamically generated charts and heat maps.
- Usage analytics collected in the backend for ongoing performance assessment.
- User feedback and model accuracy metrics tracked for continuous improvement.

***

## Contributing

We welcome contributions!  
- Fork the repo and create a feature branch.
- Submit a pull request explaining your changes.
- For questions/discussion, open an issue.

***

## License

This project is open source under the MIT License.  
See the `/LICENSE` file for full terms.

***
