# Security Policy

## Reporting Security Issues

This is a public evaluation repository for SIH 2026 purposes.
The production codebase is maintained in a private repository.

**Do NOT open public GitHub issues for security vulnerabilities.**

If you discover a security issue in the public evaluation materials,
please contact: aryanf192811@gmail.com

---

## What This Repository Contains

This repository contains:
- Documentation (Markdown files)
- Real screenshots captured from live portals
- Architecture diagrams (PNG/SVG)
- Testing and QA reports (Markdown)

## What This Repository Does NOT Contain

- Source code
- Environment variables or `.env` files
- API keys, tokens, or credentials
- Database passwords or connection strings
- JWT secrets
- Twilio, Gemini, or OpenWeatherMap API keys
- Private deployment configuration
- Production database dumps
- Any PII or real user data

## Security Decisions in the Production Codebase

For details on the security architecture of the actual system, see:
- [`docs/testing/09-security-audit.md`](./docs/testing/09-security-audit.md) — Full security audit report
- [`docs/architecture/architecture.md`](./docs/architecture/architecture.md) — Security stack section

Key verified security properties (from adversarial testing):
- Parameterized SQL throughout (SQL injection tested and held)
- JWT HS256 algorithm-pinned
- bcrypt (12 rounds) for passwords
- SHA-256 for govt ID hashing (plaintext never stored)
- CORS whitelist-only
- Rate limiting (auth: 5/15min, general: 100/15min)
- Twilio webhook signature verification
- RBAC enforced server-side with `requireGovtRole()` middleware
