from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.docutils import SphinxDirective

import os
import yaml

with open(os.path.join(os.path.dirname(__file__), "common_dt_bindings_reference.yaml"), "r") as f:
    db = yaml.safe_load(f)

class DeviceTreeParser(SphinxDirective):

    required_arguments = 1
    # has_content = True

    def build_table(self, props):
        # node = nodes.container(type="device-tree-table")
        global db
        cols = 5
        table = nodes.table()
        tgroup = nodes.tgroup(cols=cols)
        for _ in range(cols):
            colspec = nodes.colspec(colwidth=1)
            tgroup.append(colspec)
        table += tgroup

        thead = nodes.thead()
        tgroup += thead
        
        row = nodes.row()

        entry = nodes.entry()
        entry += nodes.paragraph(text="Property")
        row += entry

        entry = nodes.entry()
        entry += nodes.paragraph(text="Type")
        row += entry

        entry = nodes.entry()
        entry += nodes.paragraph(text="Description")
        row += entry

        entry = nodes.entry()
        entry += nodes.paragraph(text="Range")
        row += entry

        entry = nodes.entry()
        entry += nodes.paragraph(text="maxItems")
        row += entry


        thead.append(row)

        rows = []

        for prop in props:
            row = nodes.row()

            entry = nodes.entry()
            entry += nodes.paragraph(text=prop)
            row += entry

            entry = nodes.entry()
            if 'allOf' in props[prop]:
                text = props[prop]['allOf'][0]['$ref'].split('/')[-1]
            else:
                text = ''
            entry += nodes.paragraph(text=text)
            row += entry

            entry = nodes.entry()
            if 'description' in props[prop]:
                text = props[prop]['description']
            else:
                if prop in db:
                    text = db[prop]['description']
                else:
                    text = ''

            if prop == "spi-max-frequency" and text == "":
                print("WTF21321", prop)
            entry += nodes.paragraph(text=text)
            row += entry


            entry = nodes.entry()
            if 'allOf' in props[prop]:
                mi = props[prop]['allOf'][1]['minimum']
                ma = props[prop]['allOf'][2]['maximum']
                text = '{} to {}'.format(mi, ma)
            else:
                text = ''
            entry += nodes.paragraph(text=text)
            row += entry

            entry = nodes.entry()
            if 'maxItems' in props[prop]:
                entry += nodes.paragraph(text=props[prop]['maxItems'])
            else:
                entry += nodes.paragraph(text='')
            row += entry

            rows.append(row)

        tbody = nodes.tbody()
        tbody.extend(rows)
        tgroup += tbody

        return table

    def get_yaml(self, fn):
        # s = os.path.join(self.config.dt_bindings_include_path,fn)
        s = fn
        print(s)
        if not os.path.exists(s):
            raise Exception("File not found: {}".format(s))
        try:
            with open(s, 'r') as f:
                data = yaml.safe_load(f)
                # data = yaml.load(f, Loader=yaml.FullLoader)
        except:
            raise Exception("Invalid yaml file: {}".format(s))

        try:
            # props = data['patternProperties']['^channel@[0-9]$']['properties']
            if "properties" in data:
                props = data['properties']
            else:
                return []

            node = nodes.container(type="device-tree-table")
            node += self.build_table(props)

            sn = fn.split('/')[-1].split('.')[0]
            title = nodes.title(text=sn)

            return [title, node]
        except Exception as e:
            print(e)
            # raise Exception("Yaml data parse failed for file: {}".format(s))
            return []

        # return sections

    def run(self):
        return self.get_yaml(self.arguments[0])


def setup(app):
    app.add_config_value('dt_bindings_include_path', None, 'html')
    app.add_directive("devicetree", DeviceTreeParser)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
