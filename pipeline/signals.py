from django.dispatch import Signal


css_compressed = Signal(providing_args=["package"])
js_compressed = Signal(providing_args=["package"])
