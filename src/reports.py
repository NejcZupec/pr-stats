import jinja2
import os

from src.data_fetcher import DataFetcher


class ReportGenerator(object):

    def __init__(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(this_dir, 'templates')
        loader = jinja2.FileSystemLoader(template_dir)
        self.jinja_env = jinja2.Environment(loader=loader)

    def render_report(self):
        template = self.jinja_env.get_template('base.html')
        content = template.render(
            pull_requests=DataFetcher().get_pull_requests(),
        )
        # TODO: wrap with try/catch
        f = open('report.html', 'w')
        f.write(content)
        f.close()


if __name__ == '__main__':
    generator = ReportGenerator()
    generator.render_report()
