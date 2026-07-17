# Architecture

## High-Level Architecture

```text
Customer
    |
    v
Django Support Portal
    |
    v
Django REST API
    |
    v
PostgreSQL + Redis
    |
    v
Future LangGraph Workflow Engine
    |
    v
Future Multi-Agent Platform
Core Components
Django

Django is the system of record.

It will manage:

users
tenants
customers
tickets
approvals
audit logs
agent runs
PostgreSQL

PostgreSQL stores durable application data.

Redis

Redis will support:

cache
Celery queues
workflow state
agent memory
LangGraph

LangGraph will orchestrate future AI agents.

MCP

MCP will provide secure tool access for agents.

Langfuse

Langfuse will provide AI observability.

Week 1 Scope

Week 1 only builds:

Django
Docker
PostgreSQL
Redis
health endpoint
project structure

**What it does:** documents the system architecture.

---
