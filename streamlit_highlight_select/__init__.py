import streamlit as st
import streamlit.components.v1 as components

_component_func = components.declare_component(
    # Give the component a simple, descriptive name ("my_component"
    # does not fit this bill, so please choose something better for your
    # own component :)
    "highlight_select_component",
    url="http://localhost:3001",
)

# Wrapper function for the component. 
def highlight_select_component(name, key=None):
    """Create a new instance of "my_component".

    Parameters
    ----------
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # This is where we through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(name=name, key=key, default="?")

    # We could modify the value returned from the component if we wanted.

    return component_value

# Use data returned from component

st.subheader("Highlight Select Component")

# Create an instance of our component with a constant `name` arg, and
# print its output value.

return_string = highlight_select_component("World")
st.markdown("Return string: %s " % str(return_string))

