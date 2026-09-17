# Ownership transfer

Every upload (shown as a *project* in the GUI) has a single **main author** — its owner.
Ownership transfer reassigns that role from the current owner to another user. Because it
changes who controls the data, it is deliberately a **two-phase, request-based** operation
rather than an immediate reassignment: the current owner *offers* ownership, and the
prospective owner must *accept* before anything changes.

## The two-phase model

A transfer moves through two steps:

1. **Request.** The current owner initiates a transfer, naming the target user. The upload is
   not reassigned yet; a pending request is recorded.
2. **Response.** The target user accepts or refuses. On acceptance, the `main_author` is
   reassigned to the target. On refusal, nothing changes. While the request is still pending,
   the original owner can cancel it.

Only the current owner can initiate a transfer, and only the named target can respond to it.
Either party can inspect the pending request, and only the source can cancel it.

## Access while a request is pending

When a request is created, the target is immediately granted **reviewer (read) access** to
the upload, before deciding whether to accept. This lets the prospective owner inspect the
data before taking responsibility for it. Cancelling the request revokes that temporary
access; accepting it completes the reassignment and clears the temporary reviewer grant.

## Notifications

Transfers are surfaced through **in-app notifications** in the GUI: the target is notified
when they are offered ownership, and the source is notified if the target refuses. **No email
is sent** for any step. A user who does not see the in-app notification can still discover a
pending transfer by listing their transfers through the API, or by noticing that the upload
has appeared among the data shared with them.

## Identifying the target

The target user can be identified by `user_id`, `username`, or `email`. The GUI resolves the
user you pick to their `user_id`; when using the API directly you choose which identifier to
supply.

## Permissions

The read-only steps (listing and inspecting transfers) require only read access, while the
three state-changing steps — requesting, responding, and cancelling — require write access to
uploads. A token without write scope can inspect transfers but cannot create, accept, or
cancel one.

## Groups

The same request-and-accept model applies to transferring ownership of a **group**, with the
group owner (or an administrator) initiating and the target member accepting.

See [How to transfer upload ownership](../howto/manage/transfer_ownership.md) for the
concrete steps in the GUI and through the API.
