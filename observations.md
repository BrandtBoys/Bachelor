# Observations

## Out of memory error
When loading the semantic score, this error occurred.

The diff changes involved 15 files.
### Error message
``` shell
  File "/Users/markushojgaard/Documents/ITU/6._semester/Bachelor/Bachelor/test.py", line 276, in <module>
    main()
  File "/Users/markushojgaard/Documents/ITU/6._semester/Bachelor/Bachelor/test.py", line 88, in main
    add_commit_run_agent(commit.sha)
  File "/Users/markushojgaard/Documents/ITU/6._semester/Bachelor/Bachelor/test.py", line 137, in add_commit_run_agent
    create_csv(repo, branch_name, modified_files, commit_sha, result_file)
  File "/Users/markushojgaard/Documents/ITU/6._semester/Bachelor/Bachelor/metrics.py", line 38, in create_csv
    scores = calculate_semantic_scores(comment_pairs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/markushojgaard/Documents/ITU/6._semester/Bachelor/Bachelor/metrics.py", line 49, in calculate_semantic_scores
    scores = model.predict(commentPairs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/sentence_transformers/cross_encoder/CrossEncoder.py", line 441, in predict
    model_predictions = self.model(**features, return_dict=True)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/transformers/models/roberta/modeling_roberta.py", line 1320, in forward
    outputs = self.roberta(
              ^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/transformers/models/roberta/modeling_roberta.py", line 976, in forward
    encoder_outputs = self.encoder(
                      ^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/transformers/models/roberta/modeling_roberta.py", line 631, in forward
    layer_outputs = layer_module(
                    ^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/transformers/models/roberta/modeling_roberta.py", line 520, in forward
    self_attention_outputs = self.attention(
                             ^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/transformers/models/roberta/modeling_roberta.py", line 447, in forward
    self_outputs = self.self(
                   ^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/transformers/models/roberta/modeling_roberta.py", line 370, in forward
    attn_output = torch.nn.functional.scaled_dot_product_attention(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: MPS backend out of memory (MPS allocated: 1.73 GB, other allocations: 4.80 GB, max allowed: 6.80 GB). Tried to allocate 384.00 MB on private pool. Use PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0 to disable upper limit for memory allocations (may cause system failure).
```

## Code injection hazard
With this prompt we get this comment.

Another problem here is also that the function definition is included in the answer

### prompt
```shell
"""
  You are a documentation assistant.

  ## Instructions:
  - Given the code, make an **only** descriptive comment of the function
  - follow best comment practice regrading to the file language
  - if there is a old comment, update that to reflect the changes to the function
  - your answer will be directly inserted into code of type file language, so you answer has to be able to compile in the give file language
  - do **not** include the function definition in your answer

  ##file language:
  {file_language}

  ## Code:
  {code}

  ## Old comment:
  {old_comment}

  Return **only** the comment:
"""
```

### LLM generated comment
``` shell
'''python
def send_from_directory(
    directory: os.PathLike[str] | str,
    path: os.PathLike[str] | str,
    **kwargs: t.Any,
) -> Response:
    """
    Sends a file from the specified directory.

    Parameters:
        directory (os.PathLike[str] | str): The directory to send the file from.
        path (os.PathLike[str] | str): The path of the file to send.
        **kwargs: Additional keyword arguments for sending the file.

    Returns:
        Response: The response object containing the sent file.
    """
'''
```

## note

parent parent type
function_definition
43808
parent type
block
43891

('def get_debug_flag() -> bool:\n    """Get whether debug mode should be enabled for the app, indicated by the\n    :envvar:`FLASK_DEBUG` environment variable. The default is ``False``.\n    """\n    val = os.environ.get("FLASK_DEBUG")\n    return bool(val and val.lower() not in {"0", "false", "no"})', '')