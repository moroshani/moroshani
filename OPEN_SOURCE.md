# Open-Source Maintenance

**Maintainer:** Mohammad Mehdi Roshani ([@moroshani](https://github.com/moroshani))  
**Status date:** 2026-08-08

I maintain two public MIT-licensed projects and contribute tested fixes to projects maintained by other teams. The projects are early, so this page separates implemented work from adoption and future plans.

## Maintained Projects

### SetadInfo

- Source: https://github.com/moroshani/setadinfo
- Deployed application: https://setadinfo.ariaprojectsdashboard.ir
- Purpose: a Persian RTL workbench for searching, saving, and monitoring Iranian public purchase, tender, and auction opportunities.
- Stack: FastAPI, Python, PostgreSQL, Redis, Celery, React, TypeScript, Vite, TanStack Router and Query, Tailwind CSS, Docker Compose, and Nginx.
- Implemented surface: filtered search, saved monitoring tasks, baseline and delta tracking, listing and offer history, change inspection, notifications, role-based access, run diagnostics, migrations, CI, CodeQL, and dependency automation.
- Verification: 51 backend tests, a fresh Alembic migration, 84 browser tests, frontend lint and production build, dependency audits, responsive QA from 320px to 1440px, and GitHub CI and CodeQL all pass. GitHub currently reports no open dependency or code-scanning alerts.
- Current adoption: the application is in active development and currently used only by its maintainer for real workflow and reliability testing. I do not claim public adoption yet.
- Near-term work: strengthen acquisition and notification reliability, expand contract tests, reduce the main frontend bundle, prepare the first tagged release, and make the codebase easier for Persian-speaking contributors to enter.

### Solar Hijri Calendar Component

- Source: https://github.com/moroshani/solar-hijri-calendar-component
- First source release: https://github.com/moroshani/solar-hijri-calendar-component/releases/tag/v0.1.0
- Live demo: https://moroshani.github.io/solar-hijri-calendar-component/
- Purpose: reusable, accessible Solar Hijri / Jalali date behavior for Persian and RTL applications.
- Stack: TypeScript, React, Vite, Vitest, Playwright, and `jalaali-js`.
- Implemented surface: controlled single, range, and multiple selection; framework-neutral date math, constraints, and selection helpers; Persian and English labels; RTL presentation; ESM, CommonJS, TypeScript, React, and CSS package exports.
- Verification: clean dependency install, zero known audit vulnerabilities, TypeScript checks, 22 unit tests, two production builds, 15 responsive interaction tests, 5 visual captures, package-content inspection, and a separate consumer smoke test all passed for `0.1.0`. GitHub CI, Pages deployment, and CodeQL are green with no open security alerts.
- Current adoption: the first GitHub source release is public. npm publication is still pending, and there are no external users or download claims yet.
- Near-term work: complete the first registry release, deepen date-correctness and accessibility coverage, continue extracting a framework-neutral core, and add carefully tested adapters without fragmenting calendar behavior.

## Upstream Contributions

Merged work includes:

- [persian-calendar/persian-calendar#1879](https://github.com/persian-calendar/persian-calendar/pull/1879): fixed a Gregorian month-title overflow at large Android font scales and added an exact UI regression test.
- [nanlabs/frontend-reference#139](https://github.com/nanlabs/frontend-reference/pull/139): added and integrated React Router type guidance.
- [influxdata/docs-v2#7524](https://github.com/influxdata/docs-v2/pull/7524): repaired broken documentation fragments and anchors.

Maintainer-ready work under review includes fixes for pandas bytes shifts, converter behavior, and JSON table labels, plus contributions to Moss, Storybook MCP, and APILens. Direct links and current statuses are kept in the [profile README](./README.md).

## Maintenance Practice

- Select work by usefulness, reproducibility, and the ability to verify behavior, not by language or contribution-count targets.
- Check ownership, active contributor intent, related pull requests, repository policy, internal callers, and behavioral impact before taking an issue.
- Keep changes focused, add regression coverage, run the relevant broader suites, and communicate in the project's language and conventions.
- Welcome responsible AI-assisted contributions when the contributor reviews, understands, discloses, and tests the result.

I use Codex and other AI tools for codebase research, implementation, tests, documentation, and review preparation. I remain responsible for every decision and public submission under my account.

## Direction

The goal is to turn both maintained projects into dependable, contributor-friendly infrastructure while continuing useful work in the Persian software community and in high-standard worldwide projects. Public support would be spent on deeper verification, release work, accessibility, documentation, and substantial maintainer-ready contributions rather than artificial activity.
