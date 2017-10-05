import jinja2
import os

from src.data_fetcher import DataFetcher


class BaseReportGenerator(object):

    def __init__(self, template_file, output_filename):
        self.jinja_template = self._prepare_jinja_template(template_file)
        self.output_filename = output_filename

    @staticmethod
    def _prepare_jinja_template(template_file):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(this_dir, 'templates')
        loader = jinja2.FileSystemLoader(template_dir)
        jinja_env = jinja2.Environment(loader=loader)
        return jinja_env.get_template(template_file)

    @staticmethod
    def _write_file(filename, content):
        # TODO: wrap with try/catch
        f = open(filename, 'w')
        f.write(content)
        f.close()

    @staticmethod
    def _get_context():
        raise NotImplementedError

    def generate_report(self):
        rendered_report = self.jinja_template.render(**self._get_context())
        output_file = 'output/{}'.format(self.output_filename)
        self._write_file(output_file, rendered_report)


class PullRequestsListReport(BaseReportGenerator):

    def __init__(self):
        super(PullRequestsListReport, self).__init__(
            template_file='pull_requests_list.html',
            output_filename='pull_requests_list_report.html',
        )

    @staticmethod
    def _get_context():
        return {
            'pull_requests': DataFetcher().get_pull_requests(),
        }


if __name__ == '__main__':

    # pull requests list report
    report_generator = PullRequestsListReport()
    report_generator.generate_report()
