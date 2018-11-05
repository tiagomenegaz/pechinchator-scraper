import pytz
from datetime import datetime, timedelta
from html_sanitizer import Sanitizer

sanitizer = Sanitizer()


class SanitizeContentHTMLPipeline:

    def process_item(self, item, spider):
        if item["content_html"]:
            sanitizer.sanitize(item["content_html"])

        return item


class NormalizeThreadDatePipeline:

    def process_item(self, item, _spider):
        posted_at = item["posted_at"]
        timezone = pytz.timezone('America/Sao_Paulo')

        if "às" in posted_at:
            posted_at = posted_at.replace(" às ", " ")

        if "Hoje" in posted_at:
            hours, seconds = posted_at.strip("Hoje ").split(":")
            normalized_posted_at = datetime.today().replace(
                hour=int(hours), second=int(seconds))
        elif "Ontem" in posted_at:
            hours, seconds = posted_at.strip("Ontem ").split(":")
            normalized_posted_at = (datetime.today() - timedelta(days=1)).replace(
                hour=int(hours), second=int(seconds))
        else:
            normalized_posted_at = self.__parse_date(posted_at)

        item["posted_at"] = normalized_posted_at.astimezone(timezone)

        return item

    @staticmethod
    def __parse_date(date_str):
        for date_fmt in ('%d-%m-%Y %H:%M', '%d/%m/%Y %H:%M'):
            try:
                return datetime.strptime(date_str, date_fmt)
            except ValueError:
                pass
        raise ValueError('No valid date format')
