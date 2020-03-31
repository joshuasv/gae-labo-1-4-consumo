#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import webapp2


class MainHandler(webapp2.RequestHandler):
    def post(self):
        try:
            km = float(self.request.get("lblKm"))
            time = float(self.request.get("lblTime"))
            avgCons = float(self.request.get("lblAvgCons"))

            # Velocidad media
            mv = km / time
            # Consumo total
            totalCons = km * avgCons

            response = """
                <html>
                <head>
                <meta charset="utf-8">
                <title>Consumo</title>
                </head>
                <body>
                <h1>Consumo</h1>
                <p>Velocidad media: {} km/h</p>
                <br>
                <p>Consumo total: {} litros</p>
                </body>
                </html>
            """.format(int(mv), int(totalCons))

            self.response.write(response)
        except (TypeError, ValueError):
            self.response.write("<html><body><p>Valores introducidos inválidos</p></body></html>")




app = webapp2.WSGIApplication([
    ('/calcula', MainHandler)
], debug=True)
