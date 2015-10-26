from flask.globals import current_app
from flask_debugtoolbar.panels import DebugPanel


str_template = """
<table>
    <thead>
        <tr>
            <th>Key</th>
            <th>Value</th>
        </tr>
    </thead>
    <tbody>
        {% for key, fnc  in filters|dictsort %}
            <tr class="{{ loop.cycle('flDebugOdd', 'flDebugEven') }}">
                <td>{{ key }}</td>
                <td><code>{{ fnc.__doc__ }}</code></td>
            </tr>
        {% endfor %}
    </tbody>
</table>
"""


class TemplateFiltersDebugPanel(DebugPanel):
    name = 'TemplateFilters'
    has_content = True

    def nav_title(self):
        return 'Template Filters'

    def title(self):
        return 'Template Filters'

    def nav_subtitle(self):
        return '%d available' % len(current_app.jinja_env.filters)

    def url(self):
        return ''

    def content(self):
        template = self.jinja_env.from_string(str_template)
        return template.render(
            filters=current_app.jinja_env.filters
        )
