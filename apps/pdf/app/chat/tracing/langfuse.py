import os
from langfuse.callback import CallbackHandler
langfuse_callback_handler = CallbackHandler(
    os.environ["LANGFUSE_PUBLIC_KEY"],
    os.environ["LANGFUSE_SECRET_KEY"],
    host=os.environ["LANGFUSE_HOST"]
)
