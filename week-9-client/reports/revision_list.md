# Dashboard v1 Revision List

**Basis:** Initial dashboard QA plus the illustrative heuristic review in `peer_heuristic_review_log.md`. Items labelled “sample review” must be validated with an actual peer.

| ID | Revision / action | Priority | Status for v1 |
|---|---|---|---|
| R1 | Confirm and display the currency/unit for `Total_Revenue`; until confirmed, retain “source units”. | High | Open — requires source owner |
| R2 | Add the confirmed data refresh/as-of date to the dashboard header. | Medium | Open — source date not supplied |
| R3 | Add KPI definitions for sold rate, churn rate, and gross margin to the dashboard glossary. | Medium | Included in report notes; improve in v2 |
| R4 | Add a product-level stock-risk table for the five products where stock is below average monthly sales. | High | Planned for v2 |
| R5 | Validate city sold-rate comparisons with listing type and transaction mix. | Medium | Planned for v2 |
| R6 | Test chart readability, contrast, and responsive layout on desktop and mobile. | Medium | Manual QA required |
| R7 | Obtain one real peer review and replace the sample review notes with actual comments and evidence. | High | Pending actual peer review |

## Recommended v2 acceptance criteria

- Revenue unit and source refresh date are confirmed and displayed.
- Peer review is completed by one named reviewer, with date and evidence recorded.
- Stock-risk table lists product IDs, category, stock units, monthly sales, and stock gap.
- City comparisons include context on property and transaction mix.
- Dashboard passes desktop and mobile readability checks.
