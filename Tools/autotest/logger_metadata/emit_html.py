'''
AP_FLAKE8_CLEAN
'''
import emitter


class HTMLEmitter(emitter.Emitter):
    def preface(self):
        return """<!-- Dynamically generated list of Logger Messages
This page was generated using Tools/autotest/logger_metdata/parse.py

DO NOT EDIT
-->


<h3 style="text-align: center">Onboard Message Log Messages</h3>
<hr />

<p>This is a list of log messages which may be present in logs produced and stored onboard ArduPilot vehicles.</p>

<!-- add auto-generated table of contents with "Table of Contents Plus" plugin -->
[toc exclude="Onboard Message Log Messages"]

"""

    def postface(self):
        return ""

    def start(self):
        self.fh = open("LogMessages.html", mode='w')
        print(self.preface(), file=self.fh)

    def emit(self, doccos, enumerations):
        self.start()
        for docco in doccos:
            print('    <h1>%s</h1>' % docco.name, file=self.fh)
            if docco.url is not None:
                print('        <a href="%s">More information</a>' % docco.url, file=self.fh)
            if docco.description is not None:
                print('        <h2>%s</h2>' %
                      docco.description, file=self.fh)
            print('        <table>', file=self.fh)
            print("        <tr><th>FieldName</th><th>Units/Type</th><th>Description</th><tr>",
                  file=self.fh)
            for f in docco.fields_order:
                if "description" in docco.fields[f]:
                    fdesc = docco.fields[f]["description"]
                else:
                    fdesc = ""
                if "units" in docco.fields[f] and docco.fields[f]["units"] != "":
                    ftypeunits = docco.fields[f]["units"]
                elif "fmt" in docco.fields[f] and "char" in docco.fields[f]["fmt"]:
                    ftypeunits = docco.fields[f]["fmt"]
                elif "bitmaskenum" in docco.fields[f]:
                    ftypeunits = "bitmask"
                elif "valueenum" in docco.fields[f]:
                    ftypeunits = "enum"
                else:
                    ftypeunits = ""
                print('        <tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (f, ftypeunits, fdesc),
                      file=self.fh)
            print('        </table>', file=self.fh)

            print("", file=self.fh)
        self.stop()

    def stop(self):
        print(self.postface(), file=self.fh)
        self.fh.close()
