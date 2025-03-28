## The `update_entry` method

The root context, which is available from the `.m_context` of a `EntryArchive`, which could be accessed via `section.m_root().m_context` if `section` is attached to a `EntryArchive`, provides the functionality to update/create child entries on-the-fly and invoke the processing if necessary.

!!! note
    The usage of this functionality is strongly discouraged and should be avoided if possible.

The method has the following signature.

```python
    @contextmanager
    def update_entry(
        self,
        mainfile: str,
        *,
        write: bool = False,
        process: bool = False,
        **kwargs,
    ):
        """
        Open the target file and send it to the updater function.
        The updater function shall return the updated file content.
        The updated file will be stored and processed if needed.

        WARNING:
            If `process=True`, the updated file will be processed immediately.
            Please be aware of the fact that this method may be called during the processing of
            the parent/main file.
            This means if there are any data dependencies, there is a risk of infinite loops,
            racing conditions and/or other unexpected behavior.
            You must carefully design the logic to mitigate these risks.

        To use this function, you shall use the with-statement as follows:

        ```python
        with context.update_entry('mainfile.json',**kwargs) as content:
            # do something with content
        ```

        Parameters:
            mainfile: The relative path (from upload root) to the file to update.
            write: Whether to write the updated file back to the storage.
                If False, no processing will be triggered whatsoever.
            process: Whether to trigger processing of the updated file.
        """
        ...
```

It is wrapped with a `@contextmanager` decorator, thus it shall be used with a `with` block.
It yields a plain `dict` object that represents the content of the file.

```python
# get the context from the current archive
context = section.m_root().m_context
# create/update the file 'mainfile.json' and process it
with context.update_entry('mainfile.json', process=True) as content_dict:
    # do something with content
    content_dict['key'] = 'value'
    ...
```

The main file must be a `json` or `yaml` file.
Other formats are not supported.

If only need to read the content, leave `write=False`.
Otherwise, set `write=True` to store the updated content back to the storage.

It is possible to invoke the processing immediately by setting `process=True`.
However, this is not recommended due to various security concerns.

The following caveats must be acknowledged when using this method:

1. The specific logic of creating/updating the file must be re-entrant safe, see [details](https://en.wikipedia.org/wiki/Reentrancy_(computing)).
   To put simply, the first call and subsequent calls must yield the same result regardless of what is already stored in the file.
2. A child entry must **not** be accessed by multiple parent entries.
   Because the parent entries are processed in parallel (by multiple `celery` workers), there is a risk of racing conditions if the child entry is accessed by multiple parent entries.
3. The child entry shall not modify the parent entry (and any other entries).
   Otherwise, there is a risk of infinite loops and data corruption.
4. A child entry shall **not** depend on other child entries.
