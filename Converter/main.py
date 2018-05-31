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



class ConverterHandler(BaseHandler):
    def get(self):
        return self.render_template(
            "converter.html"
        )

class ConverterResultHandler(BaseHandler):
    def post(self):
        amount = self.request.get("amount")
        selected_unit = self.request.get("unit")
        amount_two = None
        second_unit = None
        try:
            amount = float(amount)
            if selected_unit == "kilometers":
                amount_two = amount * 0.62
                second_unit = "miles"
            elif selected_unit == "miles":
                amount_two = amount * 1.6
                second_unit = "kilometers"
        except ValueError:
            return self.write("You need to enter a number!")

        params = {"unittwo": second_unit, "unitone": selected_unit, "num1": amount, "result": amount_two}




        return self.render_template(
                "converter-result.html",
            params = params
        )


app = webapp2.WSGIApplication([
    webapp2.Route('/', ConverterHandler),
    webapp2.Route("/converter-result", ConverterResultHandler)
], debug=True)
