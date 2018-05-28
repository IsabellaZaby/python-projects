#!/usr/bin/env python
import os
import jinja2
import webapp2
from random import *


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        number_one = float(self.request.get("number_one"))
        number_two = float(self.request.get("number_second"))
        operator = self.request.get("operator")

        result = None

        if operator == "addition":
            result = number_one + number_two
        elif operator == "subtraction":
            result = number_one - number_two
        elif operator == "multiplication":
            result = number_one * number_two
        elif operator == "division":
            try:
                result = number_one / number_two
            except ZeroDivisionError:
                return self.write("You can not divide by 0!")


        self.write("Result is %s." % result)



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
