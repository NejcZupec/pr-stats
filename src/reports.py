import jinja2
import os


class ReportGenerator(object):

    def __init__(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(this_dir, 'templates')
        loader = jinja2.FileSystemLoader(template_dir)
        self.jinja_env = jinja2.Environment(loader=loader)

    def render_report(self):
        template = self.jinja_env.get_template('base.html')
        print(template.render(pull_requests=[]))


if __name__ == '__main__':
    generator = ReportGenerator()
    generator.render_report()
