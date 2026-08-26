# Open-Source Record

**Maintainer:** Mohammad Mehdi Roshani ([@moroshani](https://github.com/moroshani))

**Verified:** 2026-08-26

This page separates projects I own and maintain from work submitted to other
maintainers. Forks under `moroshani` are contribution workspaces, not projects I
claim as my own.

## Owned And Maintained

### Solar Hijri Calendar Component

- [Source](https://github.com/moroshani/solar-hijri-calendar-component)
- [Live testing lab](https://moroshani.github.io/solar-hijri-calendar-component/)
- [v0.1.0 source release](https://github.com/moroshani/solar-hijri-calendar-component/releases/tag/v0.1.0)
- Purpose: reusable, accessible Solar Hijri/Jalali date behavior for Persian and
  RTL applications.
- Stack: TypeScript, React, Vite, Vitest, Playwright, and `jalaali-js`.
- Verified surface: controlled single, range, and multiple selection; month and
  year navigation; framework-neutral date/selection helpers; Persian and English
  labels; RTL presentation; ESM, CommonJS, TypeScript, React, and CSS exports.
- Release evidence: clean install, zero-vulnerability audit, TypeScript, 22 unit
  tests, two builds, 25 browser interactions, five visual captures, package
  inspection, consumer smoke testing, CI, Pages, and CodeQL passed.
- Honest status: npm publication and external adoption are not claimed yet.

### SetadInfo

- [Source](https://github.com/moroshani/setadinfo)
- [Synthetic browser demo](https://moroshani.github.io/setadinfo/)
- Purpose: Persian RTL monitoring workbench for Iranian public purchase, tender,
  and auction opportunities.
- Stack: FastAPI, Python, PostgreSQL, Redis, Celery, React, TypeScript, Vite,
  TanStack Router/Query, Docker Compose, and Nginx.
- Verified surface: filtered search, saved monitoring tasks, history and change
  inspection, notifications, roles, diagnostics, migrations, CI, CodeQL, and
  dependency automation.
- Release evidence: 53 backend tests and fresh migration; 42 frontend tests,
  lint, production/demo builds, dependency audits, responsive browser QA, CI,
  CodeQL, and demo isolation checks passed.
- Honest status: the maintainer is the current user; there is no tagged release
  or public-adoption claim yet.

### Dominoyar

- [Public product and support repository](https://github.com/moroshani/Dominoyar)
- Role: public information, support, privacy, and future release material for a
  Persian RTL domino scorekeeper. It is not a public source repository.

## Merged Upstream Work

| Project | Result |
| --- | --- |
| [pandas `#66600`](https://github.com/pandas-dev/pandas/pull/66600) | Corrected missing-value handling for NumPy bytes dtypes. |
| [Persian Calendar `#1879`](https://github.com/persian-calendar/persian-calendar/pull/1879) | Fixed month-title overflow at large Android font scales with an exact UI regression test. |
| [Floci `#2268`](https://github.com/floci-io/floci/pull/2268) | Preserved Docker image-inspection failures; shipped in Floci `1.7.0`. |
| [InfluxData docs `#7524`](https://github.com/influxdata/docs-v2/pull/7524) | Repaired broken InfluxDB 3 documentation fragments. |
| [frontend-reference `#139`](https://github.com/nanlabs/frontend-reference/pull/139) | Added React Router type examples and generated-doc integration. |

## Work Under Review

Live state was rechecked through GitHub immediately before this update.

| Project | Current evidence |
| --- | --- |
| [pandas `#66601`](https://github.com/pandas-dev/pandas/pull/66601) | Mergeable and fully green at `ce5a64bf25`; waiting for maintainer review. |
| [pandas `#66603`](https://github.com/pandas-dev/pandas/pull/66603) | Mergeable and fully green at `802cf90cb9`; review response published and awaiting re-review. |
| [Moss `#438`](https://github.com/usemoss/moss/pull/438) | Mergeable with successful hosted checks; waiting for review. |
| [Storybook MCP `#366`](https://github.com/storybookjs/mcp/pull/366) | Mergeable with successful hosted checks; waiting for review. |
| [APILens `#207`](https://github.com/apilens/apilens/pull/207) | Mergeable; GitHub reports no hosted check rollup. |
| [OpenEverest `#3002`](https://github.com/openeverest/openeverest/pull/3002) | Mergeable with successful hosted checks; waiting for review. |

## Maintainer Handoff

- [Persian Calendar issue `#1256`](https://github.com/persian-calendar/persian-calendar/issues/1256): the current-upstream fix passed formatting, JVM tests, Android-test assembly, and the exact API 29 instrumentation test. It was delivered through the issue because external contributors cannot open the PR directly.

## Engineering Practice

- Select work by usefulness, reproducibility, ownership, and verifiability rather
  than submission frequency.
- Check contributor intent, duplicates, repository policy, internal callers, and
  behavioral impact before implementation.
- Add regression evidence, run affected suites and required final gates, and
  communicate in the project's language and conventions.
- Use Codex and other AI tools transparently while personally reviewing,
  understanding, testing, and owning every submitted change.
