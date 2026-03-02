# DatabricksHRAssistantAgent

👤 Employee opens Databricks App (SSO login)
              │
              ▼
    ┌─────────────────────┐
    │   Gradio Chat UI    │
    │  (Databricks App)   │
    └─────────┬───────────┘
              │
              ▼
    ┌─────────────────────┐
    │  Sensitivity        │
    │  Classifier (LLM)   │◄── Runs BEFORE agent acts
    └─────────┬───────────┘
              │
     ┌────────┴────────┐
     │                 │
  Sensitive        Not Sensitive
     │                 │
     ▼                 ▼
┌─────────┐    ┌───────────────┐
│ Alert   │    │  HR Policy    │
│ Email + │    │  Agent        │
│ Ticket  │    │  (LangChain)  │
└─────────┘    └──────┬────────┘
                      │
         ┌────────────┼─────────────┐
         │            │             │
         ▼            ▼             ▼
  ┌────────────┐ ┌─────────┐ ┌──────────┐
  │  Vector    │ │  Genie  │ │ osTicket │
  │  Search    │ │  Space  │ │   API    │
  │ (Policy    │ │ (Live   │ │ (Formal  │
  │  PDFs)     │ │  Data)  │ │ Tickets) │
  └─────┬──────┘ └────┬────┘ └────┬─────┘
        │             │           │
        └─────────────┴───────────┘
                      │
                      ▼
           ┌─────────────────────┐
           │   MLflow Serving    │
           │   Endpoint (CPU +   │
           │   Scale to Zero)    │
           └─────────┬───────────┘
                     │
                     ▼
           ┌─────────────────────┐
           │   Unity Catalog     │
           │   Governance + RLS  │
           │   + Audit Logs      │
           └─────────────────────┘