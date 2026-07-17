# CLAUDE.md

## Project

multi-agent-aI-platform-for-enterprise-support-operations

A production-grade Enterprise AI Support Engineering Platform using Django, LangGraph, MCP, Agentic RAG, Langfuse, MLOps, AgentOps, and human-in-the-loop governance.

## Architecture Rules

1. Django is the system of record.
2. LangGraph is the workflow orchestration engine.
3. MCP is the controlled tool-access layer.
4. PostgreSQL stores durable business data.
5. Redis supports caching, queues, and workflow state.
6. Every AI agent action must be auditable.
7. Every risky action requires human approval.

## Django Rules

- Keep views thin.
- Put business logic in services.
- Use serializers for API validation.
- Use migrations for schema changes.
- Every tenant-owned model must support tenant isolation.
- Never bypass authorization checks.

## Testing Rules

- Write tests before new behaviour.
- Every bug fix needs a regression test.
- Run pytest before committing.
- Run ruff before committing.

## Security Rules

- Never expose secrets.
- Never log API keys or tokens.
- Redact PII.
- Protect tenant boundaries.
- Reject prompt injection attempts.
- Use environment variables for secrets.

## Agent Rules

- Agents must return structured JSON.
- Agent runs must be logged.
- Agents must not access tools directly.
- Tool access must go through MCP.
- Low-confidence outputs must escalate.

## Prompt Rules

- Prompts must be versioned.
- Prompts must be evaluated.
- Prompts must be observable through Langfuse.