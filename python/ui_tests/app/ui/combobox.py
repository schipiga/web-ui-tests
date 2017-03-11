from pom import ui
from pom.ui.base import timeit, PRESENCE_ERRORS


class ComboBox(ui.ComboBox):

    @property
    @timeit
    def is_present(self):
        """Define is combobox present at display."""
        try:
            is_displayed = self.webelement.is_displayed()
            if not is_displayed:
                css_prop = self.webelement.value_of_css_property
                if (css_prop('display') == 'block' and
                        css_prop('visibility') == 'visible' and
                        css_prop('opacity') == '0'):
                    return True
                else:
                    return False
            else:
                return True
        except PRESENCE_ERRORS:
            return False
