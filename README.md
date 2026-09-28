# lab04--Hello-Kitties-

## Who Did What

| Member | Part | Contribution |
| Ko Koe | A & E | Repository setup, shared fixture, README and final checks |
| Thuta Toe | B | Withdrawal and overdraft tests |
| Kaung Min Thant | C | Yield fixture with setup and teardown |
| Aung Ko Latt | D | Test using the shared fixture |

## Our Merge Conflict

We encountered a merge conflict while working on the same repository. Git showed conflict markers such as `<<<<<<<`, `=======`, and `>>>>>>>` to separate the conflicting changes.

The team checked both versions and decided which changes should be kept. We kept the correct project changes, completed the merge, and ran the tests again to make sure everything still worked.

Git could not resolve the conflict automatically because the changes conflicted with each other, so Git could not decide which version the team wanted to keep.

## Git Contribution Summary

Output of `git shortlog -sn`:

4  Ko Koe
3  Aung Ko Latt
3  Hookie23
3  Kokoe-Frenky
3  Thuta Toe

`Ko Koe` and `Kokoe-Frenky` are the same team member, Ko Koe. `Hookie23` is Kaung Min Thant.

## Reflection Questions

### 1. Why was your push rejected, and how did you fix it?

The push was rejected because the remote repository had changes that were not in the local repository. We pulled the latest changes, resolved the differences, and then pushed again.

### 2. Why could Git not resolve the README conflict automatically?

Git could not resolve the README conflict automatically because different changes affected the same content. Git needed us to decide which version should be kept.

### 3. What is the difference between committing and pushing?

Committing saves changes to the local Git repository. Pushing sends those commits to the remote GitHub repository.

### 4. How do fixtures reduce duplicated setup code in tests?

Fixtures let multiple tests reuse the same setup code. This avoids writing the same setup steps separately in every test.