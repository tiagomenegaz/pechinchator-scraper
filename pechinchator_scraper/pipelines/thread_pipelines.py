from html_sanitizer import Sanitizer

sanitizer = Sanitizer()


class SanitizeContentHTMLPipeline:

    def process_item(self, item, spider):
        if item["content_html"]:
            sanitizer.sanitize(item["content_html"])

        return item
