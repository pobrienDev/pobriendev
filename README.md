<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="840" alt="Patrick O'Brien, Software Engineer. Identity and access automation, full-stack web apps. Baltimore, MD.">
</picture>

Software engineer working on identity and access automation. Currently building
Python tooling against the Microsoft Graph API that automates account provisioning
and deprovisioning for 400+ users across 100+ properties at Habitat America,
replacing a manual, per-person setup process.

Full-stack background in React, FastAPI/Flask, and SQL, with automated test
coverage built in from the start rather than added after the fact.

[pobriendev.github.io/portfolio](https://pobriendev.github.io/portfolio) · patobrien3590@gmail.com

---

### Built

<table>
  <tr>
    <td width="50%"><a href="https://dartmetrics.onrender.com"><img src="assets/preview-dartmetrics.jpg" alt="DartMetrics live scoring screen: a 501 leg with a suggested checkout and the bot's last visit"></a></td>
    <td width="50%"><a href="https://ticket-system-azure-omega.vercel.app"><img src="assets/preview-ticket-system.jpg" alt="Ticket system queue showing tickets with priority, status, and category tags"></a></td>
  </tr>
  <tr>
    <td align="center"><b>DartMetrics</b> · <a href="https://dartmetrics.onrender.com">live demo</a> · <a href="https://github.com/pobriendev/dartmetrics">code</a></td>
    <td align="center"><b>Ticket system</b> · <a href="https://ticket-system-azure-omega.vercel.app">live demo</a> · <a href="https://github.com/pobriendev/ticket-system">code</a></td>
  </tr>
</table>

<sub>Both demos run on free tiers that sleep when idle, so the first load can take up to a minute.</sub>

- **[ticket-system](https://github.com/pobriendev/ticket-system)** — helpdesk app, React/Vite + FastAPI + PostgreSQL, JWT auth, role-based access, full audit trail. 176 backend tests, ~96% coverage. [Live demo](https://ticket-system-azure-omega.vercel.app). [![CI status](https://github.com/pobrienDev/ticket-system/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pobrienDev/ticket-system/actions/workflows/ci.yml)
- **[entra-stale-accounts](https://github.com/pobriendev/entra-stale-accounts)** — `pip install entra-stale-accounts`. Flags Entra ID accounts inactive past a set threshold, including ones that never signed in. [![Tests status](https://github.com/pobrienDev/entra-stale-accounts/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/pobrienDev/entra-stale-accounts/actions/workflows/tests.yml) [![PyPI version](https://img.shields.io/pypi/v/entra-stale-accounts)](https://pypi.org/project/entra-stale-accounts/)
- **[employee-provisioning-tool](https://github.com/pobriendev/employee-provisioning-tool)** — CLI that runs Entra ID onboarding/offboarding end to end, with dry-run mode and a full audit log so nothing happens silently. [![Tests status](https://github.com/pobrienDev/employee-provisioning-tool/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/pobrienDev/employee-provisioning-tool/actions/workflows/tests.yml)
- **[ski-resort-explorer](https://github.com/pobriendev/ski-resort-explorer)** — React + Flask, pulls live weather and precipitation data via OpenWeatherMap.
- **[dartmetrics](https://github.com/pobriendev/dartmetrics)** — darts scoring platform (501, Cricket, Halve It) with a framework-free scoring engine and event-sourced stats — every dart is stored, nothing aggregated. [Live demo](https://dartmetrics.onrender.com). [![CI status](https://github.com/pobrienDev/dartmetrics/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pobrienDev/dartmetrics/actions/workflows/ci.yml)
- **[entra-terraform](https://github.com/pobriendev/entra-terraform)** — Terraform for the Entra ID identity layer the Graph tools above run on: app registration with least-privilege permissions and admin consent as code, a rotating secret in Key Vault, locked-down remote state. CI runs `terraform plan` on every PR over OIDC with a read-only identity and no stored credentials. [![Terraform plan status](https://github.com/pobrienDev/entra-terraform/actions/workflows/plan.yml/badge.svg?branch=main)](https://github.com/pobrienDev/entra-terraform/actions/workflows/plan.yml)

<!-- next thing goes here -->

### Working with

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img src="assets/stack-light.svg" width="692" alt="Python, TypeScript, JavaScript, PowerShell, React, FastAPI, Flask, PostgreSQL, Microsoft Graph API, Microsoft Entra ID, Azure, Terraform, GitHub Actions">
</picture>
