# Recovery case study: repository alias and prior strategy

## Situation

A repository named `poplar.agency` contained only an initial README, LICENSE, and `.gitignore`, while the prior conversation described a neighborhood marketing agency and a Neighborhood Passport strategy.

## Reliable sequence

1. Verify the SSH remote with `git ls-remote` before cloning or pushing.
2. Clone and inspect files, recent history, branches, and status.
3. Search session history using both the repository slug (`poplar.agency`) and the earlier product/business terms (`neighborhood marketing agency`, `Neighborhood Passport`).
4. Recover the earlier strategy artifact from the session's completed file-writing operation rather than recreating it from memory.
5. Add the recovered strategy document and a README that explains the relationship between Poplar (agency) and Neighborhood Passport (working product/program).
6. Commit, push, and verify the remote `main` ref SHA.

## Lesson

An empty destination repository is not evidence that the project lacks requirements. Repository identity and project identity may be aliases; conversation history can contain the authoritative strategy even when the repository does not.
