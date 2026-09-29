# How to transfer project ownership via the API

Transfer ownership of a project (an *upload* at the API and data-model level) to another user
through the `ownership-transfers` endpoints. For the point-and-click equivalent, see
[Transfer project ownership in the GUI](../gui/transfer_ownership.md).

## What you will learn

- How ownership transfer works and who is allowed to do what.
- How to request, review, accept or refuse, and cancel a transfer through the API.

## Recommended preparation

- [Authenticate programmatically](./auth.md)

## How ownership transfer works

Every project has a single **main author** — its owner. Transfer is a **two-phase,
request-based** operation: the current owner *requests* a transfer naming a target user, and the
target must *accept* before ownership changes.

- **Request, then response.** The owner creates a request; the target accepts or refuses. On
  acceptance, `main_author` is reassigned to the target. While the request is pending, the owner
  can cancel it.
- **Access while pending.** Creating the request immediately grants the target reviewer (read)
  access so they can inspect the project before deciding; cancelling revokes it.
- **Notifications.** The GUI shows an in-app notification (to the target on request, to the source
  on refusal); no email is sent.
- **Permissions.** Only the `main_author` can initiate a transfer. A coauthor can manage the
  project's collaborators (see [When the project was shared with you](#when-the-project-was-shared-with-you))
  but cannot transfer ownership.
- **Groups.** Group ownership can be transferred with the same request-and-accept model, using
  `resource_type: group`.

The state-changing calls (request, respond, cancel) require a token with `uploads:write`.

## Request the transfer (current owner)

Identify the target by `user_id`, `username`, or `email` via `target_user_type`:

```bash
curl -X POST "{{ nomad_url() }}/v1/ownership-transfers" \
  -H "Authorization: Bearer ${NOMAD_PAT}" \
  -H "Content-Type: application/json" \
  -d '{
    "resource_type": "upload",
    "resource_id": "<upload-id>",
    "target_user": "<target-user-id>",
    "target_user_type": "user_id"
  }'
```

The response returns the `transfer_id` and the resolved source and target user IDs.

## Review the pending request (either party)

```bash
# List transfers involving you
curl "{{ nomad_url() }}/v1/ownership-transfers" \
  -H "Authorization: Bearer ${NOMAD_PAT}"

# Inspect a single transfer
curl "{{ nomad_url() }}/v1/ownership-transfers/<transfer-id>" \
  -H "Authorization: Bearer ${NOMAD_PAT}"
```

## Accept or refuse (target)

On `accept`, `main_author` is reassigned to the target:

```bash
curl -X POST "{{ nomad_url() }}/v1/ownership-transfers/<transfer-id>/respond?resource_type=upload" \
  -H "Authorization: Bearer ${NOMAD_PAT}" \
  -H "Content-Type: application/json" \
  -d '{"action": "accept"}'
```

Use `{"action": "refuse"}` to decline.

## Cancel a pending request (source)

Before the target responds, the source can cancel, which revokes the target's temporary reviewer
access:

```bash
curl -X POST "{{ nomad_url() }}/v1/ownership-transfers/<transfer-id>/cancel?resource_type=upload" \
  -H "Authorization: Bearer ${NOMAD_PAT}"
```

## Verify the result

Reassigning ownership runs as a background process on the upload. Confirm that `main_author` is
the new owner and that `process_status` completed successfully:

```bash
curl "{{ nomad_url() }}/v1/uploads/<upload-id>" \
  -H "Authorization: Bearer ${NOMAD_PAT}"
```

## Endpoint reference

| Method & path | Purpose | Required scopes |
| --- | --- | --- |
| `POST /ownership-transfers` | Request a transfer (source) | `uploads:read`, `uploads:write` |
| `GET /ownership-transfers` | List your transfers | `uploads:read` |
| `GET /ownership-transfers/{id}` | Inspect one transfer | `uploads:read` |
| `POST /ownership-transfers/{id}/respond` | Accept or refuse (target) | `uploads:read`, `uploads:write` |
| `POST /ownership-transfers/{id}/cancel` | Cancel a pending request (source) | `uploads:read`, `uploads:write` |

## When the project was shared with you

If a project was shared with you — you are a coauthor or reviewer, not the `main_author` — you
cannot transfer its ownership. Only the owner can initiate a transfer. A transfer request is
rejected:

```bash
curl -X POST "{{ nomad_url() }}/v1/ownership-transfers" \
  -H "Authorization: Bearer ${NOMAD_PAT}" \
  -H "Content-Type: application/json" \
  -d '{
    "resource_type": "upload",
    "resource_id": "<upload-id>",
    "target_user": "<target-user-id>",
    "target_user_type": "user_id"
  }'
```

```json
{ "detail": "Only main author has permissions for this operation." }
```

To move such a project to another account, the owner has to initiate the transfer to you.

What you *can* do with coauthor access is manage the project's collaborators. Adding a coauthor:

```bash
curl -X POST "{{ nomad_url() }}/v1/uploads/<upload-id>/edit" \
  -H "Authorization: Bearer ${NOMAD_PAT}" \
  -H "Content-Type: application/json" \
  -d '{"metadata": {"coauthors": {"add": ["<user-id-or-email>"]}}}'
```

The edit runs as a short background process and returns the updated project (abbreviated):

```json
{
  "upload_id": "<upload-id>",
  "data": {
    "process_status": "SUCCESS",
    "main_author": "<owner-user-id>",
    "coauthors": ["<your-user-id>", "<new-coauthor-user-id>"]
  }
}
```

The new coauthor gains access immediately. Removing a coauthor (including yourself) uses the
`remove` operation:

```bash
curl -X POST "{{ nomad_url() }}/v1/uploads/<upload-id>/edit" \
  -H "Authorization: Bearer ${NOMAD_PAT}" \
  -H "Content-Type: application/json" \
  -d '{"metadata": {"coauthors": {"remove": ["<user-id>"]}}}'
```

Removing yourself immediately revokes your own access to the project.
