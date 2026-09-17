# How to transfer upload ownership

This guide shows how to transfer ownership of an upload (a *project* in the GUI) to another
user, both through the GUI and through the API. For the underlying model — the two-phase
request/accept flow, pending-state access, and notifications — see
[Explanation > Ownership transfer](../../explanation/ownership_transfer.md).

## What you will learn

- How the current owner offers ownership and the recipient accepts or refuses.
- How to do this in the GUI and, equivalently, through the API.

## Recommended preparation

- [Explanation > Ownership transfer](../../explanation/ownership_transfer.md)
- [How-to > Authenticate programmatically](./program/auth.md) (for the API workflow)

## Using the GUI

**As the current owner — offer ownership:**

1. Open the project you own.
2. Open its ownership actions and choose **Transfer ownership**.
3. In the dialog, search for and select the target user.
4. Confirm. A pending request is created and the recipient is notified; the project now shows
   a pending transfer, which you can **cancel** from the same place until it is accepted.

**As the recipient — accept or refuse:**

1. You receive an in-app notification that you have been offered ownership of the project (you
   also gain read access to it while the request is pending).
2. Open the project and choose **Accept** to take ownership, or **Refuse** to decline.

On acceptance, you become the project's owner. On refusal, ownership stays with the original
owner and the temporary access is removed.

## Using the API

The same flow is available through the `ownership-transfers` endpoints. The state-changing
calls require a token with `uploads:write`; see
[Authenticate programmatically](./program/auth.md).

**Request the transfer (current owner).** Identify the target by `user_id`, `username`, or
`email` via `target_user_type`:

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

**Review the pending request (either party).**

```bash
# List transfers involving you
curl "{{ nomad_url() }}/v1/ownership-transfers" \
  -H "Authorization: Bearer ${NOMAD_PAT}"

# Inspect a single transfer
curl "{{ nomad_url() }}/v1/ownership-transfers/<transfer-id>" \
  -H "Authorization: Bearer ${NOMAD_PAT}"
```

**Accept or refuse (target).** On `accept`, `main_author` is reassigned to the target:

```bash
curl -X POST "{{ nomad_url() }}/v1/ownership-transfers/<transfer-id>/respond?resource_type=upload" \
  -H "Authorization: Bearer ${NOMAD_PAT}" \
  -H "Content-Type: application/json" \
  -d '{"action": "accept"}'
```

Use `{"action": "refuse"}` to decline.

**Cancel a pending request (source).** Before the target responds, the source can cancel,
which revokes the target's temporary reviewer access:

```bash
curl -X POST "{{ nomad_url() }}/v1/ownership-transfers/<transfer-id>/cancel?resource_type=upload" \
  -H "Authorization: Bearer ${NOMAD_PAT}"
```

**Verify the result.** Reassigning ownership runs as a background process on the upload.
Confirm that `main_author` is the new owner and that `process_status` completed successfully:

```bash
curl "{{ nomad_url() }}/v1/uploads/<upload-id>" \
  -H "Authorization: Bearer ${NOMAD_PAT}"
```

### Endpoint reference

| Method & path | Purpose | Required scopes |
| --- | --- | --- |
| `POST /ownership-transfers` | Request a transfer (source) | `uploads:read`, `uploads:write` |
| `GET /ownership-transfers` | List your transfers | `uploads:read` |
| `GET /ownership-transfers/{id}` | Inspect one transfer | `uploads:read` |
| `POST /ownership-transfers/{id}/respond` | Accept or refuse (target) | `uploads:read`, `uploads:write` |
| `POST /ownership-transfers/{id}/cancel` | Cancel a pending request (source) | `uploads:read`, `uploads:write` |
