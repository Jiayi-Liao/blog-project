import markdown
from django.test import TestCase, RequestFactory

class MarkdownTest(TestCase):
    s = """
        ~~~~{.python}
        # python code
        ~~~~

        ~~~~.html
        <p>HTML Document</p>
        ~~~~
        """
    format_s = markdown.markdown(s, extensions=['markdown.extensions.fenced_code'])
    print format_s
