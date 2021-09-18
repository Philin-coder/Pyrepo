import inspect
from selenium.webdriver.common.action_chains import ActionChains

print(inspect.getsource(ActionChains.click))


def click(self, on_element=None):
    """
    Clicks an element.

    :Args:
     - on_element: The element to click.
       If None, clicks on current mouse position.
    """
    if on_element:
        self.move_to_element(on_element)
    if self._driver.w3c:
        self.w3c_actions.pointer_action.click()
        self.w3c_actions.key_action.pause()
        self.w3c_actions.key_action.pause()
    else:
        self._actions.append(lambda: self._driver.execute(
            Command.CLICK, {'button': 0}))
    return self
