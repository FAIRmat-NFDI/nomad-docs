# How to transfer project ownership in the GUI

Transfer ownership of a project you own to another user in the GUI. For the API workflow, the
underlying model, and the case where a project was shared with you, see
[Transfer project ownership via the API](../program/transfer_ownership.md).

## Offer ownership (current owner)

1. Open the project you own and go to its **Settings** (for a group, use the group page).
1. Choose **Transfer ownership**.
1. Search for and select the target user.
1. Confirm. A pending request is created and the recipient is notified; you can **cancel** it from
   the same place until it is accepted.

## Accept or refuse (recipient)

1. You receive an in-app notification that you have been offered ownership of the project (you also
   gain read access to it while the request is pending).
1. Open the project and choose **Accept** to take ownership, or **Refuse** to decline.

On acceptance, you become the project's owner. On refusal, ownership stays with the original owner
and the temporary access is removed.

!!! note
    You can only transfer a project you own. If a project was shared with you (you are a coauthor
    or reviewer, not the owner), you cannot transfer it — the owner must initiate the transfer.
    To manage a shared project's collaborators programmatically, see
    [Transfer project ownership via the API](../program/transfer_ownership.md#when-the-project-was-shared-with-you).
