import os

# Prevent external/third-party pytest plugins from auto-loading, which can
# break test discovery/execution in isolated environments.
os.environ.setdefault("PYTEST_DISABLE_PLUGIN_AUTOLOAD", "1")


